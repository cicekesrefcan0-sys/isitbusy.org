@echo off
echo ========================================
echo 🚂 RAILWAY BACKEND DEPLOYMENT BAŞLIYOR
echo ========================================
echo.
echo ✅ HAZIR OLAN BİLGİLER:
echo MongoDB: mongodb+srv://cicekesrefcan0_db_user:PASSWORD@cluster0.e6qgkhr.mongodb.net/isitbusy?appName=Cluster0
echo Google Places API: AIzaSyDRoQx4vJlTEioqyO7oQYdjSIJUeCb3Drs
echo Gemini AI API: AIzaSyAxFCNANlrUWD5VspWGWLM6i4VB4H7exoE
echo.
echo 🎯 ADIMLAR:
echo 1. Railway.app açılacak
echo 2. GitHub ile giriş yap (cicekesrefcan0@gmail.com)
echo 3. New Project → Deploy from GitHub repo
echo 4. esref1-main repository seç
echo 5. Settings → Root Directory → "backend" yaz
echo 6. Variables sekmesinde environment variables ekle
echo.
echo 📋 ENVIRONMENT VARIABLES (KOPYALA):
echo MONGO_URL=mongodb+srv://cicekesrefcan0_db_user:GERÇEK_ŞİFRE@cluster0.e6qgkhr.mongodb.net/isitbusy?appName=Cluster0
echo GOOGLE_PLACES_API_KEY=AIzaSyDRoQx4vJlTEioqyO7oQYdjSIJUeCb3Drs
echo GEMINI_API_KEY=AIzaSyAxFCNANlrUWD5VspWGWLM6i4VB4H7exoE
echo JWT_SECRET=isitbusy_super_secret_jwt_key_2024_production_ready_32_chars
echo CORS_ORIGINS=https://isitbusy.org,https://www.isitbusy.org
echo PORT=8000
echo ENVIRONMENT=production
echo.
echo ⚠️  ÖNEMLİ: GERÇEK_ŞİFRE yerine MongoDB Atlas şifreni yaz!
echo.
pause
echo.
echo 🚀 Railway.app açılıyor...
start https://railway.app
echo.
echo 📖 Detaylı rehber açılıyor...
start RAILWAY_DEPLOYMENT_HEMEN.md
echo.
echo ✅ Railway deployment başlatıldı!
echo ⏳ Deployment tamamlandıktan sonra api.isitbusy.org domain ekle
echo 🧪 Test: https://api.isitbusy.org/health
echo.
pause