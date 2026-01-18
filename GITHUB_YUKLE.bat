@echo off
echo ========================================
echo    GITHUB'A KOD YUKLEME REHBERI
echo ========================================
echo.

echo 🎯 ADIM 1: GitHub hesabiniz var mi?
echo.
echo Eger yoksa:
echo 1. https://github.com adresine gidin
echo 2. "Sign up" butonuna tiklayin
echo 3. Email, username, password girin
echo 4. Hesabi dogrulayin
echo.
pause

echo ========================================
echo    ADIM 2: YENİ REPOSITORY OLUSTUR
echo ========================================
echo.

echo 1. GitHub'da "New repository" butonuna tiklayin
echo 2. Repository name: "isitbusy-app" yazin
echo 3. Description: "Denver nightlife real-time tracker"
echo 4. Public secin (ucretsiz)
echo 5. "Create repository" butonuna tiklayin
echo.
pause

echo ========================================
echo    ADIM 3: GIT KURULUMU KONTROL
echo ========================================
echo.

echo Git kurulu mu kontrol ediliyor...
git --version
if %errorlevel% neq 0 (
    echo ❌ Git kurulu degil!
    echo.
    echo Git indirin:
    echo 🔗 https://git-scm.com/download/win
    echo.
    echo Kurduktan sonra bu scripti tekrar calistirin.
    pause
    exit
) else (
    echo ✅ Git kurulu!
)
echo.
pause

echo ========================================
echo    ADIM 4: KODU GITHUB'A YUKLE
echo ========================================
echo.

echo Simdi kodu GitHub'a yukleyecegiz...
echo.

REM Git repository'yi initialize et
echo [1/6] Git repository initialize ediliyor...
git init
echo.

REM Tum dosyalari ekle
echo [2/6] Dosyalar ekleniyor...
git add .
echo.

REM Ilk commit
echo [3/6] Ilk commit yapiliyor...
git commit -m "Initial commit - Is It Busy Denver app"
echo.

REM Branch adini main yap
echo [4/6] Branch main olarak ayarlaniyor...
git branch -M main
echo.

echo [5/6] GitHub repository URL'ini girin:
echo Ornek: https://github.com/yourusername/isitbusy-app.git
set /p REPO_URL="GitHub Repository URL: "
echo.

REM Remote origin ekle
echo [6/6] GitHub'a baglaniyor ve kod yukleniyor...
git remote add origin %REPO_URL%
git push -u origin main
echo.

if %errorlevel% equ 0 (
    echo ✅ KOD BASARIYLA GITHUB'A YUKLENDI!
    echo 🌐 Repository: %REPO_URL%
) else (
    echo ❌ Hata olustu. GitHub URL'ini kontrol edin.
    echo.
    echo Olasi sorunlar:
    echo - GitHub URL yanlis
    echo - Internet baglantisi yok
    echo - GitHub authentication gerekli
)
echo.
pause