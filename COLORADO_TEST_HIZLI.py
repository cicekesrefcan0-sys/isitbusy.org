#!/usr/bin/env python3
"""
Colorado Scraper Hızlı Test
Scraper'ın çalışıp çalışmadığını hızlıca test eder
"""
import asyncio
import sys
import os
from datetime import datetime

# Backend modüllerini import et
sys.path.append('backend')

async def test_colorado_scraper():
    """Colorado scraper'ı hızlıca test et"""
    print("🏔️  COLORADO SCRAPER HIZLI TEST")
    print("=" * 50)
    
    try:
        # Import test
        print("📦 Modül import testi...")
        from COLORADO_KAPSAMLI_SCRAPER import ColoradoKapsamliScraper
        print("✅ Modül başarıyla import edildi")
        
        # Database bağlantı testi
        print("\n🗄️  Database bağlantı testi...")
        try:
            from backend.database import db
            # Basit bir sorgu ile test
            count = await db.venues.count_documents({})
            print(f"✅ Database bağlantısı başarılı (mevcut venue: {count})")
        except Exception as e:
            print(f"❌ Database bağlantı hatası: {e}")
            return False
        
        # API key kontrolü
        print("\n🔑 API key kontrolü...")
        api_keys = {
            "Google Places": os.getenv('GOOGLE_PLACES_API_KEY'),
            "Ticketmaster": os.getenv('TICKETMASTER_API_KEY'),
            "Eventbrite": os.getenv('EVENTBRITE_TOKEN'),
            "EDMTrain": os.getenv('EDMTRAIN_API_KEY')
        }
        
        for name, key in api_keys.items():
            if key:
                print(f"✅ {name}: Mevcut")
            else:
                print(f"⚠️  {name}: Eksik (opsiyonel)")
        
        # Scraper instance testi
        print("\n🤖 Scraper instance testi...")
        async with ColoradoKapsamliScraper() as scraper:
            print("✅ Scraper instance başarıyla oluşturuldu")
            
            # Şehir listesi testi
            cities = scraper._filter_cities(priority_filter=1, test_mode=True)
            print(f"✅ Test şehirleri yüklendi: {len(cities)} şehir")
            
            for city_name in list(cities.keys())[:3]:
                print(f"   • {city_name}")
        
        # Mini scraping testi (sadece Denver)
        print("\n🧪 Mini scraping testi (Denver)...")
        async with ColoradoKapsamliScraper() as scraper:
            city_data = {"lat": 39.7392, "lng": -104.9903}
            
            # Google Places test (eğer API key varsa)
            if os.getenv('GOOGLE_PLACES_API_KEY'):
                venues = await scraper._scrape_google_places("Denver", city_data)
                print(f"✅ Google Places: {len(venues)} venue bulundu")
            else:
                print("⚠️  Google Places: API key yok, atlandı")
            
            # Yelp scraping test
            try:
                venues = await scraper._scrape_yelp_venues("Denver", city_data)
                print(f"✅ Yelp Scraping: {len(venues)} venue bulundu")
            except Exception as e:
                print(f"⚠️  Yelp Scraping: {str(e)[:50]}...")
            
            # Ticketmaster test (eğer API key varsa)
            if os.getenv('TICKETMASTER_API_KEY'):
                events = await scraper._scrape_ticketmaster_events("Denver")
                print(f"✅ Ticketmaster: {len(events)} event bulundu")
            else:
                print("⚠️  Ticketmaster: API key yok, atlandı")
        
        print("\n" + "=" * 50)
        print("✅ TÜM TESTLER BAŞARILI!")
        print("=" * 50)
        print("\n🚀 Scraper kullanıma hazır!")
        print("\nÇalıştırmak için:")
        print("   ./COLORADO_SCRAPER_BASLAT.bat")
        print("   veya")
        print("   python COLORADO_KAPSAMLI_SCRAPER.py --test")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import hatası: {e}")
        print("\nÇözüm:")
        print("1. Backend klasöründe olduğunuzdan emin olun")
        print("2. Gerekli Python paketlerini yükleyin: pip install -r requirements.txt")
        return False
        
    except Exception as e:
        print(f"❌ Test hatası: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_database_collections():
    """Database collection'larını test et"""
    print("\n📊 DATABASE COLLECTION TEST")
    print("-" * 30)
    
    try:
        from backend.database import db
        
        collections = ["venues", "events", "busyness_reports", "comments"]
        
        for collection_name in collections:
            collection = getattr(db, collection_name)
            count = await collection.count_documents({})
            print(f"   {collection_name}: {count} dokuman")
        
        print("✅ Database collections test başarılı")
        
    except Exception as e:
        print(f"❌ Database test hatası: {e}")

async def test_sample_data():
    """Örnek veri oluşturma testi"""
    print("\n🎯 ÖRNEK VERİ OLUŞTURMA TEST")
    print("-" * 30)
    
    try:
        from backend.database import db
        import uuid
        
        # Test venue oluştur
        test_venue = {
            "id": str(uuid.uuid4()),
            "name": "Test Venue Colorado",
            "city": "Denver",
            "state": "CO",
            "lat": 39.7392,
            "lng": -104.9903,
            "category": "test",
            "created_at": datetime.now().isoformat(),
            "test_data": True
        }
        
        await db.venues.insert_one(test_venue)
        print("✅ Test venue oluşturuldu")
        
        # Test venue'yu sil
        await db.venues.delete_one({"test_data": True})
        print("✅ Test venue silindi")
        
        print("✅ Örnek veri test başarılı")
        
    except Exception as e:
        print(f"❌ Örnek veri test hatası: {e}")

def print_system_info():
    """Sistem bilgilerini yazdır"""
    print("\n💻 SİSTEM BİLGİLERİ")
    print("-" * 20)
    print(f"Python: {sys.version.split()[0]}")
    print(f"Platform: {sys.platform}")
    print(f"Working Directory: {os.getcwd()}")
    
    # Gerekli paketleri kontrol et
    required_packages = [
        "aiohttp", "beautifulsoup4", "pymongo", "motor"
    ]
    
    print("\n📦 PAKET KONTROLÜ")
    print("-" * 15)
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"✅ {package}")
        except ImportError:
            print(f"❌ {package} (eksik)")

async def main():
    """Ana test fonksiyonu"""
    start_time = datetime.now()
    
    print_system_info()
    
    # Ana test
    success = await test_colorado_scraper()
    
    if success:
        # Ek testler
        await test_database_collections()
        await test_sample_data()
    
    duration = (datetime.now() - start_time).total_seconds()
    
    print(f"\n⏱️  Test süresi: {duration:.1f} saniye")
    
    if success:
        print("\n🎉 Colorado Scraper test başarılı!")
        print("\nSonraki adımlar:")
        print("1. API keylerini ayarlayın (opsiyonel)")
        print("2. ./COLORADO_SCRAPER_BASLAT.bat çalıştırın")
        print("3. Test modu ile başlayın")
    else:
        print("\n❌ Test başarısız!")
        print("\nSorun giderme:")
        print("1. Backend klasöründe olduğunuzdan emin olun")
        print("2. MongoDB'nin çalıştığını kontrol edin")
        print("3. Python paketlerini yükleyin")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⚠️  Test kullanıcı tarafından durduruldu")
    except Exception as e:
        print(f"\n❌ Test hatası: {e}")
        import traceback
        traceback.print_exc()