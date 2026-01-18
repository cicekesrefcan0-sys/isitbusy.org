@echo off
echo ========================================
echo 🔧 GIT HIZLI KURULUM
echo ========================================
echo.
echo 📥 Git for Windows indiriliyor...
echo.
echo 1. Git for Windows açılacak
echo 2. "Download" butonuna tıkla
echo 3. İndirilen .exe dosyasını çalıştır
echo 4. "Next, Next, Next..." ile kurulumu tamamla
echo 5. Kurulum bitince bu script'i tekrar çalıştır
echo.
pause
echo.
echo 🌐 Git for Windows açılıyor...
start https://git-scm.com/download/win
echo.
echo ⏳ Git kurulumunu tamamla ve sonra devam et...
pause
echo.
echo 🔧 Git kurulumu kontrol ediliyor...
git --version
echo.
if %errorlevel% == 0 (
    echo ✅ Git başarıyla kuruldu!
    echo.
    echo 📋 GitHub bağlantısı kuruluyor...
    cd esref1-main
    git init
    git add .
    git commit -m "Launch files added - isitbusy.org deployment ready"
    echo.
    echo 🔗 GitHub repository oluştur:
    echo 1. https://github.com/new adresine git
    echo 2. Repository name: "esref1-main"
    echo 3. "Create repository" tıkla
    echo 4. Açılan sayfadaki komutları kopyala-yapıştır
    echo.
    start https://github.com/new
) else (
    echo ❌ Git kurulumu tamamlanmadı
    echo Lütfen kurulumu tamamla ve tekrar dene
)
pause