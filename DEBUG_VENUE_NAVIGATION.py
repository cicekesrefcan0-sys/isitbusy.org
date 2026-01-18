#!/usr/bin/env python3
"""
Venue navigation sorununu debug eden script
"""
import requests
import json

def debug_venues():
    """Venue verilerini debug et"""
    print("🔍 VENUE NAVIGATION DEBUG")
    print("=" * 60)
    
    try:
        # Backend'ten venue listesini al
        response = requests.get('http://localhost:8001/api/venues?limit=10', timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            venues = data.get('data', [])
            
            print(f"✅ Backend'ten {len(venues)} venue alındı")
            print("\n📋 İlk 5 Venue Detayları:")
            print("-" * 60)
            
            for i, venue in enumerate(venues[:5], 1):
                print(f"\n{i}. {venue.get('name', 'İsim yok')}")
                print(f"   🆔 ID: {venue.get('id', 'ID yok')}")
                print(f"   📍 Adres: {venue.get('address', 'Adres yok')}")
                print(f"   🏷️  Tip: {venue.get('type', 'Tip yok')}")
                print(f"   🔗 Veri kaynağı: {venue.get('data_source', 'Bilinmiyor')}")
                print(f"   🖼️  Resim: {'✅' if venue.get('image_url') else '❌'}")
                print(f"   ⭐ Rating: {venue.get('rating', 'Yok')}")
                print(f"   💰 Price Level: {venue.get('price_level', 'Yok')}")
                
                # Venue detail endpoint'ini test et
                venue_id = venue.get('id')
                if venue_id:
                    try:
                        detail_response = requests.get(f'http://localhost:8001/api/venues/{venue_id}', timeout=5)
                        if detail_response.status_code == 200:
                            print(f"   ✅ Detail endpoint çalışıyor")
                        else:
                            print(f"   ❌ Detail endpoint hatası: {detail_response.status_code}")
                    except:
                        print(f"   ❌ Detail endpoint erişilemez")
            
            # Toplam istatistikler
            print(f"\n📊 GENEL İSTATİSTİKLER:")
            print("-" * 60)
            
            real_venues = [v for v in venues if v.get('data_source') == 'google_places']
            mock_venues = [v for v in venues if v.get('data_source') != 'google_places']
            with_images = [v for v in venues if v.get('image_url')]
            
            print(f"🟢 Gerçek veri (Google Places): {len(real_venues)}")
            print(f"🔴 Mock/Test verisi: {len(mock_venues)}")
            print(f"🖼️  Resimli venue: {len(with_images)}")
            print(f"📈 Resim oranı: {len(with_images)/len(venues)*100:.1f}%")
            
            if len(mock_venues) > 0:
                print(f"\n⚠️  MOCK VERİ BULUNDU:")
                for venue in mock_venues:
                    print(f"   - {venue.get('name')} (kaynak: {venue.get('data_source')})")
            
            return True
            
        else:
            print(f"❌ Backend API hatası: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Backend'e bağlanılamıyor!")
        print("   Backend çalışıyor mu? http://localhost:8001")
        return False
    except Exception as e:
        print(f"❌ Beklenmeyen hata: {e}")
        return False

def test_frontend_connection():
    """Frontend bağlantısını test et"""
    print(f"\n🌐 FRONTEND BAĞLANTI TESTİ")
    print("=" * 60)
    
    ports = [3000, 3001]
    
    for port in ports:
        try:
            response = requests.get(f'http://localhost:{port}', timeout=5)
            if response.status_code == 200:
                print(f"✅ Frontend çalışıyor: http://localhost:{port}")
                return port
            else:
                print(f"⚠️  Port {port}: HTTP {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"❌ Port {port}: Bağlantı yok")
        except Exception as e:
            print(f"❌ Port {port}: {e}")
    
    return None

def main():
    print("🚀 VENUE NAVIGATION SORUN TESPİTİ")
    print("=" * 60)
    
    # Backend test
    backend_ok = debug_venues()
    
    # Frontend test
    frontend_port = test_frontend_connection()
    
    # Sonuç ve öneriler
    print(f"\n💡 SONUÇ VE ÖNERİLER:")
    print("=" * 60)
    
    if backend_ok:
        print("✅ Backend çalışıyor ve veri döndürüyor")
    else:
        print("❌ Backend sorunu var - önce backend'i düzelt")
        return
    
    if frontend_port:
        print(f"✅ Frontend çalışıyor: http://localhost:{frontend_port}")
        print(f"\n🎯 YAPILACAKLAR:")
        print(f"1. Ana sayfayı aç: http://localhost:{frontend_port}")
        print(f"2. Browser cache temizle: Ctrl+Shift+R")
        print(f"3. F12 ile Developer Tools aç")
        print(f"4. Console'da hata var mı kontrol et")
        print(f"5. Network sekmesinde API çağrıları kontrol et")
    else:
        print("❌ Frontend çalışmıyor - npm start yap")

if __name__ == '__main__':
    main()