#!/usr/bin/env python3
"""
Gerçek Sorun Tespit Scripti
Frontend'de gerçekte ne olduğunu anlayalım
"""

import requests
import json
import time
from datetime import datetime

def check_frontend_console_errors():
    """Frontend console hatalarını kontrol etmek için rehber"""
    print("🌐 FRONTEND CONSOLE HATA KONTROL REHBERİ")
    print("=" * 60)
    
    print("Manuel kontrol adımları:")
    print("1. Frontend'i açın: http://localhost:3000 veya http://localhost:3001")
    print("2. F12 ile Developer Tools açın")
    print("3. Console sekmesine geçin")
    print("4. Sayfayı yenileyin (F5)")
    print("5. Herhangi bir venue'ya tıklayın")
    print("6. Console'da aşağıdaki hataları arayın:")
    print()
    print("🔍 Aranacak Hatalar:")
    print("   - 'Cannot read property of undefined'")
    print("   - 'venue.id is undefined'")
    print("   - 'Failed to fetch'")
    print("   - '404 Not Found'")
    print("   - '500 Internal Server Error'")
    print("   - React Router hataları")
    print("   - 'useParams is not defined'")
    print()
    print("📊 Network Sekmesi Kontrolü:")
    print("   - Network sekmesine geçin")
    print("   - Venue'ya tıklayın")
    print("   - API çağrılarını kontrol edin:")
    print("     * GET /api/venues/{id} - 200 OK olmalı")
    print("     * GET /api/venues/{id}/details - 200 veya 404")
    print("     * GET /api/venues/{id}/events - 200 veya 404")

def test_specific_venue_navigation():
    """Belirli bir venue ile navigasyon testi"""
    print("\n🎯 SPESİFİK VENUE NAVİGASYON TESTİ")
    print("=" * 60)
    
    try:
        # Backend'den ilk venue'yu al
        response = requests.get("http://localhost:8001/api/venues?limit=1", timeout=10)
        if response.status_code == 200:
            data = response.json()
            venues = data.get('data', [])
            
            if venues:
                venue = venues[0]
                venue_id = venue.get('id')
                venue_name = venue.get('name')
                
                print(f"🎯 Test Venue: {venue_name}")
                print(f"🆔 Venue ID: {venue_id}")
                print(f"🔗 Frontend URL: http://localhost:3000/venue/{venue_id}")
                print(f"🔗 Alternative URL: http://localhost:3001/venue/{venue_id}")
                
                # API endpoint'ini test et
                detail_response = requests.get(f"http://localhost:8001/api/venues/{venue_id}", timeout=10)
                if detail_response.status_code == 200:
                    detail_data = detail_response.json()
                    print(f"✅ Backend API çalışıyor: {detail_data.get('name')}")
                    
                    print(f"\n📋 Manuel Test Adımları:")
                    print(f"1. Bu URL'i açın: http://localhost:3000/venue/{venue_id}")
                    print(f"2. Sayfa yükleniyor mu kontrol edin")
                    print(f"3. Venue adı '{venue_name}' görünüyor mu kontrol edin")
                    print(f"4. F12 ile console'da hata var mı kontrol edin")
                    
                    return venue_id, venue_name
                else:
                    print(f"❌ Backend API hatası: {detail_response.status_code}")
                    return None, None
            else:
                print("❌ Hiç venue bulunamadı")
                return None, None
        else:
            print(f"❌ Venue listesi alınamadı: {response.status_code}")
            return None, None
            
    except Exception as e:
        print(f"❌ Test hatası: {e}")
        return None, None

def check_react_router_config():
    """React Router konfigürasyonunu kontrol et"""
    print("\n⚛️ REACT ROUTER KONFIGÜRASYON KONTROLÜ")
    print("=" * 60)
    
    try:
        with open('frontend/src/App.js', 'r', encoding='utf-8') as f:
            content = f.read()
            
        print("🔍 App.js dosyası kontrol ediliyor...")
        
        # Route tanımlarını kontrol et
        if '/venue/:id' in content:
            print("✅ /venue/:id route tanımı bulundu")
        else:
            print("❌ /venue/:id route tanımı bulunamadı!")
            
        if 'VenuePage' in content:
            print("✅ VenuePage import edilmiş")
        else:
            print("❌ VenuePage import edilmemiş!")
            
        if 'BrowserRouter' in content:
            print("✅ BrowserRouter kullanılıyor")
        else:
            print("❌ BrowserRouter bulunamadı!")
            
        print("\n📋 Route Konfigürasyonu:")
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if '/venue/:id' in line:
                print(f"   Satır {i+1}: {line.strip()}")
                
    except FileNotFoundError:
        print("❌ frontend/src/App.js dosyası bulunamadı!")
    except Exception as e:
        print(f"❌ Dosya okuma hatası: {e}")

def check_venue_page_component():
    """VenuePage bileşenini kontrol et"""
    print("\n📄 VENUEPAGE BİLEŞEN KONTROLÜ")
    print("=" * 60)
    
    try:
        with open('frontend/src/pages/VenuePage.jsx', 'r', encoding='utf-8') as f:
            content = f.read()
            
        print("🔍 VenuePage.jsx dosyası kontrol ediliyor...")
        
        # useParams kontrolü
        if 'useParams' in content:
            print("✅ useParams import edilmiş")
        else:
            print("❌ useParams import edilmemiş!")
            
        if 'const { id } = useParams()' in content:
            print("✅ useParams() ile id alınıyor")
        else:
            print("❌ useParams() ile id alınmıyor!")
            
        # API çağrısı kontrolü
        if f'${API}/venues/${id}' in content or '${API}/venues/${id}' in content:
            print("✅ API çağrısı doğru formatta")
        else:
            print("❌ API çağrısı formatı hatalı!")
            
        print("\n📋 useParams Kullanımı:")
        lines = content.split('\n')
        for i, line in enumerate(lines):
            if 'useParams' in line:
                print(f"   Satır {i+1}: {line.strip()}")
                
    except FileNotFoundError:
        print("❌ frontend/src/pages/VenuePage.jsx dosyası bulunamadı!")
    except Exception as e:
        print(f"❌ Dosya okuma hatası: {e}")

def main():
    """Ana fonksiyon"""
    print("🚀 GERÇEK SORUN TESPİT ANALİZİ")
    print("=" * 80)
    print(f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Analizleri çalıştır
    check_react_router_config()
    check_venue_page_component()
    venue_id, venue_name = test_specific_venue_navigation()
    check_frontend_console_errors()
    
    print("\n" + "=" * 80)
    print("📊 SORUN TESPİT ÖZETİ:")
    
    if venue_id:
        print(f"✅ Test venue hazır: {venue_name} (ID: {venue_id})")
        print(f"🔗 Test URL: http://localhost:3000/venue/{venue_id}")
        
        print(f"\n🎯 SONRAKİ ADIMLAR:")
        print(f"1. Yukarıdaki URL'i tarayıcıda açın")
        print(f"2. F12 ile Developer Tools açın")
        print(f"3. Console ve Network sekmelerini kontrol edin")
        print(f"4. Hataları not alın ve paylaşın")
        
    else:
        print("❌ Test venue hazırlanamadı")
        print("Backend'i kontrol edin")

if __name__ == "__main__":
    main()