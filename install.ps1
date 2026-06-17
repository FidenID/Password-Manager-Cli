# Password Manager CLI - Windows Installer

Write-Host "=== Password Manager CLI Installer (Windows) ===" -ForegroundColor Cyan
Write-Host ""

# Get install directory
$INSTALL_DIR = $PSScriptRoot
Write-Host "📁 Install directory: $INSTALL_DIR" -ForegroundColor Green

# Check Python
try {
    $pythonVersion = python --version 2>&1
    Write-Host "🐍 Python detected: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python tidak terdeteksi. Install Python terlebih dahulu!" -ForegroundColor Red
    Write-Host "   Download di: https://www.python.org/downloads/" -ForegroundColor Yellow
    exit 1
}

Write-Host ""
Write-Host "📝 Membuat batch files..." -ForegroundColor Yellow

# Create pm.bat
$pmBatContent = @"
@echo off
python "$INSTALL_DIR\pm_interactive.py" %*
"@
$pmBatPath = "$INSTALL_DIR\pm.bat"
Set-Content -Path $pmBatPath -Value $pmBatContent

# Create pmcli.bat
$pmcliBatContent = @"
@echo off
python "$INSTALL_DIR\pm.py" %*
"@
$pmcliBatPath = "$INSTALL_DIR\pmcli.bat"
Set-Content -Path $pmcliBatPath -Value $pmcliBatContent

Write-Host "✅ Batch files dibuat!" -ForegroundColor Green
Write-Host ""

# Add to PATH
$currentPath = [Environment]::GetEnvironmentVariable("Path", "User")
if ($currentPath -notlike "*$INSTALL_DIR*") {
    Write-Host "📌 Menambahkan ke PATH..." -ForegroundColor Yellow
    [Environment]::SetEnvironmentVariable("Path", "$currentPath;$INSTALL_DIR", "User")
    Write-Host "✅ PATH berhasil diupdate!" -ForegroundColor Green
    Write-Host ""
    Write-Host "⚠️  PENTING: Restart terminal/PowerShell agar PATH aktif!" -ForegroundColor Yellow
} else {
    Write-Host "✅ Folder sudah ada di PATH!" -ForegroundColor Green
}

Write-Host ""
Write-Host "🎉 Instalasi berhasil!" -ForegroundColor Cyan
Write-Host ""
Write-Host "Cara menggunakan:" -ForegroundColor White
Write-Host "  1. Restart terminal/PowerShell" -ForegroundColor White
Write-Host "  2. Jalankan password manager:" -ForegroundColor White
Write-Host "     pm              # Mode interaktif" -ForegroundColor Yellow
Write-Host "     pmcli list      # Mode CLI" -ForegroundColor Yellow
Write-Host ""
Write-Host "Selamat menggunakan! 🔐" -ForegroundColor Cyan
