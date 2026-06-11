<#
.SYNOPSIS
  Làm sạch MD đề trắc nghiệm dump từ web (TMU - Onschool) cho preview-friendly.

.DESCRIPTION
  Pattern xử lý cho từng file MD:
    1. Strip BOM + dòng noise lặp lại: header "<date>PMTMU - Onschool", "Thoát",
       "Theo dõi trả lời", "+1 điểm", title duplicate với filename.
    2. Convert "Câu N:" → "## Câu N".
    3. Join các dòng wrap của câu hỏi thành 1 paragraph.
    4. Convert "A.text" / "B.text" → "- A. text" / "- B. text" (markdown list).
    5. Thêm front-matter YAML + H1 heading lấy từ filename.
    6. Tính SHA-256 của PDF gốc (sibling exercises/pdf/<basename>.pdf) → source_hash.

  Ghi đè tại chỗ. Git tracks lịch sử, không cần backup riêng.

.PARAMETER Path
  File MD hoặc folder chứa nhiều MD. Bắt buộc.

.PARAMETER SubjectSlug
  ASCII kebab-case cho field `subject:` trong front-matter (vd: "mua-va-quan-tri-nguon-cung").

.PARAMETER DryRun
  Chỉ in báo cáo, không ghi file. Show 1 câu before/after để verify format.

.EXAMPLE
  pwsh scripts/fix-exercise-md.ps1 -Path "subjects/Mua và quản trị nguồn cung/exercises/md" -SubjectSlug "mua-va-quan-tri-nguon-cung"
  pwsh scripts/fix-exercise-md.ps1 -Path "<single>.md" -SubjectSlug "..." -DryRun
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory)][string]$Path,
    [Parameter(Mandatory)][string]$SubjectSlug,
    [switch]$DryRun
)

$ErrorActionPreference = 'Stop'

# Regex patterns cho noise
$NoisePatterns = @(
    '^\d+/\d+/\d+,\s*\d+:\d+\s*(AM|PM)TMU\s*-\s*Onschool\s*$',
    '^Thoát\s*$',
    '^Theo dõi trả lời\s*$',
    '^\+\s*1\s*điểm\s*$',
    '^Bài tập đã làm.*$',
    '^[^/]+/\s*Luyện tập trắc nghiệm.*$'  # title line dup
)

function Test-NoiseLine {
    param([string]$Line)
    foreach ($pat in $NoisePatterns) {
        if ($Line -match $pat) { return $true }
    }
    return $false
}

function Get-PdfHash {
    param([string]$MdPath)
    $baseName = [IO.Path]::GetFileNameWithoutExtension($MdPath)
    $mdDir = Split-Path -Parent $MdPath
    $pdfPath = Join-Path (Split-Path -Parent $mdDir) "pdf\$baseName.pdf"
    if (Test-Path $pdfPath) {
        $hash = (Get-FileHash -Path $pdfPath -Algorithm SHA256).Hash.ToLower()
        return "sha256:$hash"
    }
    return $null
}

function New-Question {
    param(
        [int]$Num,
        [System.Collections.Generic.List[string]]$QLines,
        [System.Collections.Generic.List[pscustomobject]]$Opts
    )
    $joined = ($QLines -join ' ').Trim()
    $normalized = $joined -replace '\s+', ' '
    return [pscustomobject]@{
        Num      = $Num
        Question = $normalized
        Options  = @($Opts)
    }
}

function Convert-ExerciseMd {
    param([string]$InputPath)

    $rawLines = Get-Content -Path $InputPath -Encoding UTF8

    if ($rawLines.Count -gt 0 -and $rawLines[0].Length -gt 0 -and [int][char]$rawLines[0][0] -eq 0xFEFF) {
        $rawLines[0] = $rawLines[0].Substring(1)
    }

    $state = 'before_first_question'
    $currentQ = 0
    $questionLines = New-Object System.Collections.Generic.List[string]
    $options = New-Object System.Collections.Generic.List[pscustomobject]
    $parsedQuestions = New-Object System.Collections.Generic.List[pscustomobject]

    foreach ($rawLine in $rawLines) {
        $line = $rawLine.TrimEnd()

        if ([string]::IsNullOrWhiteSpace($line)) { continue }
        if (Test-NoiseLine $line) { continue }

        # Câu mới
        if ($line -match '^Câu\s+(\d+)\s*:?\s*$') {
            if ($currentQ -gt 0) {
                $parsedQuestions.Add((New-Question -Num $currentQ -QLines $questionLines -Opts $options))
            }
            $currentQ = [int]$matches[1]
            $questionLines = New-Object System.Collections.Generic.List[string]
            $options = New-Object System.Collections.Generic.List[pscustomobject]
            $state = 'reading_question'
            continue
        }

        # Đáp án A./B./C./D./E.
        if ($line -match '^([A-E])\s*[\.\)]\s*(.*)$') {
            $letter = $matches[1]
            $text = $matches[2].Trim()
            $state = 'reading_options'
            $options.Add([pscustomobject]@{ Letter = $letter; Text = $text })
            continue
        }

        # Text line — phụ thuộc state
        if ($state -eq 'reading_question') {
            $questionLines.Add($line.Trim())
        }
        elseif ($state -eq 'reading_options' -and $options.Count -gt 0) {
            $last = $options[$options.Count - 1]
            $merged = ($last.Text + ' ' + $line.Trim()).Trim()
            $last.Text = $merged -replace '\s+', ' '
        }
    }

    # Flush câu cuối
    if ($currentQ -gt 0) {
        $parsedQuestions.Add((New-Question -Num $currentQ -QLines $questionLines -Opts $options))
    }

    return ,$parsedQuestions
}

