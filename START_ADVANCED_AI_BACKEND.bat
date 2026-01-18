@echo off
echo ========================================
echo  Advanced AI Backend with Web Search
echo ========================================
echo.

echo 🤖 Starting Advanced AI Backend with Web Search Integration...
echo 🔍 Features: Real-time web search, Intelligent chat, AI predictions
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
    echo GEMINI_API_KEY=your_gemini_api_key_here >> .env
    echo GOOGLE_SEARCH_API_KEY=your_google_search_api_key_here >> .env
    echo GOOGLE_SEARCH_ENGINE_ID=your_search_engine_id_here >> .env
    echo SERP_API_KEY=your_serp_api_key_here >> .env
    echo Please update .env with your actual API keys
    echo.
)

echo 🗄️ Starting MongoDB (if not running)...
start /min mongod --dbpath data

echo ⏳ Waiting for MongoDB to start...
timeout /t 3 /nobreak > nul

echo 🤖 Starting Advanced AI Backend...
echo.
echo ============================================
echo  AI Features:
echo  ✅ Real venue data from MongoDB
echo  ✅ Google Places Reviews integration  
echo  ✅ 24-hour automatic data updates
echo  ✅ Advanced AI chat with web search
echo  ✅ Real-time information retrieval
echo  ✅ Intelligent question answering
echo  ✅ Busyness predictions with AI
echo  ✅ Context-aware responses
echo ============================================
echo.
echo 🔍 Web Search APIs supported:
echo   • Google Custom Search (premium)
echo   • SerpAPI (premium)  
echo   • DuckDuckGo (free fallback)
echo.
echo 🤖 AI Models supported:
echo   • Google Gemini 2.5 Flash (free tier)
echo   • Fallback algorithm (always available)
echo.

python real_data_backend.py

echo.
echo Backend stopped. Press any key to exit...
pause > nul