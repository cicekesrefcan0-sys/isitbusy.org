@echo off
REM IsItBusy - Windows Startup Script
REM Bu dosyayi Windows Startup folder'ina kopyala

title IsItBusy - Startup Script
color 0A

echo.
echo ========================================
echo      IsItBusy - Otomatik Baslatma
echo ========================================
echo.

REM Proje dizinine git
cd /d "C:\Users\scice\Downloads\esref1-main\esref1-main"

echo 🔍 PM2 durumu kontrol ediliyor...
pm2 status >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ PM2 daemon baslatiliyor...
    pm2 ping >nul 2>&1
)

echo 🚀 Backend baslatiliyor...
pm2 start ecosystem.config.js >nul 2>&1

echo ⏳ 5 saniye bekleniyor...
timeout /t 5 /nobreak >nul

echo 📊 Sistem durumu:
pm2 status

echo.
echo ✅ IsItBusy backend baslatildi!
echo 🌐 Backend: http://localhost:8003
echo 📝 Loglar: pm2 logs
echo.

REM 10 saniye sonra pencereyi kapat
timeout /t 10