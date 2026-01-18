@echo off
echo ========================================
echo    IS IT BUSY? LAUNCH HAZIRLIK
echo ========================================
echo.

echo [DURUM] Sistem %%100 hazir! Launch basliyoruz! 🚀
echo.

echo ========================================
echo    ADIM 1: DOMAIN VE HOSTING SECIMI
echo ========================================
echo.

echo 🌐 DOMAIN ONERILERI:
echo ✅ isitbusy.com (ideal)
echo ✅ isitbusydenver.com (alternatif)
echo ✅ busydenver.com (kisa)
echo ✅ denvernightlife.app (aciklayici)
echo.

echo 💰 DOMAIN MALIYETI: $10-15/yil
echo 🛒 SATIN ALMA LINKLERI:
echo   - Namecheap: https://namecheap.com
echo   - Cloudflare: https://cloudflare.com
echo   - GoDaddy: https://godaddy.com
echo.
pause

echo ========================================
echo    ADIM 2: HOSTING PLATFORMLARI
echo ========================================
echo.

echo 🎯 FRONTEND HOSTING (UCRETSIZ):
echo ✅ Vercel - https://vercel.com
echo   - Ucretsiz tier: 100GB bandwidth
echo   - Otomatik SSL
echo   - Global CDN
echo   - Git integration
echo.

echo 🎯 BACKEND HOSTING ($5-20/ay):
echo ✅ Railway - https://railway.app
echo   - $5/ay starter plan
echo   - Otomatik scaling
echo   - Database hosting
echo   - Easy deployment
echo.

echo 🎯 DATABASE HOSTING (UCRETSIZ):
echo ✅ MongoDB Atlas - https://cloud.mongodb.com
echo   - 512MB ucretsiz tier
echo   - Mevcut verileriniz: 4,355 venue
echo   - Otomatik backup
echo.
pause

echo ========================================
echo    ADIM 3: DEPLOYMENT DOSYALARI HAZIRLA
echo ========================================
echo.

echo 📁 Production dosyalari olusturuluyor...
echo.

REM Production environment dosyasi olustur
echo # PRODUCTION ENVIRONMENT VARIABLES > esref1-main\backend\.env.production
echo MONGO_URL=mongodb+srv://username:password@cluster.mongodb.net/isitbusy >> esref1-main\backend\.env.production
echo REDIS_URL=redis://localhost:6379 >> esref1-main\backend\.env.production
echo JWT_SECRET=production-jwt-secret-change-this >> esref1-main\backend\.env.production
echo CORS_ORIGINS=https://yourdomain.com,https://www.yourdomain.com >> esref1-main\backend\.env.production
echo GOOGLE_PLACES_API_KEY=your-google-places-api-key >> esref1-main\backend\.env.production
echo GEMINI_API_KEY=your-gemini-api-key >> esref1-main\backend\.env.production
echo ENVIRONMENT=production >> esref1-main\backend\.env.production

echo ✅ .env.production olusturuldu

REM Vercel deployment config
echo { > esref1-main\frontend\vercel.json
echo   "builds": [ >> esref1-main\frontend\vercel.json
echo     { >> esref1-main\frontend\vercel.json
echo       "src": "package.json", >> esref1-main\frontend\vercel.json
echo       "use": "@vercel/static-build", >> esref1-main\frontend\vercel.json
echo       "config": { >> esref1-main\frontend\vercel.json
echo         "distDir": "build" >> esref1-main\frontend\vercel.json
echo       } >> esref1-main\frontend\vercel.json
echo     } >> esref1-main\frontend\vercel.json
echo   ], >> esref1-main\frontend\vercel.json
echo   "routes": [ >> esref1-main\frontend\vercel.json
echo     { >> esref1-main\frontend\vercel.json
echo       "src": "/api/(.*)", >> esref1-main\frontend\vercel.json
echo       "dest": "https://your-backend-url.railway.app/api/$1" >> esref1-main\frontend\vercel.json
echo     }, >> esref1-main\frontend\vercel.json
echo     { >> esref1-main\frontend\vercel.json
echo       "src": "/(.*)", >> esref1-main\frontend\vercel.json
echo       "dest": "/index.html" >> esref1-main\frontend\vercel.json
echo     } >> esref1-main\frontend\vercel.json
echo   ] >> esref1-main\frontend\vercel.json
echo } >> esref1-main\frontend\vercel.json

echo ✅ vercel.json olusturuldu

REM Railway deployment config
echo web: python server.py > esref1-main\backend\Procfile
echo ✅ Procfile olusturuldu

echo.
echo 📁 Deployment dosyalari hazir!
pause

echo ========================================
echo    ADIM 4: BETA USER LISTESI OLUSTUR
echo ========================================
echo.

