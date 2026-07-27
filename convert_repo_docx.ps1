# convert_repo_docx.ps1
# Convert all .docx files to Markdown (pandoc required)
# Run from the root of the cloned repository
#
# Usage:
#   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#   .\convert_repo_docx.ps1

$ErrorActionPreference = "Stop"
$OutDir = "markdown_from_docx"

# Check pandoc
$pandocCmd = Get-Command pandoc -ErrorAction SilentlyContinue
if (-not $pandocCmd) {
    Write-Host "ERROR: pandoc not found in PATH." -ForegroundColor Red
    Write-Host "Install: winget install --id JohnMacFarlane.Pandoc"
    Write-Host "Or download from https://pandoc.org/installing.html"
    exit 1
}

Write-Host "Searching for .docx files..." -ForegroundColor Cyan

$docxFiles = @(Get-ChildItem -Path . -Filter "*.docx" -Recurse -File | Sort-Object FullName)

if ($docxFiles.Count -eq 0) {
    Write-Host "No .docx files found. Run this script from the repository root." -ForegroundColor Yellow
    exit 1
}

Write-Host ("Found {0} files. Starting conversion..." -f $docxFiles.Count) -ForegroundColor Green
Write-Host ""

$success = 0
$failed = 0
$rootPath = (Get-Location).Path

foreach ($file in $docxFiles) {
    $relPath = $file.FullName.Substring($rootPath.Length).TrimStart("\", "/")
    $relDir = Split-Path $relPath -Parent
    $baseName = [System.IO.Path]::GetFileNameWithoutExtension($file.Name)

    if ([string]::IsNullOrEmpty($relDir)) {
        $targetDir = $OutDir
    } else {
        $targetDir = Join-Path $OutDir $relDir
    }

    if (-not (Test-Path $targetDir)) {
        New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
    }

    $outFile = Join-Path $targetDir ($baseName + ".md")
    $mediaDir = Join-Path $targetDir "media"

    Write-Host ("  -> {0}" -f $relPath) -NoNewline

    try {
        $args = @(
            $file.FullName,
            "-t", "markdown",
            "-o", $outFile,
            "--wrap=none",
            "--extract-media=$mediaDir"
        )
        & pandoc @args 2>$null

        if ($LASTEXITCODE -eq 0) {
            Write-Host "  OK" -ForegroundColor Green
            $success++
        } else {
            Write-Host "  [pandoc error]" -ForegroundColor Red
            $failed++
        }
    }
    catch {
        Write-Host ("  [exception: {0}]" -f $_.Exception.Message) -ForegroundColor Red
        $failed++
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Done." -ForegroundColor Green
Write-Host ("Success: {0}" -f $success)
Write-Host ("Failed:  {0}" -f $failed)
Write-Host ("Output folder: {0}\" -f $OutDir)
$mdCount = @(Get-ChildItem -Path $OutDir -Filter "*.md" -Recurse -ErrorAction SilentlyContinue).Count
Write-Host ("Created .md files: {0}" -f $mdCount)
Write-Host "========================================"
