@echo off
echo 🤖 AUTONOMOUS AI BACKEND BAŞLATILIYOR
echo =====================================
echo.

echo 📍 Mevcut process'leri durduruluyor...
taskkill /f /im python.exe 2>nul

echo.
echo 📂 Backend dizinine geçiliyor...
cd backend

echo.
echo 📦 Gerekli paketler kontrol ediliyor...
pip install -q fastapi uvicorn motor pymongo python-dotenv aiohttp beautifulsoup4 numpy

echo.
echo 🚀 Autonomous AI Backend başlatılıyor...
echo 📍 Server: http://localhost:8003
echo 🤖 AI Status: http://localhost:8003/api/autonomous-ai/status
echo 💬 AI Chat: http://localhost:8003/api/autonomous-ai/chat
echo 📚 Docs: http://localhost:8003/docs
echo.

echo ✅ Backend başlatıldı - AI test etmeye hazır!
echo 💡 Test için: AI_DURUM_KONTROL.py çalıştırın
echo.

python real_data_backend.py

pause