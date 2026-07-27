@echo off
chcp 65001 >nul
setlocal

echo.
echo ========================================
echo  DOCX to Markdown converter
echo ========================================
echo.

if not exist "README.md" (
    echo [ERROR] Run this bat from the repository root folder.
    echo.
    pause
    exit /b 1
)

powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0convert_repo_docx.ps1"

echo.
pause
