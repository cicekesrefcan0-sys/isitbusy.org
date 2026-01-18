@echo off
echo ========================================
echo    HEMEN SIMDI BASLA - ISITBUSY.ORG
echo ========================================
echo.

echo 🎉 DOMAIN ALINDI: isitbusy.org ✅
echo 🚀 Simdi 3 adimda live yapalim!
echo.

echo ========================================
echo    ADIM 1: GITHUB'A KOD YUKLE
echo ========================================
echo.

echo 🔗 HEMEN YAPIN:
echo 1. https://github.com adresine gidin
echo 2. "New repository" butonuna tiklayin
echo 3. Repository name: "isitbusy-app"
echo 4. Public secin
echo 5. "Create repository" butonuna tiklayin
echo.

echo ✅ Repository olusturduktan sonra ENTER'a basin...
pause

echo.
echo 📤 Kodu GitHub'a yukluyoruz...
echo.

REM GitHub'a kod yükleme
git init
git add .
git commit -m "Initial commit - Is It Busy Denver app"
git branch -M main

echo.
echo 🔗 GitHub repository URL'inizi girin:
echo Ornek: https://github.com/yourusername/isitbusy-app.git
set /p REPO_URL="Repository URL: "

git remote add origin %REPO_URL%
git push -u origin main

if %errorlevel% equ 0 (
    echo ✅ KOD GITHUB'A YUKLENDI!
) else (
    echo ❌ Hata! GitHub URL'ini kontrol edin.
    pause
    exit
)

echo.
pause

echo ========================================
echo    ADIM 2: VERCEL'E DEPLOY ET
echo ========================================
echo.

echo 🚀 HEMEN YAPIN:
echo 1. https://vercel.com adresine gidin
echo 2. "Sign Up" → "Continue with GitHub"
echo 3. "New Project" butonuna tiklayin
echo 4. "isitbusy-app" repository'nizi secin
echo 5. "Import" butonuna tiklayin
echo.

echo ⚙️ ONEMLI AYARLAR:
echo 📁 Root Directory: "frontend" SECIN!
echo 🔧 Framework: Create React App (otomatik)
echo 📦 Build Command: npm run build (otomatik)
echo.

echo 🚀 "Deploy" butonuna tiklayin!
echo.

echo ✅ Deployment tamamlandiginda ENTER'a basin...
pause

echo ========================================
echo    ADIM 3: DOMAIN BAGLAMA
echo ========================================
echo.

echo 🌐 VERCEL'DE:
echo 1. Project → Settings → Domains
echo 2. "Add Domain" → "isitbusy.org"
echo 3. "Add" butonuna tiklayin
echo.

echo 📝 DNS KAYITLARI (domain provider'da):
echo A Record: @ → 76.76.19.61
echo CNAME: www → cname.vercel-dns.com
echo.

echo 🔧 Domain provider'iniza gidin ve DNS ayarlarini yapin
echo.

echo ✅ DNS ayarlarini yaptiktan sonra ENTER'a basin...
pause

echo ========================================
echo    TEST VE DOGRULAMA
echo ========================================
echo.

echo ⏰ 5-10 dakika bekleyin...
echo.

echo 🌐 Test edin: https://isitbusy.org
echo.

echo Beklenen sonuclar:
echo ✅ Sayfa yukleniyor
echo ✅ SSL aktif (kilit ikonu)
echo ✅ Harita gorunuyor
echo ✅ Venue listesi gorunuyor
echo.

echo ========================================
echo    TEBRIKLER! 🎉
echo ========================================
echo.

echo 🚀 isitbusy.org LIVE OLDU!
echo 🌐 https://isitbusy.org
echo.

echo 📊 SIMDIKI DURUM:
echo ✅ Frontend live
echo ⏳ Backend gerekli (sonraki adim)
echo ⏳ Database gerekli (sonraki adim)
echo.

echo 🎯 SONRAKI ADIM:
echo Backend deployment icin Railway kullanacagiz
echo.

echo HAZIR MISINIZ? 🚀
pause