@echo off
echo 🚨 AI SORUNU - HIZLI ÇÖZÜM
echo ============================
echo.

echo 📍 Mevcut Python process'lerini durduruluyor...
taskkill /f /im python.exe 2>nul

echo.
echo 📂 Backend dizinine geçiliyor...
cd esref1-main\backend

echo.
echo 📦 Gerekli paketleri kontrol ediliyor...
pip install -q fastapi uvicorn motor pymongo python-dotenv aiohttp numpy

echo.
echo 🚀 Backend başlatılıyor...
echo 📍 Server: http://localhost:8003
echo 🤖 AI Status: http://localhost:8003/api/autonomous-ai/status
echo.

echo ✅ Backend başlatıldı!
echo 💡 30 saniye bekleyin, sonra frontend'de brain ikonu (🧠) ile test edin
echo.

start python real_data_backend.py

echo.
echo 🔍 Test için ayrı bir terminal'de şunu çalıştırın:
echo python HEMEN_TEST_ET.py
echo.

pause