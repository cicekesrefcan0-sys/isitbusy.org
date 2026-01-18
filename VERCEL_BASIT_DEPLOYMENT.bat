@echo off
echo ========================================
echo    VERCEL DEPLOYMENT - BASIT REHBER
echo ========================================
echo.

echo 🎉 isitbusy.org domain alindi! ✅
echo Simdi Vercel'e deploy edelim!
echo.

echo ========================================
echo    ADIM 1: VERCEL HESABI AC
echo ========================================
echo.

echo 1. Tarayicinizi acin
echo 2. https://vercel.com adresine gidin
echo 3. "Sign Up" butonuna tiklayin
echo 4. "Continue with GitHub" secin
echo 5. GitHub hesabinizla giris yapin
echo 6. Vercel'e GitHub erisim izni verin
echo.

echo ✅ Vercel hesabi hazir oldugunda ENTER'a basin...
pause
echo.

echo ========================================
echo    ADIM 2: YENİ PROJE OLUSTUR
echo ========================================
echo.

echo Vercel dashboard'da:
echo.
echo 1. "New Project" butonuna tiklayin
echo 2. "Import Git Repository" bolumunde
echo 3. "isitbusy-app" repository'nizi bulun
echo 4. "Import" butonuna tiklayin
echo.

echo ✅ Repository import edildiginde ENTER'a basin...
pause
echo.

echo ========================================
echo    ADIM 3: PROJE AYARLARI
echo ========================================
echo.

echo Vercel project settings:
echo.
echo 📁 Root Directory: "frontend" SECIN
echo    (Cok onemli! frontend klasorunu secmelisiniz)
echo.
echo 🔧 Framework Preset: "Create React App" (otomatik)
echo 📦 Build Command: "npm run build" (otomatik)
echo 📂 Output Directory: "build" (otomatik)
echo.

echo ✅ Ayarlari yaptiktan sonra ENTER'a basin...
pause
echo.

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
echo 🌐 Otomatik URL: https://isitbusy-app.vercel.app
echo.

echo ✅ Deployment tamamlandiginda ENTER'a basin...
pause
echo.

echo ========================================
echo    ADIM 5: CUSTOM DOMAIN BAGLAMA
echo ========================================
echo.

echo Vercel dashboard'da:
echo.
echo 1. Project'inize tiklayin
echo 2. "Settings" sekmesine gidin
echo 3. "Domains" bolumunu bulun
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
echo.

echo ========================================
echo    ADIM 6: DNS AYARLARI
echo ========================================
echo.

echo Domain provider'iniza gidin (isitbusy.org'u aldiginiz site):
echo.
echo 🔧 DNS Management / DNS Settings bolumunu bulun
echo.
echo ➕ A Record ekleyin:
echo    Name: @ (veya bos)
echo    Value: 76.76.19.61
echo    TTL: 300
echo.
echo ➕ CNAME Record ekleyin:
echo    Name: www
echo    Value: cname.vercel-dns.com
echo    TTL: 300
echo.

echo 💾 "Save" veya "Update" butonuna tiklayin
echo.

echo ✅ DNS ayarlarini yaptiktan sonra ENTER'a basin...
pause
echo.

echo ========================================
echo    ADIM 7: TEST VE DOGRULAMA
echo ========================================
echo.

echo ⏰ 5-10 dakika bekleyin (DNS propagation)
echo.

echo Test edin:
echo 🌐 https://isitbusy.org
echo 🌐 https://www.isitbusy.org
echo.

echo Beklenen sonuclar:
echo ✅ Sayfa yukleniyor
echo ✅ SSL sertifikasi aktif (kilit ikonu)
echo ✅ Harita gorunuyor
echo ✅ Venue listesi gorunuyor
echo ⚠️ API hatalari normal (backend henuz yok)
echo.

echo ========================================
echo    BASARI KONTROL LISTESI
echo ========================================
echo.

echo ✅ TEKNIK CHECKLIST:
echo [ ] Vercel hesabi acildi
echo [ ] GitHub repository import edildi
echo [ ] Frontend basariyla deploy edildi
echo [ ] isitbusy.org domain baglandi
echo [ ] SSL sertifikasi aktif
echo [ ] https://isitbusy.org calisiyor
echo.

echo ✅ FONKSIYONEL CHECKLIST:
echo [ ] Ana sayfa yukleniyor
echo [ ] Harita gorunuyor
echo [ ] Venue listesi gorunuyor (mock data)
echo [ ] Navigation calisiyor
echo [ ] Responsive tasarim calisiyor
echo.

echo ========================================
echo    SORUN GIDERME
echo ========================================
echo.

echo ❌ Build hatasi alirseniz:
echo - Node.js version 16+ gerekli
echo - package.json kontrol edin
echo - Dependencies eksik olabilir
echo.

echo ❌ Domain baglanmiyorsa:
echo - DNS kayitlarini kontrol edin
echo - 24 saat bekleyin (propagation)
echo - Domain provider support'a basvurun
echo.

echo ❌ SSL hatasi alirseniz:
echo - Domain dogru baglandigini kontrol edin
echo - 24 saat bekleyin (otomatik SSL)
echo - Vercel support'a basvurun
echo.

echo ========================================
echo    SONRAKI ADIMLAR
echo ========================================
echo.

echo ✅ Frontend deployment tamamlandi!
echo.

echo 🎯 Sonraki yapilacaklar:
echo 1. Railway backend deployment (30 dakika)
echo 2. MongoDB Atlas setup (20 dakika)
echo 3. API domain baglama (api.isitbusy.org)
echo 4. Environment variables guncelleme
echo 5. Full stack testing
echo.

echo 🎉 TEBRIKLER! isitbusy.org LIVE OLDU!
echo.

echo Simdi backend deployment icin:
echo RAILWAY_DEPLOYMENT.bat scriptini calistirin
echo.
pause