@echo off
echo Backend'i background'da baslatiliyor...

cd /d "%~dp0backend"

REM Backend'i background process olarak baslat
start /B python real_data_backend.py > backend.log 2>&1

echo.
echo ✅ Backend background'da baslatildi!
echo 📊 Port: 8003
echo 📝 Log dosyasi: backend\backend.log
echo.
echo Backend durumunu kontrol etmek icin:
echo   tasklist | findstr python
echo.
echo Backend'i durdurmak icin:
echo   taskkill /f /im python.exe
echo.
pause