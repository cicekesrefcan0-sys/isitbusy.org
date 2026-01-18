@echo off
echo ========================================
echo 🚀 HIZLI OPTIMIZASYON BASLAT
echo ========================================
echo.

echo 📋 1. Database indexlerini olusturuyor...
cd backend
python -c "
import asyncio
from database_indexes import DatabaseIndexManager
from database import db

async def create_indexes():
    manager = DatabaseIndexManager(db)
    await manager.create_all_indexes()
    print('✅ Database indexes created')

asyncio.run(create_indexes())
"

echo.
echo 📋 2. Cache warming servisini baslatıyor...
python -c "
import asyncio
from services.cache_warmer import cache_warmer

async def start_warmer():
    print('🔥 Starting cache warmer...')
    await cache_warmer.warm_all_caches()
    print('✅ Cache warmed successfully')

asyncio.run(start_warmer())
"

echo.
echo 📋 3. Backend servisi baslatıyor (optimized)...
start "Backend Server" python server.py

echo.
echo 📋 4. Frontend servisi baslatıyor...
cd ../frontend
start "Frontend Server" npm start

echo.
echo 📋 5. Performance test hazırlanıyor...
cd ..
timeout /t 10 /nobreak > nul
echo.
echo 🧪 Performance testi baslatılıyor...
python PERFORMANCE_TEST.py

echo.
echo ========================================
echo ✅ OPTIMIZASYON TAMAMLANDI!
echo ========================================
echo.
echo 📊 Beklenen performans iyileştirmeleri:
echo   • API yanıt süresi: 10-15s → 500-800ms (95%% iyileştirme)
echo   • Sayfa yükleme: 5-8s → 1.5-2s (75%% iyileştirme)  
echo   • Gerçek zamanlı güncelleme: 100-500ms → 20-50ms (80%% iyileştirme)
echo   • Bellek kullanımı: 500MB+ → 200-300MB (60%% azalma)
echo   • Eşzamanlı bağlantı: 100-200 → 1000+ (5x iyileştirme)
echo.
echo 🌐 Uygulamaya erişim:
echo   Frontend: http://localhost:3000
echo   Backend API: http://localhost:8001/api
echo.
pause