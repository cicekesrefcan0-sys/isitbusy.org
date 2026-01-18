#!/usr/bin/env python3
"""
CORS ve API Test
Frontend'in backend'e neden bağlanamadığını tespit et
"""

import requests
import json
from datetime import datetime

def test_backend_direct():
    """Backend'i direkt test et"""
    print("🔧 BACKEND DİREKT TESTİ")
    print("=" * 40)
    
    try:
        # Health check
        response = requests.get("http://localhost:8001/health", timeout=5)
        if response.status_code == 200:
            print("✅ Backend health check başarılı")
        else:
            print(f"⚠️ Backend health check: {response.status_code}")
    except Exception as e:
        print(f"❌ Backend health check hatası: {e}")
        return False
    
    try:
        # API venues endpoint
        response = requests.get("http://localhost:8001/api/venues?limit=3", timeout=10)
        if response.status_code == 200:
            data = response.json()
            venues = data.get('data', [])
            print(f"✅ Backend API çalışıyor: {len(venues)} venue")
            return True
        else:
            print(f"❌ Backend API hatası: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend API test hatası: {e}")
        return False

def test_cors_headers():
    """CORS header'larını test et"""
    print("\n🌐 CORS HEADER TESTİ")
    print("=" * 40)
    
    try:
        # OPTIONS request (preflight)
        response = requests.options(
            "http://localhost:8001/api/venues",
            headers={
                'Origin': 'http://localhost:3000',
                'Access-Control-Request-Method': 'GET',
                'Access-Control-Request-Headers': 'Content-Type'
            },
            timeout=5
        )
        
        print(f"OPTIONS Response Status: {response.status_code}")
        print("CORS Headers:")
        for header, value in response.headers.items():
            if 'access-control' in header.lower():
                print(f"  {header}: {value}")
        
        # GET request with Origin header
        response = requests.get(
            "http://localhost:8001/api/venues?limit=1",
            headers={'Origin': 'http://localhost:3000'},
            timeout=5
        )
        
        print(f"\nGET Response Status: {response.status_code}")
        print("CORS Headers in GET response:")
        for header, value in response.headers.items():
            if 'access-control' in header.lower():
                print(f"  {header}: {value}")
                
        return response.status_code == 200
        
    except Exception as e:
        print(f"❌ CORS test hatası: {e}")
        return False

def test_frontend_backend_connection():
    """Frontend'in backend'e bağlantısını simüle et"""
    print("\n🔗 FRONTEND-BACKEND BAĞLANTI SİMÜLASYONU")
    print("=" * 40)
    
    # Frontend'in yapacağı API çağrısını simüle et
    headers = {
        'Origin': 'http://localhost:3000',
        'Referer': 'http://localhost:3000/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    }
    
    try:
        response = requests.get(
            "http://localhost:8001/api/venues?limit=5",
            headers=headers,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            venues = data.get('data', [])
            print(f"✅ Frontend simülasyonu başarılı: {len(venues)} venue")
            
            if venues:
                venue = venues[0]
                venue_id = venue.get('id')
                venue_name = venue.get('name')
                
                # Venue detail API'yi test et
                detail_response = requests.get(
                    f"http://localhost:8001/api/venues/{venue_id}",
                    headers=headers,
                    timeout=10
                )
                
                if detail_response.status_code == 200:
                    detail_data = detail_response.json()
                    print(f"✅ Venue detail API başarılı: {detail_data.get('name')}")
                    return True
                else:
                    print(f"❌ Venue detail API hatası: {detail_response.status_code}")
                    return False
            else:
                print("⚠️ Venue listesi boş")
                return False
        else:
            print(f"❌ Frontend simülasyon hatası: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Frontend-Backend bağlantı hatası: {e}")
        return False

def check_backend_port():
    """Backend'in hangi portta çalıştığını kontrol et"""
    print("\n🔍 BACKEND PORT KONTROLÜ")
    print("=" * 40)
    
    ports = [8000, 8001, 8002, 5000]
    working_ports = []
    
    for port in ports:
        try:
            response = requests.get(f"http://localhost:{port}/health", timeout=3)
            if response.status_code == 200:
                print(f"✅ Port {port} çalışıyor")
                working_ports.append(port)
            else:
                print(f"⚠️ Port {port} yanıt: {response.status_code}")
        except:
            print(f"❌ Port {port} bağlantı hatası")
    
    return working_ports

def main():
    """Ana test fonksiyonu"""
    print("🚀 CORS VE API BAĞLANTI TESTİ")
    print("=" * 60)
    print(f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Testleri çalıştır
    working_ports = check_backend_port()
    backend_ok = test_backend_direct()
    cors_ok = test_cors_headers()
    connection_ok = test_frontend_backend_connection()
    
    print("\n" + "=" * 60)
    print("📊 TEST SONUÇLARI:")
    print(f"   🔧 Backend Çalışıyor: {'✅' if backend_ok else '❌'}")
    print(f"   🌐 CORS Konfigürasyonu: {'✅' if cors_ok else '❌'}")
    print(f"   🔗 Frontend Bağlantı: {'✅' if connection_ok else '❌'}")
    print(f"   📡 Çalışan Portlar: {working_ports}")
    
    if not backend_ok:
        print(f"\n❌ BACKEND SORUNU:")
        print(f"   - Backend çalışmıyor veya erişilemiyor")
        print(f"   - Port 8001'de backend var mı kontrol edin")
        
    elif not cors_ok:
        print(f"\n❌ CORS SORUNU:")
        print(f"   - CORS header'ları eksik veya yanlış")
        print(f"   - Backend CORS konfigürasyonunu kontrol edin")
        
    elif not connection_ok:
        print(f"\n❌ BAĞLANTI SORUNU:")
        print(f"   - Frontend backend'e bağlanamıyor")
        print(f"   - Network/Firewall sorunu olabilir")
        
    else:
        print(f"\n✅ TÜM TESTLER BAŞARILI!")
        print(f"   Backend ve CORS düzgün çalışıyor")
        print(f"   Sorun frontend'de olabilir")
        
        print(f"\n🔧 FRONTEND KONTROL ÖNERİLERİ:")
        print(f"   1. Browser cache'i temizleyin (Ctrl+Shift+R)")
        print(f"   2. Frontend'i yeniden başlatın")
        print(f"   3. Browser console'da JavaScript hataları kontrol edin")
        print(f"   4. Network sekmesinde API çağrıları kontrol edin")

if __name__ == "__main__":
    main()