function Format-Output {
    param(
        [string]$InputPath,
        [array]$Questions,
        [string]$SubjectSlug
    )

    $baseName = [IO.Path]::GetFileNameWithoutExtension($InputPath)
    $pdfName = "$baseName.pdf"
    $pdfHash = Get-PdfHash -MdPath $InputPath
    $timestamp = (Get-Date).ToString('yyyy-MM-ddTHH:mm:ssK')

    $title = $baseName -replace '^[^_]+_', ''

    $sb = New-Object System.Text.StringBuilder
    [void]$sb.AppendLine('---')
    [void]$sb.AppendLine("source_pdf: `"$pdfName`"")
    if ($pdfHash) {
        [void]$sb.AppendLine("source_hash: `"$pdfHash`"")
    }
    [void]$sb.AppendLine("cleaned_at: `"$timestamp`"")
    [void]$sb.AppendLine("subject: `"$SubjectSlug`"")
    [void]$sb.AppendLine('doc_type: "exercise"')
    [void]$sb.AppendLine("total_questions: $($Questions.Count)")
    [void]$sb.AppendLine('---')
    [void]$sb.AppendLine('')
    [void]$sb.AppendLine("# $title")
    [void]$sb.AppendLine('')

    foreach ($q in $Questions) {
        [void]$sb.AppendLine("## Câu $($q.Num)")
        [void]$sb.AppendLine('')
        [void]$sb.AppendLine($q.Question)
        [void]$sb.AppendLine('')
        foreach ($opt in $q.Options) {
            [void]$sb.AppendLine("- $($opt.Letter). $($opt.Text)")
        }
        [void]$sb.AppendLine('')
    }

    return $sb.ToString().TrimEnd() + "`n"
}

# === Main ===
$resolved = Resolve-Path -Path $Path
if (Test-Path $resolved -PathType Container) {
    $files = Get-ChildItem -Path $resolved -Filter '*.md' -File
} else {
    $files = @(Get-Item $resolved)
}

if ($files.Count -eq 0) {
    Write-Warning "Không tìm thấy file MD nào tại: $Path"
    exit 1
}

Write-Host "Processing $($files.Count) file(s) with subject slug: $SubjectSlug" -ForegroundColor Cyan
if ($DryRun) {
    Write-Host "(DRY RUN — không ghi file)" -ForegroundColor Yellow
}
Write-Host ''

foreach ($file in $files) {
    $questions = Convert-ExerciseMd -InputPath $file.FullName
    $output = Format-Output -InputPath $file.FullName -Questions $questions -SubjectSlug $SubjectSlug

    Write-Host "[$($file.Name)]" -ForegroundColor Green
    Write-Host "  Questions parsed: $($questions.Count)"

    $missingOpts = @($questions | Where-Object { $_.Options.Count -lt 2 })
    if ($missingOpts.Count -gt 0) {
        $nums = ($missingOpts | ForEach-Object { $_.Num }) -join ', '
        Write-Host "  WARN: $($missingOpts.Count) câu có <2 options — kiểm tra câu: $nums" -ForegroundColor Yellow
    }

    if ($DryRun) {
        if ($questions.Count -gt 0) {
            Write-Host "  --- Preview Câu 1 ---" -ForegroundColor DarkGray
            $previewQ = $questions[0]
            Write-Host "  ## Câu $($previewQ.Num)"
            Write-Host ''
            Write-Host "  $($previewQ.Question)"
            Write-Host ''
            foreach ($opt in $previewQ.Options) {
                Write-Host "  - $($opt.Letter). $($opt.Text)"
            }
            Write-Host '  ---' -ForegroundColor DarkGray
        }
    } else {
        Set-Content -Path $file.FullName -Value $output -Encoding UTF8 -NoNewline
        Write-Host "  Wrote $($output.Length) bytes" -ForegroundColor DarkGreen
    }
    Write-Host ''
}

if ($DryRun) {
    Write-Host "DRY RUN complete. Bỏ -DryRun để ghi file." -ForegroundColor Yellow
} else {
    Write-Host "Done. Chạy: pwsh scripts/check-project.ps1 -Subject `"<tên môn>`" để verify." -ForegroundColor Cyan
}
