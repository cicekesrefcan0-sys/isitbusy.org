@echo off
color 0B
echo.
echo ========================================
echo        SISTEM DURUMU KONTROL
echo ========================================
echo.

echo 🔍 Backend Process Kontrol:
tasklist | findstr python
if %errorlevel% == 0 (
    echo ✅ Backend process bulundu
) else (
    echo ❌ Backend process bulunamadi
)

echo.
echo 🌐 Port 8003 Kontrol:
netstat -an | findstr :8003
if %errorlevel% == 0 (
    echo ✅ Port 8003 aktif
) else (
    echo ❌ Port 8003 kapali
)

echo.
echo 📊 Backend Health Check:
curl -s http://localhost:8003/health > nul 2>&1
if %errorlevel% == 0 (
    echo ✅ Backend saglikli
) else (
    echo ❌ Backend yanit vermiyor
)

echo.
echo 📝 Son 10 log satiri:
if exist "backend\backend.log" (
    powershell "Get-Content 'backend\backend.log' -Tail 10"
) else (
    echo Log dosyasi bulunamadi
)

echo.
pause