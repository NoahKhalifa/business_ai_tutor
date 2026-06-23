<#
.SYNOPSIS
  Audit trạng thái project Business AI Tutor.

.DESCRIPTION
  Quét từng môn trong `subjects/` (bỏ `_template`) và kiểm tra:
    - metadata.yaml có tồn tại không
    - Đủ folder bắt buộc: lectures/{pdf,md}, exercises/{pdf,md}, solutions, extensions
    - Folder audio nếu metadata.yaml có `media_types: ["audio"]`
    - PDF nhưng chưa có MD tương ứng (cache stale hoặc chưa convert)
    - Solution có status gì, đã có review chưa, đã có extension chưa
    - exercise_file trong front-matter có trỏ về file thật trong exercises/md/ không

  In báo cáo markdown ra stdout. Exit 1 nếu có issues, 0 nếu sạch.

.PARAMETER WriteStatus
  Sinh STATUS.md (auto-generated) cho mỗi môn được audit. Đè file cũ.

.PARAMETER Subject
  Giới hạn audit về 1 môn (theo tên folder).

.EXAMPLE
  pwsh scripts/check-project.ps1
  pwsh scripts/check-project.ps1 -WriteStatus
  pwsh scripts/check-project.ps1 -Subject "Quản trị marketing"
#>

[CmdletBinding()]
param(
    [switch]$WriteStatus,
    [string]$Subject
)

$ErrorActionPreference = 'Stop'

# Project root = parent của scripts/
$ProjectRoot = Split-Path -Parent $PSScriptRoot
$SubjectsDir = Join-Path $ProjectRoot 'subjects'
if (-not (Test-Path $SubjectsDir)) {
    throw "Subjects directory not found: $SubjectsDir"
}

function Test-AudioEnabled {
    param([string]$MetadataPath)
    if (-not (Test-Path $MetadataPath)) { return $false }
    $content = Get-Content $MetadataPath -Raw -Encoding UTF8
    if ($content -match '(?m)^media_types:\s*\[([^\]]*)\]') {
        return $matches[1] -match 'audio'
    }
    return $false
}

