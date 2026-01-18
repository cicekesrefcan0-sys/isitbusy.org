@echo off
echo ========================================
echo    🚀 VERCEL HIZLI DEPLOYMENT
echo ========================================
echo.

echo ✅ DOMAIN HAZIR: isitbusy.org
echo 🎯 HEDEF: Frontend'i Vercel'e deploy et
echo.

echo ========================================
echo    ADIM 1: VERCEL HESABI AC
echo ========================================
echo.

echo 🌐 1. https://vercel.com adresine git
echo 👤 2. "Sign Up" butonuna tikla
echo 🔗 3. "Continue with GitHub" sec
echo ✅ 4. GitHub ile giris yap
echo.

echo HEMEN YAPIN! 2 dakika surer.
pause

echo ========================================
echo    ADIM 2: NEW PROJECT OLUSTUR
echo ========================================
echo.

echo 📁 1. Vercel dashboard'da "New Project" tikla
echo 🔗 2. "Import Git Repository" sec
echo 📂 3. GitHub'dan "esref1-main" repository'yi bul
echo ✅ 4. "Import" butonuna tikla
echo.

echo HEMEN YAPIN! 1 dakika surer.
pause

echo ========================================
echo    ADIM 3: PROJECT AYARLARI
echo ========================================
echo.

echo ⚙️ PROJECT CONFIGURATION:
echo.
echo 📁 Root Directory: "frontend" SEC
echo 📦 Framework Preset: "Create React App" (otomatik)
echo 🔧 Build Command: "npm run build" (default)
echo 📂 Output Directory: "build" (default)
echo.

echo 🔑 ENVIRONMENT VARIABLES EKLE:
echo.
echo Variable Name: REACT_APP_API_URL
echo Value: https://api.isitbusy.org
echo.
echo Variable Name: REACT_APP_ENVIRONMENT  
echo Value: production
echo.
echo Variable Name: GENERATE_SOURCEMAP
echo Value: false
echo.

echo HEMEN YAPIN! 3 dakika surer.
pause

echo ========================================
echo    ADIM 4: DEPLOY ET!
echo ========================================
echo.

echo 🚀 1. "Deploy" butonuna tikla
echo ⏰ 2. 2-3 dakika bekle (build process)
echo ✅ 3. "Deployment completed" mesajini bekle
echo 🌐 4. Vercel URL'ini kopyala (ornek: https://esref1-main.vercel.app)
echo.

echo SONUC: Frontend live olacak!
echo.

echo HEMEN YAPIN! 3 dakika surer.
pause

echo ========================================
echo    ADIM 5: CUSTOM DOMAIN BAGLA
echo ========================================
echo.

echo 🔗 VERCEL'DE DOMAIN AYARLARI:
echo.
echo 1. Project dashboard'da "Settings" tikla
echo 2. "Domains" sekmesine git
echo 3. "Add Domain" butonuna tikla
echo 4. "isitbusy.org" yaz
echo 5. "Add" butonuna tikla
echo.

echo 📋 DNS KAYITLARINI KOPYALA:
echo Vercel size su bilgileri verecek:
echo.
echo A Record: @ → 76.76.19.61
echo CNAME: www → cname.vercel-dns.com
echo.

echo HEMEN YAPIN! 2 dakika surer.
pause

echo ========================================
echo    ADIM 6: DOMAIN PROVIDER'DA DNS
echo ========================================
echo.

