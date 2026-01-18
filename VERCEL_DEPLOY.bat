@echo off
echo ========================================
echo    VERCEL DEPLOYMENT - isitbusy.org
echo ========================================
echo.

echo 🎉 GitHub'a kod yuklendi! ✅
echo 🚀 Simdi Vercel'e deploy edelim!
echo.

echo ========================================
echo    ADIM 1: VERCEL HESABI AC
echo ========================================
echo.

echo 🌐 Tarayicinizi acin ve su adimları yapin:
echo.
echo 1. https://vercel.com adresine gidin
echo 2. "Sign Up" butonuna tiklayin
echo 3. "Continue with GitHub" secin
echo 4. GitHub hesabinizla giris yapin
echo 5. Vercel'e GitHub erisim izni verin
echo.

echo ✅ Vercel hesabi actiktan sonra ENTER'a basin...
pause

echo ========================================
echo    ADIM 2: PROJE IMPORT ET
echo ========================================
echo.

echo Vercel dashboard'da:
echo.
echo 1. "New Project" butonuna tiklayin (sag ust)
echo 2. "Import Git Repository" bolumunde
echo 3. "isitbusy-app" repository'nizi bulun
echo 4. "Import" butonuna tiklayin
echo.

echo ✅ Repository import ettiginde ENTER'a basin...
pause

echo ========================================
echo    ADIM 3: PROJE AYARLARI (ONEMLI!)
echo ========================================
echo.

echo ⚠️ DIKKAT: Bu ayarlar cok onemli!
echo.
echo 📁 Root Directory: "frontend" SECIN
echo    (Bu cok onemli! Mutlaka frontend klasorunu secin)
echo.
echo 🔧 Framework Preset: "Create React App" (otomatik algılar)
echo 📦 Build Command: "npm run build" (otomatik)
echo 📂 Output Directory: "build" (otomatik)
echo.

echo ✅ Ayarlari yaptiktan sonra ENTER'a basin...
pause

echo ========================================
echo    ADIM 4: DEPLOY ET
echo ========================================
echo.

echo 🚀 "Deploy" butonuna tiklayin!
echo.
echo ⏰ 2-3 dakika bekleyin...
echo 📊 Build loglarini izleyin
echo.
echo Build basarili olursa:
echo ✅ "Congratulations!" mesaji goreceksiniz
echo 🌐 Otomatik URL: https://isitbusy-app-xxx.vercel.app
echo.

echo ✅ Deployment basarili oldugunda ENTER'a basin...
pause

echo ========================================
echo    ADIM 5: CUSTOM DOMAIN BAGLAMA
echo ========================================
echo.

echo Vercel dashboard'da:
echo.
echo 1. Project'inize tiklayin
echo 2. "Settings" sekmesine gidin
echo 3. Sol menuden "Domains" secin
echo 4. "Add Domain" butonuna tiklayin
echo 5. "isitbusy.org" yazin
echo 6. "Add" butonuna tiklayin
echo.

echo Vercel size DNS kayitlarini verecek:
echo 📝 A Record: @ → 76.76.19.61
echo 📝 CNAME: www → cname.vercel-dns.com
echo.

echo ✅ Domain eklediginde ENTER'a basin...
pause

echo ========================================
echo    ADIM 6: DNS AYARLARI
echo ========================================
echo.

echo 🔧 isitbusy.org'u aldiginiz sitede DNS ayarlari yapin:
echo.
echo Domain provider'iniza gidin ve:
echo.
echo ➕ A Record ekleyin:
echo    Name: @ (veya bos birak)
echo    Value: 76.76.19.61
echo    TTL: 300 (veya Auto)
echo.
echo ➕ CNAME Record ekleyin:
echo    Name: www
echo    Value: cname.vercel-dns.com
echo    TTL: 300 (veya Auto)
echo.

echo 💾 "Save" veya "Update" butonuna tiklayin
echo.

echo ✅ DNS ayarlarini yaptiktan sonra ENTER'a basin...
pause

echo ========================================
echo    ADIM 7: TEST VE DOGRULAMA
echo ========================================
echo.

echo ⏰ 5-10 dakika bekleyin (DNS propagation)
echo.

echo 🌐 Test edin:
echo https://isitbusy.org
echo https://www.isitbusy.org
echo.

echo Beklenen sonuclar:
echo ✅ Sayfa yukleniyor
echo ✅ SSL sertifikasi aktif (kilit ikonu)
echo ✅ Harita gorunuyor
echo ✅ Venue listesi gorunuyor (mock data)
echo ✅ Navigation calisiyor
echo ⚠️ API hatalari normal (backend henuz yok)
echo.

echo ========================================
echo    BASARI KONTROL LISTESI
echo ========================================
echo.

echo ✅ TEKNIK CHECKLIST:
echo [ ] Vercel hesabi acildi
echo [ ] GitHub repository import edildi
echo [ ] Root directory "frontend" secildi
echo [ ] Frontend basariyla deploy edildi
echo [ ] isitbusy.org domain baglandi
echo [ ] DNS kayitlari eklendi
echo [ ] SSL sertifikasi aktif
echo [ ] https://isitbusy.org calisiyor
echo.

echo ✅ FONKSIYONEL CHECKLIST:
echo [ ] Ana sayfa yukleniyor
echo [ ] Harita gorunuyor
echo [ ] Venue listesi gorunuyor
echo [ ] Navigation calisiyor
echo [ ] Responsive tasarim calisiyor
echo [ ] Loading states calisiyor
echo.

echo ========================================
echo    TEBRIKLER! 🎉
echo ========================================
echo.

echo 🚀 isitbusy.org LIVE OLDU!
echo 🌐 https://isitbusy.org
echo.

echo 📊 SIMDIKI DURUM:
echo ✅ Frontend live ve calisiyor
echo ✅ Domain baglandi ve SSL aktif
echo ✅ Harita ve venue listesi gorunuyor
echo ⏳ Backend deployment gerekli (sonraki adim)
echo ⏳ Database setup gerekli (sonraki adim)
echo.

echo 🎯 SONRAKI ADIMLAR:
echo 1. Railway backend deployment
echo 2. MongoDB Atlas database setup
echo 3. API domain baglama (api.isitbusy.org)
echo 4. Environment variables guncelleme
echo 5. Full stack testing
echo.

echo 💪 HARIKA IS CIKARDINIZ!
echo Frontend deployment tamamlandi!
echo.

echo Sonraki adim icin RAILWAY_DEPLOY.bat scriptini calistirin
echo.
pause