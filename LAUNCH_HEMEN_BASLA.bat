@echo off
echo ========================================
echo    ISITBUSY.ORG HEMEN LAUNCH!
echo ========================================
echo.

echo 🎉 DOMAIN ALINDI: isitbusy.org ✅
echo 🚀 Hemen live yapalim!
echo.

echo ========================================
echo    LAUNCH SURECI - 3 ADIM
echo ========================================
echo.

echo [ADIM 1] Git kurulum ve GitHub upload
echo [ADIM 2] Vercel deployment
echo [ADIM 3] Domain baglama ve test
echo.

echo Toplam sure: 30-45 dakika
echo Sonuc: https://isitbusy.org live!
echo.

echo ========================================
echo    ADIM 1: GIT VE GITHUB
echo ========================================
echo.

echo 🔧 Git kurulumu kontrol ediliyor...
git --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Git kurulu degil!
    echo.
    echo 🔗 HEMEN YAPIN:
    echo 1. https://git-scm.com/download/win
    echo 2. "64-bit Git for Windows Setup" indirin
    echo 3. Kurun (default ayarlar tamam)
    echo 4. Bu scripti tekrar calistirin
    echo.
    pause
    exit
) else (
    echo ✅ Git kurulu!
)

echo.
echo 🌐 GitHub repository olusturun:
echo.
echo 1. https://github.com → "New repository"
echo 2. Name: "isitbusy-app"
echo 3. Public secin
echo 4. "Create repository"
echo.

echo ✅ Repository olusturduktan sonra ENTER'a basin...
pause

echo.
echo 📝 GitHub repository URL'inizi girin:
set /p REPO_URL="Repository URL: "

echo.
echo 📤 Kod yukleniyor...

git init
git config --global user.name "IsItBusy Developer" 2>nul
git config --global user.email "developer@isitbusy.org" 2>nul
git add .
git commit -m "Initial commit - Is It Busy Denver app"
git branch -M main
git remote add origin %REPO_URL%
git push -u origin main

if %errorlevel% equ 0 (
    echo ✅ GitHub'a kod yuklendi!
) else (
    echo ❌ Hata! URL'i kontrol edin ve tekrar deneyin.
    pause
    exit
)

echo.
echo ========================================
echo    ADIM 2: VERCEL DEPLOYMENT
echo ========================================
echo.

echo 🚀 HEMEN YAPIN:
echo.
echo 1. https://vercel.com → "Sign Up"
echo 2. "Continue with GitHub"
echo 3. "New Project"
echo 4. "isitbusy-app" repository'yi import edin
echo 5. Root Directory: "frontend" SECIN!
echo 6. "Deploy" butonuna tiklayin
echo.

echo ✅ Deployment tamamlandiginda ENTER'a basin...
pause

echo ========================================
echo    ADIM 3: DOMAIN BAGLAMA
echo ========================================
echo.

echo 🌐 Vercel'de:
echo 1. Project → Settings → Domains
echo 2. "Add Domain" → "isitbusy.org"
echo 3. DNS kayitlarini alin
echo.

echo 🔧 Domain provider'da DNS ayarlari:
echo A Record: @ → 76.76.19.61
echo CNAME: www → cname.vercel-dns.com
echo.

echo ✅ DNS ayarlarini yaptiktan sonra ENTER'a basin...
pause

echo ========================================
echo    FINAL TEST
echo ========================================
echo.

echo ⏰ 5-10 dakika bekleyin...
echo.

echo 🌐 Test: https://isitbusy.org
echo.

echo Beklenen:
echo ✅ Sayfa yukleniyor
echo ✅ SSL aktif
echo ✅ Harita gorunuyor
echo ✅ Venue listesi var
echo.

echo ========================================
echo    TEBRIKLER! 🎉
echo ========================================
echo.

echo 🚀 isitbusy.org LIVE!
echo 🌐 https://isitbusy.org
echo.

echo 📊 DURUM:
echo ✅ Frontend: Live
echo ⏳ Backend: Sonraki adim
echo ⏳ Database: Sonraki adim
echo.

echo 🎯 SONRAKI: Backend deployment
echo.

echo HARIKA IS! 💪
pause