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

# === Main ===
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
