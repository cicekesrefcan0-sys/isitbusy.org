@echo off
echo ========================================
echo  Starting Real Data Backend with Reviews
echo ========================================
echo.

echo 🚀 Starting Real Data Backend with Google Places Reviews Integration...
echo 📊 Features: Real venues, Real reviews, 24h auto-updates
echo 🌐 Server will be available at: http://localhost:8003
echo 📚 API Documentation: http://localhost:8003/docs
echo.

cd backend

echo ⚙️ Checking Python environment...
python --version
echo.

echo 📦 Installing/updating dependencies...
pip install -r requirements.txt
echo.

echo 🔑 Checking environment variables...
if not exist .env (
    echo ⚠️ Warning: .env file not found
    echo Creating basic .env file...
    echo GOOGLE_PLACES_API_KEY=your_api_key_here > .env
    echo MONGODB_URI=mongodb://localhost:27017/isitbusy >> .env
    echo Please update .env with your actual API keys
    echo.
)

echo 🗄️ Starting MongoDB (if not running)...
start /min mongod --dbpath data

echo ⏳ Waiting for MongoDB to start...
timeout /t 3 /nobreak > nul

echo 🚀 Starting Real Data Backend with Reviews...
echo.
echo ============================================
echo  Backend Features:
echo  ✅ Real venue data from MongoDB
echo  ✅ Google Places Reviews integration  
echo  ✅ 24-hour automatic data updates
echo  ✅ Real-time review fetching
echo  ✅ Admin endpoints for monitoring
echo ============================================
echo.

python real_data_backend.py

echo.
echo Backend stopped. Press any key to exit...
pause > nul