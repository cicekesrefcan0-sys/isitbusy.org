@echo off
echo 🚀 STARTING REAL DATA MODE
echo ========================
echo.
echo 📍 Backend will run on: http://localhost:8003
echo 📍 Frontend should use: http://localhost:3000
echo.
echo 🔄 Starting real data backend with 1700+ venues...
echo 💡 All venues have working website links!
echo.
cd backend
python real_data_backend.py
pause