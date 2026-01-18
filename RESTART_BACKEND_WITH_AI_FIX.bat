@echo off
echo 🔧 RESTARTING BACKEND WITH AUTONOMOUS AI FIX
echo =============================================
echo.

echo 📍 Stopping any existing backend processes...
taskkill /f /im python.exe 2>nul

echo.
echo 🚀 Starting backend with fixed Autonomous AI...
cd backend

echo 📦 Checking dependencies...
pip install -q numpy sqlite3 2>nul

echo.
echo 🤖 Starting Real Data Backend with Autonomous AI Fix...
echo 📍 Server: http://localhost:8003
echo 🧠 AI Status: http://localhost:8003/api/autonomous-ai/status
echo 💬 AI Chat: http://localhost:8003/api/autonomous-ai/chat
echo.

echo ✅ Red Rocks questions should now work properly!
echo 💡 Test question: "Show me tonight's events at Red Rocks"
echo.

python real_data_backend.py

pause