@echo off
color 0C
echo.
echo ========================================
echo         BACKEND DURDURMA
echo ========================================
echo.

echo 🔍 Aktif Python process'leri:
tasklist | findstr python

echo.
echo ⚠️  Tum Python process'lerini durdurmak istiyor musun? (Y/N)
set /p choice=Secim: 

if /i "%choice%"=="Y" (
    echo.
    echo 🛑 Python process'leri durduruluyor...
    taskkill /f /im python.exe >nul 2>&1
    
    if %errorlevel% == 0 (
        echo ✅ Backend basariyla durduruldu
    ) else (
        echo ❌ Hata: Process durdurulamadi
    )
) else (
    echo ❌ Islem iptal edildi
)

echo.
echo 📊 Guncel durum:
tasklist | findstr python

echo.
pause