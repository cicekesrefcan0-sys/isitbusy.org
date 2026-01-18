@echo off
echo 🤖 AUTONOMOUS AI SYSTEM - STARTUP TEST
echo =====================================
echo.

echo 📍 Starting backend server with Autonomous AI...
cd backend
echo 🔧 Installing dependencies...
pip install -r requirements.txt

echo.
echo 🚀 Starting Real Data Backend with Autonomous AI...
echo 📍 Server will be available at: http://localhost:8003
echo 📚 API Documentation: http://localhost:8003/docs
echo 🤖 Autonomous AI endpoints: http://localhost:8003/api/autonomous-ai/
echo.

python real_data_backend.py

pause