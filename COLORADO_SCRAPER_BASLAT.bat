@echo off
echo ========================================
echo 🏔️  COLORADO KAPSAMLI SCRAPER
echo ========================================
echo.

echo Hangi modu çalıştırmak istiyorsunuz?
echo.
echo 1. Test Modu (5 şehir, hızlı test)
echo 2. Öncelikli Şehirler (Denver, Boulder, Colorado Springs vb.)
echo 3. Tüm Colorado (50+ şehir, tam scraping)
echo 4. Sadece Venue Scraping
echo 5. Sadece Event Scraping
echo.
set /p choice="Seçiminizi yapın (1-5): "

if "%choice%"=="1" goto test_mode
if "%choice%"=="2" goto priority_mode
if "%choice%"=="3" goto full_mode
if "%choice%"=="4" goto venues_only
if "%choice%"=="5" goto events_only

echo Geçersiz seçim!
pause
exit

:test_mode
echo.
echo 🧪 TEST MODU BAŞLATIYOR...
echo ========================================
echo • Denver, Boulder, Colorado Springs, Aspen, Fort Collins
echo • Hızlı test için optimize edilmiş
echo • Tahmini süre: 5-10 dakika
echo.
python COLORADO_KAPSAMLI_SCRAPER.py --test --priority 1
goto end

:priority_mode
echo.
echo ⭐ ÖNCELİKLİ ŞEHIRLER MODU BAŞLATIYOR...
echo ========================================
echo • Öncelik 1-2 şehirler (yaklaşık 25 şehir)
echo • Denver metro, dağ kasabaları, büyük şehirler
echo • Tahmini süre: 30-45 dakika
echo.
python COLORADO_KAPSAMLI_SCRAPER.py --priority 2
goto end

:full_mode
echo.
echo 🌟 TAM COLORADO SCRAPING BAŞLATIYOR...
echo ========================================
echo • Tüm Colorado şehirleri (50+ şehir)
echo • Kapsamlı venue ve event scraping
echo • Tahmini süre: 1-2 saat
echo.
echo ⚠️  Bu işlem uzun sürebilir. Devam etmek istiyor musunuz? (Y/N)
set /p confirm=
if /i "%confirm%"=="Y" (
    python COLORADO_KAPSAMLI_SCRAPER.py --priority 3
) else (
    echo İşlem iptal edildi.
    goto end
)
goto end

:venues_only
echo.
echo 🏢 SADECE VENUE SCRAPING BAŞLATIYOR...
echo ========================================
echo • Google Places, Yelp, TripAdvisor
echo • Tüm venue tipleri
echo • Tahmini süre: 20-30 dakika
echo.
python COLORADO_KAPSAMLI_SCRAPER.py --venues-only --priority 2
goto end

:events_only
echo.
echo 🎉 SADECE EVENT SCRAPING BAŞLATIYOR...
echo ========================================
echo • Ticketmaster, Eventbrite, EDMTrain
echo • Facebook, Meetup, yerel kaynaklar
echo • Tahmini süre: 15-25 dakika
echo.
python COLORADO_KAPSAMLI_SCRAPER.py --events-only --priority 2
goto end

:end
echo.
echo ========================================
echo ✅ SCRAPING TAMAMLANDI!
echo ========================================
echo.
echo 📊 Sonuçları kontrol edin:
echo   • colorado_scraping_results_*.json
echo   • Backend database (venues, events collections)
echo.
echo 🌐 Test etmek için:
echo   • Frontend: http://localhost:3000
echo   • API: http://localhost:8001/api/venues
echo.
echo 📋 Ek komutlar:
echo   • python COLORADO_KAPSAMLI_SCRAPER.py --help
echo   • python COLORADO_KAPSAMLI_SCRAPER.py --test --priority 1
echo.
pause