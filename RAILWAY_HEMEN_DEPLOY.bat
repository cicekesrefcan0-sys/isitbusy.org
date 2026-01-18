@echo off
echo ========================================
echo 🚂 RAILWAY DEPLOYMENT - HEMEN BAŞLA!
echo ========================================
echo.
echo ✅ GITHUB REPOSITORY HAZIR:
echo https://github.com/cicekesrefcan0-sys/esref1-main.git
echo.
echo 📋 HAZIR BİLGİLER:
echo MongoDB: mongodb+srv://cicekesrefcan0_db_user:PASSWORD@cluster0.e6qgkhr.mongodb.net/isitbusy?appName=Cluster0
echo Google Places API: AIzaSyDRoQx4vJlTEioqyO7oQYdjSIJUeCb3Drs
echo Gemini AI API: AIzaSyAxFCNANlrUWD5VspWGWLM6i4VB4H7exoE
echo.
echo 🚂 RAILWAY DEPLOYMENT ADIM ADIM:
echo.
echo 1. Railway.app açılacak
echo 2. "Login with GitHub" tıkla (cicekesrefcan0@gmail.com)
echo 3. "New Project" → "Deploy from GitHub repo"
echo 4. "cicekesrefcan0-sys/esref1-main" repository seç
echo 5. "Deploy Now" tıkla
echo.
pause
echo.
echo 🌐 Railway.app açılıyor...
start https://railway.app
echo.
echo ⚙️ DEPLOYMENT SONRASI AYARLAR:
echo.
echo 📁 ROOT DIRECTORY:
echo Settings → Root Directory → "backend" yaz
echo.
echo 🔑 ENVIRONMENT VARIABLES (KOPYALA):
echo.
echo MONGO_URL=mongodb+srv://cicekesrefcan0_db_user:GERÇEK_ŞİFRE@cluster0.e6qgkhr.mongodb.net/isitbusy?appName=Cluster0
echo GOOGLE_PLACES_API_KEY=AIzaSyDRoQx4vJlTEioqyO7oQYdjSIJUeCb3Drs
echo GEMINI_API_KEY=AIzaSyAxFCNANlrUWD5VspWGWLM6i4VB4H7exoE
echo JWT_SECRET=isitbusy_super_secret_jwt_key_2024_production_ready_32_chars
echo CORS_ORIGINS=https://isitbusy.org,https://www.isitbusy.org
echo PORT=8000
echo ENVIRONMENT=production
echo.
echo 🌐 CUSTOM DOMAIN:
echo Settings → Domains → "api.isitbusy.org" ekle
echo.
echo ⏳ Deployment tamamlandıktan sonra test et:
echo https://[railway-url]/health
echo https://api.isitbusy.org/health
echo.
echo 🎯 BEKLENEN SONUÇ:
echo {"status": "healthy", "timestamp": "..."}
echo.
echo 🚀 HEMEN BAŞLA!
pause