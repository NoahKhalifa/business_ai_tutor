<#
.SYNOPSIS
  PowerShell wrapper for tools/pdf_extract — finds Python automatically.

.DESCRIPTION
  Locates a working Python interpreter (skipping the Microsoft Store stub),
  forces UTF-8 console, and forwards args to `python -m tools.pdf_extract`.

.PARAMETER InputPath
  PDF file or folder of PDFs (passed through to the CLI). Alias -i.

.PARAMETER Output
  Output directory. Alias -o.

.PARAMETER Components
  Comma-separated list: text,tables,images,math.

.PARAMETER Force
  Bypass cache.

.PARAMETER NoConfusables
  Skip Vietnamese OCR confusable flagging.

.PARAMETER Quiet
  Suppress progress.

.EXAMPLE
  pwsh scripts/pdf-extract.ps1 "input.pdf"
  pwsh scripts/pdf-extract.ps1 "subjects/X/lectures/pdf/" -Output "subjects/X/lectures/md/"
  pwsh scripts/pdf-extract.ps1 "input.pdf" -o "out/" -Force -Components text,tables
#>
[CmdletBinding()]
param(
    [Parameter(Position = 0, Mandatory = $true)]
    [Alias('i')]
    [string]$InputPath,

    [Alias('o')]
    [string]$Output,

    [string]$Components,

    [switch]$Force,

    [switch]$NoConfusables,

    [switch]$Quiet
)

$ErrorActionPreference = 'Stop'

function Find-Python {
    $candidatePaths = @(
        (Join-Path $env:LOCALAPPDATA 'Programs\Python\Python313\python.exe'),
        (Join-Path $env:LOCALAPPDATA 'Programs\Python\Python312\python.exe'),
        (Join-Path $env:LOCALAPPDATA 'Programs\Python\Python311\python.exe'),
        (Join-Path $env:LOCALAPPDATA 'Programs\Python\Python310\python.exe')
    )
    foreach ($p in $candidatePaths) {
        if (Test-Path $p) { return $p }
    }
    $cmd = Get-Command python -ErrorAction SilentlyContinue
    if ($cmd -and $cmd.Source -notmatch 'WindowsApps') {
        return $cmd.Source
    }
    throw "Python >=3.10 not found. Cài từ https://www.python.org/downloads/windows/"
}

$python = Find-Python
$projectRoot = Split-Path -Parent $PSScriptRoot
$env:PYTHONIOENCODING = 'utf-8'

$cliArgs = @($InputPath)
if ($Output)          { $cliArgs += @('-o', $Output) }
if ($Components)      { $cliArgs += @('--components', $Components) }
if ($Force)           { $cliArgs += '--force' }
if ($NoConfusables)   { $cliArgs += '--no-confusables' }
if ($Quiet)           { $cliArgs += '--quiet' }

Push-Location $projectRoot
try {
    & $python -m tools.pdf_extract @cliArgs
    exit $LASTEXITCODE
} finally {
    Pop-Location
}
