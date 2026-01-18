@echo off
echo ========================================
echo 🎯 ISITBUSY.ORG LAUNCH - DEVAM EDİYORUZ
echo ========================================
echo.
echo ✅ TAMAMLANAN ADIMLAR:
echo 1. ✅ Vercel Frontend Deployment
echo 2. ✅ MongoDB Atlas Setup (Cluster0)
echo 3. ✅ Google Places API Key: AIzaSyDRoQx4vJlTEioqyO7oQYdjSIJUeCb3Drs
echo 4. ✅ Gemini AI API Key: AIzaSyAxFCNANlrUWD5VspWGWLM6i4VB4H7exoE
echo.
echo 🔄 ŞU ANDA: RAILWAY BACKEND DEPLOYMENT
echo.
echo 📋 HAZIR BİLGİLER:
echo Domain: isitbusy.org ✅
echo Email: cicekesrefcan0@gmail.com ✅
echo MongoDB: mongodb+srv://cicekesrefcan0_db_user:PASSWORD@cluster0.e6qgkhr.mongodb.net/isitbusy?appName=Cluster0
echo Google Places API: AIzaSyDRoQx4vJlTEioqyO7oQYdjSIJUeCb3Drs ✅
echo Gemini AI API: AIzaSyAxFCNANlrUWD5VspWGWLM6i4VB4H7exoE ✅
echo.
echo ========================================
echo 🚂 RAILWAY BACKEND DEPLOYMENT - HEMEN!
echo ========================================
echo.
echo 📋 ADIM ADIM:
echo 1. Railway.app açılacak
echo 2. GitHub ile giriş yap (cicekesrefcan0@gmail.com)
echo 3. New Project → Deploy from GitHub repo
echo 4. esref1-main repository seç
echo 5. Settings → Root Directory → "backend" yaz
echo 6. Variables sekmesinde environment variables ekle
echo 7. Custom domain "api.isitbusy.org" ekle
echo.
pause
echo.
echo 🚀 Railway.app açılıyor...
start https://railway.app
echo.
echo 📖 Detaylı rehber açılıyor...
start RAILWAY_DEPLOYMENT_HEMEN.md
echo.
echo ⚠️  ENVIRONMENT VARIABLES (KOPYALA):
echo.
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
echo ⏳ Railway deployment tamamlandıktan sonra devam et...
pause
echo.
echo ========================================
echo 🌐 DNS AYARLARI VE FINAL TEST
echo ========================================
echo.
echo 📋 SONRAKI ADIMLAR:
echo 1. Domain provider'da DNS kayıtları ayarla
echo 2. https://isitbusy.org test et
echo 3. https://api.isitbusy.org/health test et
echo 4. Full-stack entegrasyon test et
echo.
echo 🧪 TEST KOMUTLARI:
echo curl https://api.isitbusy.org/health
echo curl https://api.isitbusy.org/api/venues
echo.
echo 🎉 LAUNCH TAMAMLANACAK!
echo.
echo ✅ BAŞARI KRİTERLERİ:
echo - https://isitbusy.org açılıyor ✅/❌
echo - https://api.isitbusy.org/health çalışıyor ✅/❌
echo - Frontend-Backend bağlantısı çalışıyor ✅/❌
echo - AI chat widget çalışıyor ✅/❌
echo.
echo 🚀 DEVAM EDELİM!
pause