echo 🌐 DOMAIN PROVIDER'INIZA GIT:
echo (isitbusy.org'u aldiginiz site - Porkbun/Namecheap/etc)
echo.

echo 🔧 DNS MANAGEMENT'A GIT:
echo.

echo ➕ A RECORD EKLE:
echo Name: @ (veya bos birak)
echo Type: A
echo Value: 76.76.19.61
echo TTL: 300 (veya Auto)
echo.

echo ➕ CNAME RECORD EKLE:
echo Name: www
echo Type: CNAME  
echo Value: cname.vercel-dns.com
echo TTL: 300 (veya Auto)
echo.

echo 💾 "Save" veya "Update" butonuna tikla
echo.

echo HEMEN YAPIN! 5 dakika surer.
pause

echo ========================================
echo    ADIM 7: SSL VE TEST
echo ========================================
echo.

echo 🔒 SSL SERTIFIKASI (OTOMATIK):
echo ⏰ 5-10 dakika bekle
echo 🔒 SSL otomatik aktif olacak
echo ✅ https://isitbusy.org calisacak
echo.

echo 🧪 SITE TESTI:
echo.
echo 1. https://isitbusy.org adresine git
echo 2. Sayfa yukleniyor mu kontrol et
echo 3. "Find Venues" butonuna tikla
echo 4. Harita gorunuyor mu kontrol et
echo 5. Venue listesi gorunuyor mu kontrol et
echo.

echo ⚠️ BEKLENEN HATALAR:
echo - API calls fail (backend henuz yok - NORMAL)
echo - Real-time features calismiyor (backend gerekli)
echo - Bu hatalar normal, frontend calisiyor demek!
echo.

echo HEMEN TEST EDIN! 10 dakika surer.
pause

echo ========================================
echo    ADIM 8: BETA SIGNUP FORM
echo ========================================
echo.

echo 📝 FORMSPREE SETUP:
echo.
echo 1. https://formspree.io adresine git
echo 2. "Sign Up" ^> Email ile kayit ol
echo 3. "New Form" tikla
echo 4. Form name: "IsItBusy Beta Signups"
echo 5. Form endpoint'ini kopyala: https://formspree.io/f/xxxxxxxx
echo.

echo 🔧 BETA SAYFASINI GUNCELLE:
echo.
echo 1. Vercel dashboard'da "Functions" veya "Settings" git
echo 2. beta.html dosyasinda form action'ini guncelle:
echo    action="https://formspree.io/f/xxxxxxxx"
echo 3. Redeploy et (otomatik olabilir)
echo.

echo ✅ SONUC: https://isitbusy.org/beta live
echo.

echo HEMEN YAPIN! 10 dakika surer.
pause

echo ========================================
echo    DEPLOYMENT TAMAMLANDI!
echo ========================================
echo.

echo 🎉 TEBRIKLER! FRONTEND LIVE!
echo.

echo 🌐 WEBSITE: https://isitbusy.org
echo 📱 BETA: https://isitbusy.org/beta
echo 📊 VERCEL DASHBOARD: https://vercel.com/dashboard
echo.

echo ✅ BASARILI DEPLOYMENT CHECKLIST:
echo [ ] Vercel hesabi acildi
echo [ ] esref1-main repository import edildi
echo [ ] Frontend basariyla deploy edildi
echo [ ] isitbusy.org domain baglandi
echo [ ] SSL sertifikasi aktif
echo [ ] https://isitbusy.org calisiyor
echo [ ] Beta signup form live
echo.

echo 📊 PERFORMANCE METRIKLERI:
echo 🚀 First Contentful Paint: ^<1.5s
echo 🎯 Largest Contentful Paint: ^<2.5s
echo ⚡ Time to Interactive: ^<3.5s
echo 📱 Mobile Performance Score: ^>90
echo.

echo ========================================
echo    SONRAKI ADIMLAR
echo ========================================
echo.

echo 🔄 SIMDI YAPILACAKLAR:
echo.
echo 1️⃣ RAILWAY BACKEND DEPLOYMENT (30 dk)
echo 2️⃣ MONGODB ATLAS SETUP (20 dk)
echo 3️⃣ API DOMAIN BAGLAMA (api.isitbusy.org)
echo 4️⃣ ENVIRONMENT VARIABLES GUNCELLEME
echo 5️⃣ FULL STACK TESTING
echo.

echo 🎯 BUGUN SONU HEDEFI:
echo ✅ https://isitbusy.org LIVE
echo ✅ https://api.isitbusy.org LIVE
echo ✅ Full-stack app calisyor
echo ✅ 50+ beta user kayit
echo.

echo ========================================
echo    SORUN GIDERME
echo ========================================
echo.

echo 🔧 DOMAIN BAGLANMIYOR:
echo - DNS propagation bekle (24 saate kadar)
echo - DNS kayitlarini kontrol et
echo - Vercel'de domain status kontrol et
echo.

echo 🔧 BUILD HATASI:
echo - Node.js version kontrol et (16+)
echo - Package.json dependencies kontrol et
echo - Vercel logs'u incele
echo.

echo 🔧 SSL HATASI:
echo - Domain dogru baglandiginden emin ol
echo - 24 saat bekle (otomatik SSL)
echo - Vercel support'a basvur
echo.

echo ========================================
echo    BASARI METRIKLERI
echo ========================================
echo.

echo 📊 BUGUN SONU HEDEFLERI:
echo ✅ isitbusy.org live ve calisyor
echo ✅ Page load time ^<2 saniye
echo ✅ Mobile responsive calisyor
echo ✅ SEO meta tags aktif
echo ✅ Beta signup form calisyor
echo.

echo 📊 HAFTA SONU HEDEFLERI:
echo ✅ 100+ page views
echo ✅ 20+ beta signups
echo ✅ Social media shares
echo ✅ Google indexing baslamis
echo.

echo 🎯 FRONTEND DEPLOYMENT BASARILI!
echo 💪 BACKEND DEPLOYMENT'A GECIN!
echo 🚀 LAUNCH DEVAM EDIYOR!
echo.

echo HAZIR MISINIZ? RAILWAY DEPLOYMENT! 🚂
pause