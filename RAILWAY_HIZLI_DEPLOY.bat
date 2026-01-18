@echo off
echo ========================================
echo    🚂 RAILWAY BACKEND DEPLOYMENT
echo ========================================
echo.

echo ✅ FRONTEND: isitbusy.org (Vercel'de)
echo 🎯 HEDEF: Backend'i Railway'e deploy et
echo 🌐 SONUC: api.isitbusy.org
echo.

echo ========================================
echo    ADIM 1: RAILWAY HESABI AC
echo ========================================
echo.

echo 🚂 1. https://railway.app adresine git
echo 👤 2. "Sign Up" butonuna tikla
echo 🔗 3. "Continue with GitHub" sec
echo ✅ 4. GitHub ile giris yap
echo 💳 5. Kredi karti bilgilerini gir (free tier icin)
echo.

echo HEMEN YAPIN! 3 dakika surer.
pause

echo ========================================
echo    ADIM 2: NEW PROJECT OLUSTUR
echo ========================================
echo.

echo 📁 1. Railway dashboard'da "New Project" tikla
echo 🔗 2. "Deploy from GitHub repo" sec
echo 📂 3. "esref1-main" repository'yi bul ve sec
echo ✅ 4. "Deploy Now" butonuna tikla
echo.

echo ⚙️ PROJECT AYARLARI:
echo 📁 Root Directory: "backend" (otomatik algılar)
echo 🐍 Runtime: Python (otomatik algılar)
echo 📦 Build Command: pip install -r requirements.txt
echo 🚀 Start Command: python server.py
echo.

echo HEMEN YAPIN! 2 dakika surer.
pause

echo ========================================
echo    ADIM 3: ENVIRONMENT VARIABLES
echo ========================================
echo.

echo 🔑 GEREKLI ENV VARIABLES:
echo.

echo 1. Railway dashboard'da "Variables" sekmesine git
echo 2. Asagidaki degiskenleri tek tek ekle:
echo.

echo ➕ MONGO_URL
echo Value: mongodb+srv://username:password@cluster.mongodb.net/isitbusy
echo (MongoDB Atlas'tan alacaksiniz)
echo.

echo ➕ GOOGLE_PLACES_API_KEY  
echo Value: your_google_places_api_key
echo (Google Cloud Console'dan alacaksiniz)
echo.

echo ➕ GEMINI_API_KEY
echo Value: your_gemini_api_key
echo (Google AI Studio'dan alacaksiniz)
echo.

echo ➕ JWT_SECRET
echo Value: your_super_secret_jwt_key_here_32_chars_minimum
echo.

echo ➕ CORS_ORIGINS
echo Value: https://isitbusy.org,https://www.isitbusy.org
echo.

echo ➕ PORT
echo Value: 8000
echo.

echo ➕ ENVIRONMENT
echo Value: production
echo.

echo HEMEN YAPIN! 5 dakika surer.
pause

echo ========================================
echo    ADIM 4: MONGODB ATLAS SETUP
echo ========================================
echo.

echo 🍃 MONGODB ATLAS KURULUM:
echo.

echo 1. https://cloud.mongodb.com adresine git
echo 2. "Sign Up" ^> Google ile giris yap
echo 3. "Build a Database" tikla
echo 4. "FREE" tier sec (M0 Sandbox)
echo 5. Cloud Provider: AWS
echo 6. Region: US East (N. Virginia)
echo 7. Cluster Name: "isitbusy-cluster"
echo 8. "Create Cluster" tikla
echo.

echo 👤 DATABASE USER OLUSTUR:
echo 9. "Database Access" ^> "Add New Database User"
echo 10. Username: isitbusy
echo 11. Password: [guclu sifre olustur - kaydet!]
echo 12. Database User Privileges: "Read and write to any database"
echo 13. "Add User" tikla
echo.

echo 🌐 NETWORK ACCESS:
echo 14. "Network Access" ^> "Add IP Address"
echo 15. "Allow Access from Anywhere" sec (0.0.0.0/0)
echo 16. "Confirm" tikla
echo.

echo 🔗 CONNECTION STRING AL:
echo 17. "Clusters" ^> "Connect" tikla
echo 18. "Connect your application" sec
echo 19. Driver: Python, Version: 3.6 or later
echo 20. Connection string'i kopyala:
echo     mongodb+srv://isitbusy:^<password^>@isitbusy-cluster.xxxxx.mongodb.net/isitbusy
echo 21. ^<password^> yerine gercek sifreyi yaz
echo.

echo HEMEN YAPIN! 15 dakika surer.
pause

echo ========================================
echo    ADIM 5: GOOGLE APIS SETUP
echo ========================================
echo.

echo 🔑 GOOGLE PLACES API:
echo.

echo 1. https://console.cloud.google.com adresine git
echo 2. "New Project" olustur: "isitbusy-org"
echo 3. "APIs ^& Services" ^> "Library"
echo 4. "Places API" ara ve "Enable" et
echo 5. "Credentials" ^> "Create Credentials" ^> "API Key"
echo 6. API Key'i kopyala ve kaydet
echo 7. "Restrict Key" tikla
echo 8. "HTTP referrers" sec
echo 9. Website restrictions: *.isitbusy.org/*
echo 10. "Save" tikla
echo.

echo 🤖 GEMINI AI API:
echo.

echo 1. https://makersuite.google.com/app/apikey adresine git
echo 2. "Create API Key" tikla
echo 3. API Key'i kopyala ve kaydet
echo.

echo HEMEN YAPIN! 15 dakika surer.
pause

echo ========================================
echo    ADIM 6: RAILWAY'E ENV VARS EKLE
echo ========================================
echo.

echo 🔄 RAILWAY'E GERI DON:
echo.

echo 1. Railway dashboard'da projenizi ac
echo 2. "Variables" sekmesine git
echo 3. Asagidaki degerleri gir:
echo.

echo MONGO_URL = [MongoDB connection string]
echo GOOGLE_PLACES_API_KEY = [Google Places API key]
echo GEMINI_API_KEY = [Gemini API key]
echo JWT_SECRET = your_super_secret_jwt_key_here_32_chars_minimum
echo CORS_ORIGINS = https://isitbusy.org,https://www.isitbusy.org
echo PORT = 8000
echo ENVIRONMENT = production
echo.

echo 4. "Save" tikla
echo 5. Otomatik redeploy baslar
echo.

echo HEMEN YAPIN! 5 dakika surer.
pause

echo ========================================
echo    ADIM 7: DEPLOYMENT BEKLE
echo ========================================
echo.

echo ⏰ DEPLOYMENT PROCESS:
echo.

echo 1. Railway "Deployments" sekmesine git
echo 2. Build logs'u izle
echo 3. "Building..." ^> "Deploying..." ^> "Success" bekle
echo 4. Deployment URL'ini kopyala
echo    Ornek: https://backend-production-xxxx.up.railway.app
echo.

echo 🧪 API TEST:
echo 5. Browser'da URL/health adresine git
echo    Ornek: https://backend-production-xxxx.up.railway.app/health
echo 6. {"status": "healthy"} donuyorsa BASARILI!
echo.

echo HEMEN YAPIN! 10 dakika surer.
pause

echo ========================================
echo    ADIM 8: CUSTOM DOMAIN BAGLA
echo ========================================
echo.

echo 🔗 API.ISITBUSY.ORG BAGLAMA:
echo.

echo 1. Railway dashboard'da "Settings" tikla
echo 2. "Domains" bolumunu bul
echo 3. "Custom Domain" tikla
echo 4. "api.isitbusy.org" gir
echo 5. "Add Domain" tikla
echo 6. CNAME record'u kopyala
echo.

echo 🌐 DOMAIN PROVIDER'DA DNS:
echo.

echo 7. Domain provider'iniza git (Porkbun/Namecheap/etc)
echo 8. DNS Management'a git
echo 9. CNAME record ekle:
echo    Name: api
echo    Type: CNAME
echo    Value: [Railway'den kopyaladiginiz CNAME]
echo    TTL: 300
echo 10. "Save" tikla
echo.

echo ⏰ 5-10 dakika bekle (DNS propagation)
echo.

echo HEMEN YAPIN! 10 dakika surer.
pause

echo ========================================
echo    ADIM 9: FULL STACK TEST
echo ========================================
echo.

echo 🧪 BACKEND API TEST:
echo.

echo 1. https://api.isitbusy.org/health
echo   Sonuc: {"status": "healthy"}
echo.

echo 2. https://api.isitbusy.org/api/venues
echo   Sonuc: Venue listesi JSON
echo.

echo 3. https://api.isitbusy.org/api/venues/search?query=denver
echo   Sonuc: Denver venues JSON
echo.

echo 🌐 FRONTEND-BACKEND ENTEGRASYON:
echo.

echo 4. https://isitbusy.org adresine git
echo 5. "Find Venues" butonuna tikla
echo 6. Venue'lar yukleniyor mu kontrol et
echo 7. Bir venue'ya tikla
echo 8. Venue detay sayfasi aciliyor mu kontrol et
echo 9. AI chat widget calisyor mu test et
echo.

echo ✅ HEPSI CALISIYORSA: FULL STACK LIVE!
echo.

echo HEMEN TEST EDIN! 10 dakika surer.
pause

echo ========================================
echo    DEPLOYMENT TAMAMLANDI!
echo ========================================
echo.

echo 🎉 TEBRIKLER! FULL STACK LIVE!
echo.

echo 🌐 FRONTEND: https://isitbusy.org
echo 🌐 BACKEND: https://api.isitbusy.org
echo 📱 BETA: https://isitbusy.org/beta
echo 📊 RAILWAY DASHBOARD: https://railway.app/dashboard
echo.

echo ✅ BASARILI DEPLOYMENT CHECKLIST:
echo [ ] Railway hesabi acildi
echo [ ] Backend basariyla deploy edildi
echo [ ] MongoDB Atlas kuruldu ve baglandi
echo [ ] Google APIs kuruldu ve baglandi
echo [ ] Environment variables eklendi
echo [ ] api.isitbusy.org domain baglandi
echo [ ] SSL sertifikasi aktif
echo [ ] Backend API calisyor
echo [ ] Frontend-Backend entegrasyonu calisyor
echo.

echo 📊 PERFORMANCE METRIKLERI:
echo 🚀 API Response Time: ^<500ms
echo 🎯 Database Query Time: ^<200ms
echo ⚡ Uptime: ^>99%%
echo 📱 CORS properly configured
echo.

echo ========================================
echo    SONRAKI ADIMLAR
echo ========================================
echo.

echo 🔄 SIMDI YAPILACAKLAR:
echo.

echo 1️⃣ SOSYAL MEDYA HESAPLARI AC (30 dk)
echo 2️⃣ BETA USER RECRUITMENT BASLA (60 dk)
echo 3️⃣ ANALYTICS SETUP (Google Analytics) (20 dk)
echo 4️⃣ PERFORMANCE MONITORING (15 dk)
echo 5️⃣ LOCAL PR VE MARKETING (120 dk)
echo.

echo 🎯 BUGUN SONU HEDEFI:
echo ✅ Full-stack app live
echo ✅ 4 sosyal medya hesabi aktif
echo ✅ 50+ beta user kayit
echo ✅ Local PR baslamis
echo.

echo ========================================
echo    SORUN GIDERME
echo ========================================
echo.

echo 🔧 BACKEND DEPLOY HATASI:
echo - Requirements.txt kontrol et
echo - Python version kontrol et (3.8+)
echo - Railway logs'u incele
echo - Environment variables kontrol et
echo.

echo 🔧 DATABASE BAGLANTI HATASI:
echo - MongoDB connection string kontrol et
echo - Database user permissions kontrol et
echo - Network access (0.0.0.0/0) kontrol et
echo - Password'de ozel karakter var mi kontrol et
echo.

echo 🔧 API CALLS FAIL:
echo - CORS origins kontrol et
echo - API keys gecerli mi kontrol et
echo - Rate limits asiliyor mu kontrol et
echo.

echo ========================================
echo    BASARI METRIKLERI
echo ========================================
echo.

echo 📊 BUGUN SONU HEDEFLERI:
echo ✅ https://isitbusy.org live ve calisyor
echo ✅ https://api.isitbusy.org live ve calisyor
echo ✅ Full-stack entegrasyon calisyor
echo ✅ 4,355+ venues gorunuyor
echo ✅ AI chat widget calisyor
echo ✅ Real-time data akiyor
echo.

echo 📊 HAFTA SONU HEDEFLERI:
echo ✅ 500+ API calls/day
echo ✅ 200+ active users
echo ✅ 100+ venue detail views
echo ✅ 50+ AI chat interactions
echo ✅ 99%%+ uptime
echo.

echo 🎯 BACKEND DEPLOYMENT BASARILI!
echo 💪 MARKETING VE PR'A GECIN!
echo 🚀 LAUNCH NEREDEYSE TAMAMLANDI!
echo.

echo HAZIR MISINIZ? SOSYAL MEDYA ZAMANI! 📱
pause