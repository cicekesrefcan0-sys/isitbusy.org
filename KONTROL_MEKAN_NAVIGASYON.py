#!/usr/bin/env python3
"""
Mekan Navigasyon Düzeltme Kontrolü
Bu script yapılan düzeltmeleri doğrular
"""

import requests
import json
import time
from datetime import datetime

def test_backend_api():
    """Backend API'yi test et"""
    print("🔍 BACKEND API TESTİ")
    print("=" * 40)
    
    backend_url = "http://localhost:8001"
    
    try:
        # Health check
        response = requests.get(f"{backend_url}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Backend çalışıyor")
        else:
            print(f"⚠️ Backend health check: {response.status_code}")
    except:
        print("❌ Backend'e bağlanılamıyor")
        return False
    
    try:
        # Venue listesi
        response = requests.get(f"{backend_url}/api/venues?limit=5", timeout=10)
        if response.status_code == 200:
            data = response.json()
            venues = data.get('data', [])
            print(f"✅ {len(venues)} mekan bulundu")
            
            # İlk mekanı test et
            if venues:
                venue = venues[0]
                venue_id = venue.get('id')
                venue_name = venue.get('name', 'Bilinmeyen')
                
                print(f"🎯 Test Mekanı: {venue_name} (ID: {venue_id})")
                
                # Tek mekan detayı
                detail_response = requests.get(f"{backend_url}/api/venues/{venue_id}", timeout=10)
                if detail_response.status_code == 200:
                    detail_data = detail_response.json()
                    detail_name = detail_data.get('name', 'Bilinmeyen')
                    
                    if detail_name == venue_name:
                        print("✅ Mekan ID eşleştirmesi doğru")
                        return True
                    else:
                        print(f"❌ ID eşleştirme hatası: {venue_name} != {detail_name}")
                        return False
                else:
                    print(f"❌ Mekan detayı alınamadı: {detail_response.status_code}")
                    return False
            else:
                print("⚠️ Hiç mekan bulunamadı")
                return False
        else:
            print(f"❌ Venue listesi alınamadı: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ API test hatası: {e}")
        return False

def check_frontend_files():
    """Frontend dosyalarındaki düzeltmeleri kontrol et"""
    print("\n🔧 FRONTEND DÜZELTME KONTROLÜ")
    print("=" * 40)
    
    files_to_check = [
        {
            'file': 'frontend/src/pages/HomePage.jsx',
            'patterns': [
                'venue.id || venue._id',
                'navigate(`/venue/${venue.id || venue._id}`)'
            ]
        },
        {
            'file': 'frontend/src/components/TrendingVenues.jsx',
            'patterns': [
                'venue.id || venue._id',
                'navigate(`/venue/${venue.id || venue._id}`)'
            ]
        }
    ]
    
    all_good = True
    
    for file_info in files_to_check:
        file_path = file_info['file']
        patterns = file_info['patterns']
        
        print(f"\n📁 Kontrol: {file_path}")
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            for pattern in patterns:
                if pattern in content:
                    print(f"   ✅ Bulundu: {pattern}")
                else:
                    print(f"   ❌ Bulunamadı: {pattern}")
                    all_good = False
                    
        except FileNotFoundError:
            print(f"   ❌ Dosya bulunamadı: {file_path}")
            all_good = False
        except Exception as e:
            print(f"   ❌ Dosya okuma hatası: {e}")
            all_good = False
    
    return all_good

def test_frontend_connection():
    """Frontend bağlantısını test et"""
    print("\n🌐 FRONTEND BAĞLANTI TESTİ")
    print("=" * 40)
    
    frontend_url = "http://localhost:3001"
    
    try:
        response = requests.get(frontend_url, timeout=10)
        if response.status_code == 200:
            print("✅ Frontend erişilebilir")
            print(f"   URL: {frontend_url}")
            return True
        else:
            print(f"⚠️ Frontend yanıt kodu: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Frontend'e bağlanılamıyor")
        print("   Frontend başlatılmış mı? (npm start)")
        return False
    except Exception as e:
        print(f"❌ Frontend test hatası: {e}")
        return False

def main():
    """Ana test fonksiyonu"""
    print("🚀 MEKAN NAVİGASYON DÜZELTME KONTROLÜ")
    print("=" * 60)
    print(f"Tarih: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Testleri çalıştır
    frontend_files_ok = check_frontend_files()
    backend_api_ok = test_backend_api()
    frontend_connection_ok = test_frontend_connection()
    
    # Sonuçları özetle
    print("\n" + "=" * 60)
    print("📊 TEST SONUÇLARI:")
    print(f"   Frontend Düzeltmeleri: {'✅ TAMAM' if frontend_files_ok else '❌ SORUN VAR'}")
    print(f"   Backend API: {'✅ TAMAM' if backend_api_ok else '❌ SORUN VAR'}")
    print(f"   Frontend Bağlantı: {'✅ TAMAM' if frontend_connection_ok else '❌ SORUN VAR'}")
    
    if frontend_files_ok and backend_api_ok and frontend_connection_ok:
        print("\n🎉 TÜM KONTROLLER BAŞARILI!")
        print("Mekan navigasyon sorunu düzeltildi.")
        print(f"\n🔗 Test için: {frontend_url if frontend_connection_ok else 'Frontend başlatılmamış'}")
        
        print("\n📋 Manuel Test Adımları:")
        print("1. Frontend'i açın (http://localhost:3001)")
        print("2. Ana sayfada herhangi bir mekana tıklayın")
        print("3. Doğru mekan sayfasının açıldığını kontrol edin")
        print("4. Trending mekanlardan da test edin")
        
    else:
        print("\n⚠️ Bazı kontroller başarısız oldu.")
        print("Lütfen sorunları giderin ve tekrar test edin.")
    
    return frontend_files_ok and backend_api_ok and frontend_connection_ok

if __name__ == "__main__":
    success = main()
    exit(0 if success else 1)