function Get-FrontMatterField {
    param(
        [string]$FilePath,
        [string]$Field
    )
    if (-not (Test-Path $FilePath)) { return $null }
    $lines = Get-Content $FilePath -Encoding UTF8 -TotalCount 30
    foreach ($line in $lines) {
        if ($line -match "^${Field}:\s*`"?([^`"]+)`"?\s*$") {
            return $matches[1].Trim()
        }
    }
    return $null
}

# Normalize body content for boilerplate detection:
# strip front-matter, chapter/question numbers, dates, scores → so 2 file khác chương vẫn so được phần lập luận chung.
function Get-NormalizedBody {
    param([string]$FilePath)
    if (-not (Test-Path $FilePath)) { return '' }
    $raw = Get-Content $FilePath -Raw -Encoding UTF8
    if (-not $raw) { return '' }
    # Strip front-matter giữa 2 dòng ---
    $body = $raw -replace '(?s)^---\s*\r?\n.*?\r?\n---\s*\r?\n', ''
    # Strip markdown headings (### Heading...) - structure lặp lại không phải boilerplate explanation
    $body = $body -replace '(?m)^#{1,6}\s+.*$', ''
    # Strip "Chương N" / "chương N" (mọi dấu)
    $body = $body -replace '(?i)Ch(ư|u)(ơ|o)ng\s*\d+', 'CHX'
    # Strip "Câu N" / "QN" / "Q.N"
    $body = $body -replace '(?i)(Câu|Q\.?)\s*\d+', 'QX'
    # Strip dates YYYY-MM-DD
    $body = $body -replace '\d{4}-\d{2}-\d{2}', 'DATE'
    # Strip scores X.X/10 hoặc X/10
    $body = $body -replace '\d+(\.\d+)?\s*/\s*10', 'SCORE'
    # Strip line/page refs "dòng X-Y", "trang N"
    $body = $body -replace '(?i)d(ò|o)ng\s*\d+(-\d+)?', 'LINE'
    $body = $body -replace '(?i)trang\s*\d+', 'PAGE'
    # Collapse whitespace
    $body = $body -replace '\s+', ' '
    return $body.Trim()
}

# Tách body đã normalize thành 5-gram shingles (5 từ liên tiếp) để Jaccard bắt boilerplate
# tốt hơn split-by-sentence (vốn fail khi text bị collapse whitespace).
function Get-ShingleSet {
    param(
        [string]$Text,
        [int]$N = 5
    )
    if (-not $Text) { return @() }
    $tokens = $Text -split '\s+' | Where-Object { $_.Length -gt 0 }
    if ($tokens.Count -lt $N) { return @() }
    $set = New-Object 'System.Collections.Generic.HashSet[string]'
    for ($i = 0; $i -le $tokens.Count - $N; $i++) {
        $shingle = ($tokens[$i..($i + $N - 1)] -join ' ').ToLowerInvariant()
        [void]$set.Add($shingle)
    }
    return @($set)
}

function Get-JaccardSimilarity {
    param(
        [string[]]$SetA,
        [string[]]$SetB
    )
    if ($SetA.Count -eq 0 -or $SetB.Count -eq 0) { return 0.0 }
    $a = New-Object 'System.Collections.Generic.HashSet[string]' (,[string[]]$SetA)
    $b = New-Object 'System.Collections.Generic.HashSet[string]' (,[string[]]$SetB)
    $intersect = New-Object 'System.Collections.Generic.HashSet[string]' (,[string[]]$SetA)
    $intersect.IntersectWith($b)
    $union = New-Object 'System.Collections.Generic.HashSet[string]' (,[string[]]$SetA)
    $union.UnionWith($b)
    if ($union.Count -eq 0) { return 0.0 }
    return [double]$intersect.Count / [double]$union.Count
}

# Đếm số shingle N-gram lặp lại >= MinRepeat lần trong cùng 1 file.
# Pattern boilerplate phổ biến nhất: solver giải MCQ dùng cùng 1 cụm explain cho mọi câu.
function Get-IntraFileRepetition {
    param(
        [string]$FilePath,
        [int]$N = 10,
        [int]$MinRepeat = 5
    )
    $body = Get-NormalizedBody -FilePath $FilePath
    $tokens = $body -split '\s+' | Where-Object { $_.Length -gt 0 }
    if ($tokens.Count -lt $N) { return @() }
    $counts = @{}
    for ($i = 0; $i -le $tokens.Count - $N; $i++) {
        $sh = ($tokens[$i..($i + $N - 1)] -join ' ').ToLowerInvariant()
        if ($counts.ContainsKey($sh)) { $counts[$sh] += 1 } else { $counts[$sh] = 1 }
    }
    $hits = @()
    foreach ($k in $counts.Keys) {
        if ($counts[$k] -ge $MinRepeat) {
            $hits += [pscustomobject]@{ Phrase = $k; Count = $counts[$k] }
        }
    }
    return @($hits | Sort-Object Count -Descending)
}

function Find-IntraFileBoilerplate {
    param(
        [string]$Folder,
        [string]$Pattern,
        [int]$N = 10,
        [int]$MinRepeat = 5
    )
    $result = New-Object System.Collections.Generic.List[pscustomobject]
    if (-not (Test-Path $Folder)) { return $result }
    foreach ($f in @(Get-ChildItem $Folder -Filter $Pattern -ErrorAction SilentlyContinue)) {
        $hits = Get-IntraFileRepetition -FilePath $f.FullName -N $N -MinRepeat $MinRepeat
        if ($hits.Count -gt 0) {
            $top = $hits[0]
            $result.Add([pscustomobject]@{
                File           = $f.Name
                UniquePhrases  = $hits.Count
                TopPhraseCount = $top.Count
                TopPhrase      = $top.Phrase.Substring(0, [Math]::Min(80, $top.Phrase.Length))
            })
        }
    }
    return $result
}

# Trả về list các cặp file có Jaccard >= Threshold → flag template copy-paste cross-file
function Find-BoilerplateDuplicates {
    param(
        [string]$Folder,
        [string]$Pattern,
        [double]$Threshold = 0.85
    )
    $result = New-Object System.Collections.Generic.List[pscustomobject]
    if (-not (Test-Path $Folder)) { return $result }
    $files = @(Get-ChildItem $Folder -Filter $Pattern -ErrorAction SilentlyContinue)
    if ($files.Count -lt 2) { return $result }

    $sigs = @{}
    foreach ($f in $files) {
        $body = Get-NormalizedBody -FilePath $f.FullName
        $sigs[$f.Name] = Get-ShingleSet -Text $body -N 5
    }

    for ($i = 0; $i -lt $files.Count; $i++) {
        for ($j = $i + 1; $j -lt $files.Count; $j++) {
            $a = $files[$i].Name
            $b = $files[$j].Name
            $sim = Get-JaccardSimilarity -SetA $sigs[$a] -SetB $sigs[$b]
            if ($sim -ge $Threshold) {
                $result.Add([pscustomobject]@{
                    FileA      = $a
                    FileB      = $b
                    Similarity = [math]::Round($sim * 100, 1)
                })
            }
        }
    }
    return $result
}

function Invoke-AuditSubject {
    param([System.IO.DirectoryInfo]$SubjectDir)

    $issues = New-Object System.Collections.Generic.List[string]
    $solutionRows = New-Object System.Collections.Generic.List[pscustomobject]

    $metadataPath = Join-Path $SubjectDir.FullName 'metadata.yaml'
    if (-not (Test-Path $metadataPath)) {
        $issues.Add("Missing metadata.yaml")
    }
    $audioEnabled = Test-AudioEnabled $metadataPath

    # Required folders
    $requiredFolders = @('lectures\pdf', 'lectures\md', 'exercises\pdf', 'exercises\md', 'solutions', 'extensions')
    foreach ($f in $requiredFolders) {
        $p = Join-Path $SubjectDir.FullName $f
        if (-not (Test-Path $p)) {
            $issues.Add("Missing folder: $($f -replace '\\','/')")
        }
    }

    # Audio folders nếu môn declare audio
    if ($audioEnabled) {
        foreach ($f in @('lectures\audio', 'exercises\audio')) {
            $p = Join-Path $SubjectDir.FullName $f
            if (-not (Test-Path $p)) {
                $issues.Add("media_types declares audio but missing $($f -replace '\\','/')")
            }
        }
    }

    # PDF without MD (lectures + exercises)
    foreach ($area in @('lectures', 'exercises')) {
        $pdfDir = Join-Path $SubjectDir.FullName "$area\pdf"
        $mdDir = Join-Path $SubjectDir.FullName "$area\md"
        if ((Test-Path $pdfDir) -and (Test-Path $mdDir)) {
            $pdfFiles = @(Get-ChildItem $pdfDir -Filter '*.pdf' -ErrorAction SilentlyContinue)
            $mdBaseNames = @(Get-ChildItem $mdDir -Filter '*.md' -ErrorAction SilentlyContinue | ForEach-Object { $_.BaseName })
            foreach ($pdf in $pdfFiles) {
                if ($mdBaseNames -notcontains $pdf.BaseName) {
                    $issues.Add("PDF without MD: $area/pdf/$($pdf.Name)")
                }
            }
        }
    }

    # Solutions → review + extension matching
    $solDir = Join-Path $SubjectDir.FullName 'solutions'
    $extDir = Join-Path $SubjectDir.FullName 'extensions'
    $exMdDir = Join-Path $SubjectDir.FullName 'exercises\md'
    if (Test-Path $solDir) {
        $solutions = @(Get-ChildItem $solDir -Filter '*_solution.md' -ErrorAction SilentlyContinue)
        foreach ($sol in $solutions) {
            $baseSlug = $sol.BaseName -replace '_solution$', ''
            $reviewPath = Join-Path $solDir "${baseSlug}_review.md"
            $extPath = Join-Path $extDir "${baseSlug}_extended.md"
            $hasReview = Test-Path $reviewPath
            $hasExt = Test-Path $extPath

            $status = Get-FrontMatterField -FilePath $sol.FullName -Field 'status'
            if (-not $status) { $status = '?' }

            # Verify exercise_file points to a real file
            $exerciseFile = Get-FrontMatterField -FilePath $sol.FullName -Field 'exercise_file'
            if ($exerciseFile) {
                $exPath = Join-Path $exMdDir $exerciseFile
                if (-not (Test-Path $exPath)) {
                    $issues.Add("Solution '$($sol.Name)' refs missing exercise_file: $exerciseFile")
                }
            }

            $solutionRows.Add([pscustomobject]@{
                Slug = $baseSlug
                Status = $status
                Review = if ($hasReview) { 'YES' } else { 'NO' }
                Extended = if ($hasExt) { 'YES' } else { 'NO' }
            })

            # Flag: draft solution thiếu review/extension
            if ($status -eq 'draft' -and -not $hasReview) {
                $issues.Add("Draft solution without review: $($sol.Name)")
            }
        }

        # Boilerplate detection - cross-file: 2 file trong cùng folder >=85% giống nhau (Jaccard 5-gram)
        $reviewDupes = Find-BoilerplateDuplicates -Folder $solDir -Pattern '*_review.md' -Threshold 0.85
        foreach ($d in $reviewDupes) {
            $issues.Add("BOILERPLATE review (~$($d.Similarity)% similar): '$($d.FileA)' ~ '$($d.FileB)' --possible template copy-paste, verify reviewer independence")
        }
        $solutionDupes = Find-BoilerplateDuplicates -Folder $solDir -Pattern '*_solution.md' -Threshold 0.85
        foreach ($d in $solutionDupes) {
            $issues.Add("BOILERPLATE solution (~$($d.Similarity)% similar): '$($d.FileA)' ~ '$($d.FileB)' --possible boilerplate solver output")
        }

        # Boilerplate detection - intra-file: cùng 1 cụm 10 từ lặp >=5 lần trong cùng file
        # (pattern phổ biến nhất ở solver MCQ: cùng 1 đoạn explain cho mọi câu)
        foreach ($b in (Find-IntraFileBoilerplate -Folder $solDir -Pattern '*_solution.md' -N 10 -MinRepeat 5)) {
            $issues.Add("INTRA-FILE boilerplate in '$($b.File)': $($b.UniquePhrases) phrase(s) repeated, top phrase x$($b.TopPhraseCount): ""$($b.TopPhrase)...""")
        }
        foreach ($b in (Find-IntraFileBoilerplate -Folder $solDir -Pattern '*_review.md' -N 10 -MinRepeat 5)) {
            $issues.Add("INTRA-FILE boilerplate in '$($b.File)': $($b.UniquePhrases) phrase(s) repeated, top phrase x$($b.TopPhraseCount): ""$($b.TopPhrase)...""")
        }
    }

    $counts = [pscustomobject]@{
        LecturesPdf  = @(Get-ChildItem (Join-Path $SubjectDir.FullName 'lectures\pdf') -Filter '*.pdf' -ErrorAction SilentlyContinue).Count
        LecturesMd   = @(Get-ChildItem (Join-Path $SubjectDir.FullName 'lectures\md') -Filter '*.md' -ErrorAction SilentlyContinue).Count
        ExercisesPdf = @(Get-ChildItem (Join-Path $SubjectDir.FullName 'exercises\pdf') -Filter '*.pdf' -ErrorAction SilentlyContinue).Count
        ExercisesMd  = @(Get-ChildItem (Join-Path $SubjectDir.FullName 'exercises\md') -Filter '*.md' -ErrorAction SilentlyContinue).Count
        Solutions    = $solutionRows.Count
    }

    return [pscustomobject]@{
        Name         = $SubjectDir.Name
        AudioEnabled = $audioEnabled
        Issues       = $issues
        SolutionRows = $solutionRows
        Counts       = $counts
    }
}

function Format-SubjectSection {
    param($Audit)
    $sb = New-Object System.Text.StringBuilder
    [void]$sb.AppendLine("## $($Audit.Name)")
    [void]$sb.AppendLine("")
    $audio = if ($Audit.AudioEnabled) { 'yes' } else { 'no' }
    [void]$sb.AppendLine("- Audio enabled: $audio")
    $c = $Audit.Counts
    [void]$sb.AppendLine("- Files: lectures pdf=$($c.LecturesPdf) md=$($c.LecturesMd) | exercises pdf=$($c.ExercisesPdf) md=$($c.ExercisesMd) | solutions=$($c.Solutions)")
    [void]$sb.AppendLine("")
    if ($Audit.Issues.Count -gt 0) {
        [void]$sb.AppendLine("**Issues ($($Audit.Issues.Count)):**")
        [void]$sb.AppendLine("")
        foreach ($i in $Audit.Issues) {
            [void]$sb.AppendLine("- [!] $i")
        }
        [void]$sb.AppendLine("")
    } else {
        [void]$sb.AppendLine("**Issues: none**")
        [void]$sb.AppendLine("")
    }
    if ($Audit.SolutionRows.Count -gt 0) {
        [void]$sb.AppendLine("**Solution pipeline:**")
        [void]$sb.AppendLine("")
        [void]$sb.AppendLine("| Slug | Status | Review | Extended |")
        [void]$sb.AppendLine("|---|---|---|---|")
        foreach ($r in $Audit.SolutionRows) {
            [void]$sb.AppendLine("| $($r.Slug) | $($r.Status) | $($r.Review) | $($r.Extended) |")
        }
        [void]$sb.AppendLine("")
    }
    return $sb.ToString()
}

function Format-StatusMd {
    param($Audit)
    $sb = New-Object System.Text.StringBuilder
    [void]$sb.AppendLine("# STATUS - $($Audit.Name)")
    [void]$sb.AppendLine("")
    [void]$sb.AppendLine("> **Auto-generated by ``scripts/check-project.ps1 -WriteStatus``. DO NOT edit by hand.**")
    [void]$sb.AppendLine("> Last update: $(Get-Date -Format 'yyyy-MM-ddTHH:mm:ssK')")
    [void]$sb.AppendLine("")
    [void]$sb.Append((Format-SubjectSection $Audit))
    return $sb.ToString()
}

# === Environment check (tools/pdf_extract dependencies) ===
function Test-PdfExtractEnv {
    $issues = @()
    $pyExe = $null

    # 1. Prefer user-level install (Python ≥3.10 installed via python.org installer)
    $candidatePaths = @(
        (Join-Path $env:LOCALAPPDATA 'Programs\Python\Python313\python.exe'),
        (Join-Path $env:LOCALAPPDATA 'Programs\Python\Python312\python.exe'),
        (Join-Path $env:LOCALAPPDATA 'Programs\Python\Python311\python.exe'),
        (Join-Path $env:LOCALAPPDATA 'Programs\Python\Python310\python.exe')
    )
    foreach ($p in $candidatePaths) {
        if (Test-Path $p) { $pyExe = $p; break }
    }

    # 2. Fall back to PATH — but skip Microsoft Store stub
    if (-not $pyExe) {
        $cmd = Get-Command python -ErrorAction SilentlyContinue
        if ($cmd -and $cmd.Source -notmatch 'WindowsApps') {
            $pyExe = $cmd.Source
        }
    }

    if (-not $pyExe) {
        $issues += "Python ≥3.10 not found (cần cho tools/pdf_extract). Cài từ https://www.python.org/downloads/windows/"
        return $issues
    }

    $deps = & $pyExe -c "import fitz, pdfplumber" 2>&1
    if ($LASTEXITCODE -ne 0) {
        $issues += "Python deps missing: chạy ``& '$pyExe' -m pip install -r tools/pdf_extract/requirements.txt``"
    }
    return $issues
}

# === Main ===
$envIssues = Test-PdfExtractEnv

$allSubjects = @(Get-ChildItem $SubjectsDir -Directory | Where-Object { $_.Name -ne '_template' })
if ($Subject) {
    $allSubjects = @($allSubjects | Where-Object { $_.Name -eq $Subject })
    if ($allSubjects.Count -eq 0) {
        throw "Subject not found: $Subject"
    }
}

$totalIssues = 0
$report = New-Object System.Text.StringBuilder
[void]$report.AppendLine("# Project Check Report")
[void]$report.AppendLine("")
[void]$report.AppendLine("- Generated: $(Get-Date -Format 'yyyy-MM-ddTHH:mm:ssK')")
[void]$report.AppendLine("- Subjects audited: $($allSubjects.Count)")
[void]$report.AppendLine("")

if ($envIssues.Count -gt 0) {
    [void]$report.AppendLine("## Environment (tools/pdf_extract)")
    foreach ($issue in $envIssues) {
        [void]$report.AppendLine("- WARN: $issue")
    }
    [void]$report.AppendLine("")
    $totalIssues += $envIssues.Count
}

foreach ($subj in $allSubjects) {
    $audit = Invoke-AuditSubject -SubjectDir $subj
    $totalIssues += $audit.Issues.Count
    [void]$report.Append((Format-SubjectSection $audit))

    if ($WriteStatus) {
        $statusPath = Join-Path $subj.FullName 'STATUS.md'
        Set-Content -Path $statusPath -Value (Format-StatusMd $audit) -Encoding UTF8
        Write-Host "Wrote $statusPath" -ForegroundColor Green
    }
}

[void]$report.AppendLine("---")
[void]$report.AppendLine("")
[void]$report.AppendLine("**Total issues across project: $totalIssues**")

Write-Output $report.ToString()

if ($totalIssues -gt 0) { exit 1 } else { exit 0 }
