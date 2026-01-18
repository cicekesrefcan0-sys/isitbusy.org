"""
Sistem Durum Kontrolü - Tüm servislerin çalışıp çalışmadığını kontrol eder
"""
import requests
import asyncio
import json
from datetime import datetime

def check_service(name, url, timeout=5):
    """Servis durumunu kontrol et"""
    try:
        response = requests.get(url, timeout=timeout)
        if response.status_code == 200:
            return {"status": "✅ ÇALIŞIYOR", "code": response.status_code, "response_time": f"{response.elapsed.total_seconds():.2f}s"}
        else:
            return {"status": "⚠️ PROBLEM", "code": response.status_code, "response_time": f"{response.elapsed.total_seconds():.2f}s"}
    except requests.exceptions.ConnectionError:
        return {"status": "❌ BAĞLANTI YOK", "code": "N/A", "response_time": "N/A"}
    except requests.exceptions.Timeout:
        return {"status": "⏰ TIMEOUT", "code": "N/A", "response_time": ">5s"}
    except Exception as e:
        return {"status": f"❌ HATA: {str(e)}", "code": "N/A", "response_time": "N/A"}

def test_api_endpoints():
    """API endpoint'lerini test et"""
    base_url = "http://localhost:8001"
    
    endpoints = [
        {"name": "Health Check", "url": f"{base_url}/health"},
        {"name": "Venues List", "url": f"{base_url}/api/venues"},
        {"name": "Trending Venues", "url": f"{base_url}/api/trending/venues"},
        {"name": "Analytics", "url": f"{base_url}/api/analytics"},
        {"name": "News", "url": f"{base_url}/api/news"},
        {"name": "Search", "url": f"{base_url}/api/search/venues"},
    ]
    
    print("🔍 API ENDPOINT TESTLERİ")
    print("=" * 60)
    
    for endpoint in endpoints:
        result = check_service(endpoint["name"], endpoint["url"])
        print(f"{endpoint['name']:<20} | {result['status']:<15} | {result['code']:<10} | {result['response_time']}")
    
    print("\n")

def test_frontend():
    """Frontend durumunu kontrol et"""
    print("🌐 FRONTEND DURUMU")
    print("=" * 60)
    
    frontend_url = "http://localhost:3000"
    result = check_service("React Frontend", frontend_url)
    print(f"Frontend Server     | {result['status']:<15} | {result['code']:<10} | {result['response_time']}")
    
    print("\n")

def test_database_connection():
    """Veritabanı bağlantısını test et"""
    print("🗄️ VERİTABANI DURUMU")
    print("=" * 60)
    
    try:
        # MongoDB bağlantısını test et
        import pymongo
        client = pymongo.MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=3000)
        client.server_info()  # Bağlantıyı test et
        
        # Veritabanı istatistikleri
        db = client.isitbusy
        venue_count = db.venues.count_documents({})
        user_count = db.users.count_documents({})
        report_count = db.busyness_reports.count_documents({})
        
        print(f"MongoDB Bağlantısı  | ✅ ÇALIŞIYOR      | Aktif         | <1s")
        print(f"Venues Collection   | {venue_count} mekan        | Hazır         | -")
        print(f"Users Collection    | {user_count} kullanıcı      | Hazır         | -")
        print(f"Reports Collection  | {report_count} rapor        | Hazır         | -")
        
        client.close()
        
    except Exception as e:
        print(f"MongoDB Bağlantısı  | ❌ BAĞLANTI YOK   | Hata          | N/A")
        print(f"Hata: {str(e)}")
    
    print("\n")

def test_sample_data():
    """Örnek veri çekmeyi test et"""
    print("📊 VERİ TESTLERİ")
    print("=" * 60)
    
    try:
        # Venues test
        response = requests.get("http://localhost:8001/api/venues?limit=5", timeout=5)
        if response.status_code == 200:
            data = response.json()
            venues = data.get('data', [])  # API response format: {"data": venues, "total": count}
            print(f"Venues API          | ✅ ÇALIŞIYOR      | {len(venues)} mekan    | {response.elapsed.total_seconds():.2f}s")
            
            if venues:
                sample_venue = venues[0]
                print(f"Örnek Mekan         | {sample_venue.get('name', 'N/A')[:20]:<15} | {sample_venue.get('city', 'N/A'):<10} | -")
        else:
            print(f"Venues API          | ⚠️ PROBLEM        | {response.status_code}         | {response.elapsed.total_seconds():.2f}s")
    
    except Exception as e:
        print(f"Venues API          | ❌ HATA           | N/A        | N/A")
    
    try:
        # Search test
        response = requests.get("http://localhost:8001/api/search/venues?q=church", timeout=5)
        if response.status_code == 200:
            results = response.json()
            venues = results.get('venues', [])
            print(f"Search API          | ✅ ÇALIŞIYOR      | {len(venues)} sonuç    | {response.elapsed.total_seconds():.2f}s")
        else:
            print(f"Search API          | ⚠️ PROBLEM        | {response.status_code}         | {response.elapsed.total_seconds():.2f}s")
    
    except Exception as e:
        print(f"Search API          | ❌ HATA           | N/A        | N/A")
    
    print("\n")

def main():
    """Ana test fonksiyonu"""
    print("\n" + "=" * 60)
    print("🚀 SİSTEM DURUM KONTROLÜ")
    print("=" * 60)
    print(f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    print()
    
    # Frontend kontrolü
    test_frontend()
    
    # Backend API kontrolü
    test_api_endpoints()
    
    # Veritabanı kontrolü
    test_database_connection()
    
    # Veri testleri
    test_sample_data()
    
    print("=" * 60)
    print("📋 ÖZET")
    print("=" * 60)
    
    # Genel durum özeti
    services_to_check = [
        ("Frontend", "http://localhost:3000"),
        ("Backend API", "http://localhost:8001/health"),
        ("Venues API", "http://localhost:8001/api/venues"),
        ("Search API", "http://localhost:8001/api/search/venues?q=test")
    ]
    
    working_services = 0
    total_services = len(services_to_check)
    
    for name, url in services_to_check:
        result = check_service(name, url, timeout=3)
        if "✅" in result["status"]:
            working_services += 1
    
    print(f"Çalışan Servisler: {working_services}/{total_services}")
    
    if working_services == total_services:
        print("🎉 TÜM SİSTEMLER ÇALIŞIYOR!")
        print("✅ Sistem production-ready durumda")
        print("🌐 Frontend: http://localhost:3000")
        print("🔧 Backend API: http://localhost:8001")
    elif working_services >= total_services - 1:
        print("⚠️ SİSTEM ÇOĞUNLUKLA ÇALIŞIYOR")
        print("💡 Bazı servisler sorunlu olabilir")
    else:
        print("❌ SİSTEMDE SORUNLAR VAR")
        print("🔧 Servisleri yeniden başlatmayı deneyin")
        print("   1. MongoDB: 1_MONGODB_BASLAT.bat")
        print("   2. Backend: 2_BACKEND_BASLAT.bat")
        print("   3. Frontend: 3_FRONTEND_BASLAT.bat")
    
    print("=" * 60)

if __name__ == "__main__":
    main()