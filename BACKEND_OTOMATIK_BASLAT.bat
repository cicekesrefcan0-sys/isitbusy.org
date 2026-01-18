@echo off
title IsItBusy Backend - Otomatik Restart
color 0A
echo.
echo ========================================
echo   IsItBusy Backend - Otomatik Restart
echo ========================================
echo.

cd /d "%~dp0backend"

:restart
echo [%date% %time%] Backend baslatiliyor...
python real_data_backend.py

echo.
echo [%date% %time%] Backend durdu! 5 saniye sonra yeniden baslatiliyor...
echo Kapatmak icin Ctrl+C basin
timeout /t 5 /nobreak >nul
echo.
goto restart