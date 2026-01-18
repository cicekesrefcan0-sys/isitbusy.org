@echo off
echo ========================================
echo EVENTBRITE COLORADO INTEGRATION
echo ========================================
echo.
echo Bu script Eventbrite Colorado entegrasyonunu test eder
echo.

echo 1. Backend servisi baslatiliyor...
echo.
start "Backend Server" cmd /k "cd backend && python server.py"

timeout /t 5

echo 2. Frontend servisi baslatiliyor...
echo.
start "Frontend Server" cmd /k "cd frontend && npm start"

timeout /t 3

echo 3. Test scripti calistiriliyor...
echo.
start "Test Script" cmd /k "python TEST_EVENTBRITE_COLORADO.py"

echo.
echo ========================================
echo SERVISLER BASLATILDI!
echo ========================================
echo.
echo Backend: http://localhost:8000
echo Frontend: http://localhost:3000
echo.
echo API Endpoints:
echo - GET /api/eventbrite/cities
echo - GET /api/eventbrite/events
echo - GET /api/eventbrite/after-parties
echo - POST /api/eventbrite/scrape
echo.
echo Eventbrite API Key eklemek icin:
echo backend/.env dosyasina EVENTBRITE_API_KEY=your_key_here ekleyin
echo.
pause