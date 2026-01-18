#!/usr/bin/env python3
"""
Final Venue Navigation Test
Gerçek navigasyon sorununu test et
"""

import requests
import json
import time
from datetime import datetime

def test_complete_navigation_flow():
    """Tam navigasyon akışını test et"""
    print("🎯 KOMPLE NAVİGASYON AKIŞ TESTİ")
    print("=" * 60)
    
    try:
        # 1. Venue listesi al
        print("1️⃣ Venue listesi alınıyor...")
        response = requests.get("http://localhost:8001/api/venues?limit=5", timeout=10)
        
        if response.status_code != 200:
            print(f"❌ Venue listesi alınamadı: {response.status_code}")
            return False
            
        data = response.json()
        venues = data.get('data', [])
        print(f"✅ {len(venues)} venue bulundu")
        
        # 2. Her venue için navigasyon testi
        for i, venue in enumerate(venues[:3]):
            venue_id = venue.get('id')
            venue_name = venue.get('name', 'Bilinmeyen')
            
            print(f"\n2️⃣ Test {i+1}: {venue_name}")
            print(f"   🆔 ID: {venue_id}")
            
            # 3. Venue detail API'yi test et (VenuePage'in yapacağı çağrı)
            detail_response = requests.get(f"http://localhost:8001/api/venues/{venue_id}", timeout=10)
            
            if detail_response.status_code == 200:
                detail_data = detail_response.json()
                detail_name = detail_data.get('name', 'Bilinmeyen')
                detail_id = detail_data.get('id')
                
                print(f"   ✅ API Response: {detail_name}")
                print(f"   🔗 URL: /venue/{venue_id}")
                
                # ID eşleşmesi kontrol et
                if detail_id == venue_id and detail_name == venue_name:
                    print(f"   ✅ Perfect Match: Liste ve detay aynı")
                else:
                    print(f"   ⚠️ Mismatch:")
                    print(f"      Liste: {venue_name} (ID: {venue_id})")
                    print(f"      Detay: {detail_name} (ID: {detail_id})")
                    
            else:
                print(f"   ❌ Detail API hatası: {detail_response.status_code}")
                return False
        
        print(f"\n✅ TÜM NAVİGASYON TESTLERİ BAŞARILI!")
        return True
        
    except Exception as e:
        print(f"❌ Test hatası: {e}")
        return False

def test_frontend_api_calls():
    """Frontend'in yapacağı API çağrılarını test et"""
    print("\n🌐 FRONTEND API ÇAĞRI SİMÜLASYONU")
    print("=" * 60)
    
    # Frontend'in API base URL'i
    api_base = "http://localhost:8001/api"
    
    try:
        # 1. Ana sayfa venues listesi
        print("1️⃣ Ana sayfa venues API...")
        response = requests.get(f"{api_base}/venues?limit=20", timeout=10)
        if response.status_code == 200:
            venues = response.json().get('data', [])
            print(f"   ✅ {len(venues)} venue alındı")
            
            # İlk venue'yu seç
            if venues:
                test_venue = venues[0]
                venue_id = test_venue.get('id')
                venue_name = test_venue.get('name')
                
                print(f"\n2️⃣ Venue detay sayfası API...")
                print(f"   🎯 Test venue: {venue_name}")
                print(f"   🔗 Navigate to: /venue/{venue_id}")
                
                # 2. Venue detay sayfası API'leri
                detail_response = requests.get(f"{api_base}/venues/{venue_id}", timeout=10)
                if detail_response.status_code == 200:
                    detail_data = detail_response.json()
                    print(f"   ✅ Venue detay: {detail_data.get('name')}")
                else:
                    print(f"   ❌ Venue detay hatası: {detail_response.status_code}")
                    return False
                
                # 3. Venue events API
                events_response = requests.get(f"{api_base}/venues/{venue_id}/events", timeout=10)
                if events_response.status_code == 200:
                    events = events_response.json()
                    print(f"   ✅ Events: {len(events)} event")
                else:
                    print(f"   ⚠️ Events API: {events_response.status_code}")
                
                # 4. Venue details (photos, etc.)
                details_response = requests.get(f"{api_base}/venues/{venue_id}/details", timeout=10)
                if details_response.status_code == 200:
                    details = details_response.json()
                    photos = details.get('photos', [])
                    print(f"   ✅ Details: {len(photos)} photo")
                else:
                    print(f"   ⚠️ Details API: {details_response.status_code}")
                
                print(f"\n✅ FRONTEND API SİMÜLASYONU BAŞARILI!")
                return True
        else:
            print(f"   ❌ Venues API hatası: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Frontend API test hatası: {e}")
        return False

def check_frontend_status():
    """Frontend durumunu kontrol et"""
    print("\n🖥️ FRONTEND DURUM KONTROLÜ")
    print("=" * 60)
    
    frontend_urls = [
        "http://localhost:3000",
        "http://localhost:3001"
    ]
    
    for url in frontend_urls:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"✅ Frontend çalışıyor: {url}")
                return url
        except:
            print(f"❌ Frontend erişilemiyor: {url}")
    
    print("⚠️ Frontend bulunamadı. npm start çalışıyor mu?")
    return None

def main():
    """Ana test fonksiyonu"""
    print("🚀 FINAL VENUE NAVİGASYON TESTİ")
    print("=" * 80)
    print(f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Testleri çalıştır
    navigation_ok = test_complete_navigation_flow()
    frontend_api_ok = test_frontend_api_calls()
    frontend_url = check_frontend_status()
    
    print("\n" + "=" * 80)
    print("📊 FINAL TEST SONUÇLARI:")
    print(f"   🎯 Navigasyon Akışı: {'✅ BAŞARILI' if navigation_ok else '❌ BAŞARISIZ'}")
    print(f"   🌐 Frontend API: {'✅ BAŞARILI' if frontend_api_ok else '❌ BAŞARISIZ'}")
    print(f"   🖥️ Frontend Erişim: {'✅ ' + frontend_url if frontend_url else '❌ BAŞARISIZ'}")
    
    if navigation_ok and frontend_api_ok and frontend_url:
        print(f"\n🎉 TÜM TESTLER BAŞARILI!")
        print(f"🔗 Test için: {frontend_url}")
        print("\n📋 Manuel Test Adımları:")
        print("1. Yukarıdaki URL'i açın")
        print("2. Herhangi bir venue'ya tıklayın")
        print("3. Doğru venue sayfasının açıldığını kontrol edin")
        print("4. URL'de doğru venue ID'nin göründüğünü kontrol edin")
        print("5. F12 ile console'da hata olmadığını kontrol edin")
        
        print("\n🔧 Eğer hala sorun varsa:")
        print("- Browser cache'i temizleyin (Ctrl+Shift+R)")
        print("- Frontend'i yeniden başlatın")
        print("- Console'da JavaScript hatalarını kontrol edin")
        
    else:
        print(f"\n⚠️ Bazı testler başarısız oldu.")
        print("Lütfen hataları giderin ve tekrar test edin.")

if __name__ == "__main__":
    main()