echo 🎯 BETA TEST HEDEFI: 50-100 kullanici
echo.

echo 📝 BETA USER KAYNAKLARI:
echo ✅ Arkadas ve aile (10-20 kisi)
echo ✅ Sosyal medya takipcileri (20-30 kisi)
echo ✅ Denver Facebook gruplari (20-30 kisi)
echo ✅ Universite ogrencileri (10-20 kisi)
echo.

echo 🎁 BETA USER INCENTIVE'LARI:
echo ✅ Erken erisim badge
echo ✅ Premium features ucretsiz
echo ✅ Leaderboard'da ozel isim
echo ✅ Venue recommendations priority
echo.

echo 📋 BETA SIGNUP FORM OLUSTURULUYOR...

REM Beta signup HTML formu olustur
echo ^<!DOCTYPE html^> > beta_signup.html
echo ^<html^> >> beta_signup.html
echo ^<head^> >> beta_signup.html
echo     ^<title^>Is It Busy? Beta Signup^</title^> >> beta_signup.html
echo     ^<style^> >> beta_signup.html
echo         body { font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px; } >> beta_signup.html
echo         .form-group { margin: 20px 0; } >> beta_signup.html
echo         input, textarea { width: 100%%; padding: 10px; margin: 5px 0; } >> beta_signup.html
echo         button { background: #007bff; color: white; padding: 15px 30px; border: none; border-radius: 5px; cursor: pointer; } >> beta_signup.html
echo         .hero { text-align: center; margin-bottom: 40px; } >> beta_signup.html
echo     ^</style^> >> beta_signup.html
echo ^</head^> >> beta_signup.html
echo ^<body^> >> beta_signup.html
echo     ^<div class="hero"^> >> beta_signup.html
echo         ^<h1^>🍺 Is It Busy? Beta Access^</h1^> >> beta_signup.html
echo         ^<p^>Denver'in ilk real-time venue busyness uygulamasi!^</p^> >> beta_signup.html
echo         ^<p^>Beta testcisi ol, premium ozellikleri ucretsiz kullan!^</p^> >> beta_signup.html
echo     ^</div^> >> beta_signup.html
echo     ^<form action="https://formspree.io/f/your-form-id" method="POST"^> >> beta_signup.html
echo         ^<div class="form-group"^> >> beta_signup.html
echo             ^<label^>Isim:^</label^> >> beta_signup.html
echo             ^<input type="text" name="name" required^> >> beta_signup.html
echo         ^</div^> >> beta_signup.html
echo         ^<div class="form-group"^> >> beta_signup.html
echo             ^<label^>Email:^</label^> >> beta_signup.html
echo             ^<input type="email" name="email" required^> >> beta_signup.html
echo         ^</div^> >> beta_signup.html
echo         ^<div class="form-group"^> >> beta_signup.html
echo             ^<label^>Telefon:^</label^> >> beta_signup.html
echo             ^<input type="tel" name="phone"^> >> beta_signup.html
echo         ^</div^> >> beta_signup.html
echo         ^<div class="form-group"^> >> beta_signup.html
echo             ^<label^>Denver'da en cok gittigin yerler:^</label^> >> beta_signup.html
echo             ^<textarea name="venues" rows="3"^>^</textarea^> >> beta_signup.html
echo         ^</div^> >> beta_signup.html
echo         ^<button type="submit"^>Beta Access Iste! 🚀^</button^> >> beta_signup.html
echo     ^</form^> >> beta_signup.html
echo ^</body^> >> beta_signup.html
echo ^</html^> >> beta_signup.html

echo ✅ beta_signup.html olusturuldu
echo 🌐 Formu Formspree ile aktif hale getirin: https://formspree.io
pause

echo ========================================
echo    ADIM 5: SOSYAL MEDYA HAZIRLIK
echo ========================================
echo.

echo 📱 SOSYAL MEDYA HESAPLARI:
echo ✅ Instagram: @isitbusydenver
echo ✅ TikTok: @isitbusyapp  
echo ✅ Facebook: Is It Busy Denver
echo ✅ Twitter: @isitbusyapp
echo.

echo 📸 CONTENT FIKIRLERI:
echo ✅ Denver venue spotlights
echo ✅ Nightlife tips ve tricks
echo ✅ Real-time busyness screenshots
echo ✅ User testimonials
echo ✅ Behind-the-scenes development
echo.

echo 🎨 BRAND ASSETS OLUSTURULUYOR...

REM Social media post template
echo 🍺 DENVER'S HOTTEST SPOTS, REAL-TIME! > social_media_content.txt
echo. >> social_media_content.txt
echo 📍 4,355+ venues tracked >> social_media_content.txt
echo 📊 Live busyness updates >> social_media_content.txt
echo 🎉 Events ^& nightlife discovery >> social_media_content.txt
echo 🏆 Gamification ^& rewards >> social_media_content.txt
echo. >> social_media_content.txt
echo Join the beta: [link] >> social_media_content.txt
echo #Denver #Nightlife #TechStartup #IsItBusy >> social_media_content.txt

echo ✅ social_media_content.txt olusturuldu
pause

echo ========================================
echo    ADIM 6: LAUNCH TIMELINE
echo ========================================
echo.

echo 📅 LAUNCH TAKVIMI:
echo.
echo [BUGUN - GUN 1]
echo ✅ Domain satin al
echo ✅ Vercel ^& Railway hesaplari ac
echo ✅ MongoDB Atlas setup
echo ✅ Beta signup form yayinla
echo.

echo [YARIN - GUN 2]
echo ✅ Frontend Vercel'e deploy
echo ✅ Backend Railway'e deploy  
echo ✅ Database migration
echo ✅ SSL sertifikasi kontrol
echo.

echo [GUN 3-4]
echo ✅ Production testing
echo ✅ Performance optimization
echo ✅ Beta user recruitment (50 kisi)
echo ✅ Social media accounts setup
echo.

echo [GUN 5-7]
echo ✅ Beta launch (50 kullanici)
echo ✅ User feedback collection
echo ✅ Bug fixes ^& improvements
echo ✅ Local PR ^& marketing
echo.

echo [HAFTA 2]
echo ✅ Public launch
echo ✅ Denver marketing push
echo ✅ Venue partnerships
echo ✅ User acquisition campaigns
echo.
pause

echo ========================================
echo    ADIM 7: HEMEN YAPILACAKLAR
echo ========================================
echo.

echo 🎯 SIMDI YAPMANIZ GEREKENLER:
echo.

echo [1] DOMAIN SATIN AL (30 dakika)
echo 🌐 https://namecheap.com
echo 💡 Oneri: isitbusy.com veya isitbusydenver.com
echo.

echo [2] HOSTING HESAPLARI AC (30 dakika)
echo 🚀 Vercel: https://vercel.com (frontend)
echo 🚂 Railway: https://railway.app (backend)
echo 🍃 MongoDB Atlas: https://cloud.mongodb.com (database)
echo.

echo [3] BETA SIGNUP FORM YAYINLA (15 dakika)
echo 📝 Formspree: https://formspree.io
echo 📄 beta_signup.html dosyasini kullan
echo.

echo [4] SOSYAL MEDYA HESAPLARI AC (45 dakika)
echo 📱 Instagram, TikTok, Facebook, Twitter
echo 📸 social_media_content.txt'i kullan
echo.

echo [5] BETA USER RECRUITMENT BASLA (surekli)
echo 👥 Arkadas, aile, sosyal medya
echo 🎯 Hedef: 50-100 kisi
echo.

echo ========================================
echo    LAUNCH SUCCESS METRICS
echo ========================================
echo.

echo 📊 HAFTA 1 HEDEFLERI:
echo ✅ 50+ beta users
echo ✅ 500+ app sessions
echo ✅ 10+ dakika avg session time
echo ✅ 5+ venues per session
echo.

echo 📊 AY 1 HEDEFLERI:
echo ✅ 1,000+ daily active users
echo ✅ 20%% weekly retention
echo ✅ 10+ venue partnerships
echo ✅ $500+ monthly revenue
echo.

echo 📊 AY 2 HEDEFLERI:
echo ✅ 5,000+ daily active users
echo ✅ 30%% weekly retention
echo ✅ 50+ venue partnerships
echo ✅ $2,000+ monthly revenue
echo.

echo ========================================
echo    LAUNCH HAZIRLIK TAMAMLANDI!
echo ========================================
echo.

echo 🎉 TUM DOSYALAR HAZIR!
echo 📁 .env.production
echo 📁 vercel.json
echo 📁 Procfile
echo 📁 beta_signup.html
echo 📁 social_media_content.txt
echo.

echo 🚀 SIMDI YAPMANIZ GEREKENLER:
echo 1. Domain satin al
echo 2. Hosting hesaplari ac
echo 3. Beta signup form yayinla
echo 4. Sosyal medya hesaplari ac
echo 5. Beta user recruitment basla
echo.

echo 🎯 LAUNCH ZAMANI: 7 GUN ICINDE!
echo 💰 TOPLAM MALIYET: $50-100/ay
echo 📈 BASARI SANSI: %%90+
echo.

echo HAZIR MISINIZ? HEMEN BASLAYIN! 🚀
echo.
pause