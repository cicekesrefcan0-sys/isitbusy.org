@echo off
color 0A
echo.
echo ========================================
echo      PM2 ile Hizli Baslatma
echo ========================================
echo.

REM Logs klasoru olustur
if not exist "logs" mkdir logs

echo 🔍 PM2 kurulu mu kontrol ediliyor...
pm2 --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ PM2 kurulu degil!
    echo.
    echo PM2 kurmak icin:
    echo 1. Node.js kur: https://nodejs.org/
    echo 2. npm install -g pm2
    echo.
    pause
    exit /b 1
)

echo ✅ PM2 kurulu
echo.

echo 🚀 Backend ve Frontend baslatiliyor...
pm2 start ecosystem.config.js

echo.
echo 📊 Sistem durumu:
pm2 status

echo.
echo 📝 Logları izlemek icin:
echo   pm2 logs
echo.
echo 🔄 Restart icin:
echo   pm2 restart all
echo.
echo 🛑 Durdurmak icin:
echo   pm2 stop all
echo.

echo ✅ Sistem hazir!
echo 🌐 Frontend: http://localhost:3000
echo 🔧 Backend: http://localhost:8003
echo.

pause