@echo off
echo ========================================
echo    GIT KURULUM VE GITHUB UPLOAD
echo ========================================
echo.

echo 🔧 Git kurulu degil! Hemen kuralim...
echo.

echo 1. Tarayicinizi acin
echo 2. https://git-scm.com/download/win adresine gidin
echo 3. "64-bit Git for Windows Setup" indirin
echo 4. Indirilen dosyayi calistirin
echo 5. "Next" butonlarina tiklayin (default ayarlar tamam)
echo 6. Kurulum tamamlandiginda bu scripti tekrar calistirin
echo.

echo ✅ Git kurduktan sonra ENTER'a basin...
pause

echo.
echo 🔄 Git kurulumunu kontrol ediyoruz...
git --version
if %errorlevel% neq 0 (
    echo ❌ Git hala kurulu degil!
    echo Lutfen Git'i kurun ve tekrar deneyin.
    pause
    exit
)

echo ✅ Git basariyla kuruldu!
echo.

echo ========================================
echo    GITHUB REPOSITORY OLUSTURMA
echo ========================================
echo.

echo 🌐 GitHub'da repository olusturun:
echo.
echo 1. https://github.com adresine gidin
echo 2. Eger hesabiniz yoksa "Sign up" yapin
echo 3. "New repository" (yesil buton) tiklayin
echo 4. Repository name: "isitbusy-app" yazin
echo 5. "Public" secin (ucretsiz)
echo 6. "Create repository" butonuna tiklayin
echo.

echo ✅ Repository olusturduktan sonra ENTER'a basin...
pause

echo.
echo 📝 GitHub repository URL'inizi girin:
echo Ornek: https://github.com/yourusername/isitbusy-app.git
set /p REPO_URL="Repository URL: "

echo.
echo 📤 Kodu GitHub'a yukluyoruz...
echo.

REM Git repository initialize
echo [1/6] Git repository initialize ediliyor...
git init

REM Git config (eger yoksa)
git config --global user.name "IsItBusy Developer" 2>nul
git config --global user.email "developer@isitbusy.org" 2>nul

REM Dosyalari ekle
echo [2/6] Dosyalar ekleniyor...
git add .

REM Commit
echo [3/6] Commit yapiliyor...
git commit -m "Initial commit - Is It Busy Denver app ready for launch"

REM Branch main yap
echo [4/6] Branch main olarak ayarlaniyor...
git branch -M main

REM Remote ekle
echo [5/6] GitHub repository baglaniyor...
git remote add origin %REPO_URL%

REM Push
echo [6/6] Kod GitHub'a yukleniyor...
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo ✅ BASARILI! KOD GITHUB'A YUKLENDI!
    echo 🌐 Repository: %REPO_URL%
    echo.
    echo 🎯 Sonraki adim: Vercel deployment
    echo VERCEL_DEPLOY.bat scriptini calistirin
) else (
    echo.
    echo ❌ Hata olustu!
    echo.
    echo Olasi nedenler:
    echo - GitHub URL yanlis girildi
    echo - Internet baglantisi sorunu
    echo - GitHub authentication gerekli
    echo.
    echo Cozum:
    echo 1. GitHub URL'ini kontrol edin
    echo 2. GitHub hesabinizla giris yaptiginizdan emin olun
    echo 3. Bu scripti tekrar calistirin
)

echo.
pause