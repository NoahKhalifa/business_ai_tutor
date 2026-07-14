$ErrorActionPreference = 'Stop'

$repoRoot = Split-Path -Parent (Split-Path -Parent $PSScriptRoot)
$checker = Join-Path $repoRoot 'scripts\check-project.ps1'
$subject = (Get-ChildItem (Join-Path $repoRoot 'subjects') -Directory | Where-Object { $_.Name -like 'Kinh t*' } | Select-Object -First 1).Name
$output = & powershell -NoProfile -ExecutionPolicy Bypass -File $checker -Subject $subject 2>&1 | Out-String

if ($output -notmatch 'exercises pdf=0 docx=7 md=7') {
    throw "Expected DOCX exercise sources to be counted. Actual output:`n$output"
}

if ($output -match 'DOCX without MD') {
    throw "Expected the seven matching exercise MD files to satisfy their DOCX sources. Actual output:`n$output"
}

Write-Output 'PASS: check-project counts and matches DOCX exercise sources.'
