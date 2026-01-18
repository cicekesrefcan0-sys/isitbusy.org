#!/usr/bin/env python3
"""
Frontend Port Test
Hangi portta çalıştığını kesin olarak tespit et
"""

import requests
import time

def test_frontend_ports():
    """Frontend portlarını test et"""
    print("🌐 FRONTEND PORT TESTİ")
    print("=" * 40)
    
    ports = [3000, 3001, 3002]
    working_ports = []
    
    for port in ports:
        try:
            print(f"🔍 Port {port} test ediliyor...")
            response = requests.get(f"http://localhost:{port}", timeout=5)
            if response.status_code == 200:
                print(f"✅ Port {port} çalışıyor!")
                working_ports.append(port)
            else:
                print(f"⚠️ Port {port} yanıt kodu: {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"❌ Port {port} bağlantı hatası")
        except Exception as e:
            print(f"❌ Port {port} hata: {e}")
    
    return working_ports

def test_venue_navigation_direct():
    """Direkt venue navigasyonunu test et"""
    print("\n🎯 DIREKT VENUE NAVİGASYON TESTİ")
    print("=" * 40)
    
    # Backend'den test venue al
    try:
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
                
                # Working portları test et
                working_ports = test_frontend_ports()
                
                if working_ports:
                    for port in working_ports:
                        venue_url = f"http://localhost:{port}/venue/{venue_id}"
                        print(f"\n🔗 Test URL (Port {port}): {venue_url}")
                        
                        print(f"\n📋 MANUEL TEST ADIMLARİ:")
                        print(f"1. Bu URL'i tarayıcıda açın: {venue_url}")
                        print(f"2. Sayfa yükleniyor mu kontrol edin")
                        print(f"3. '{venue_name}' venue bilgileri görünüyor mu kontrol edin")
                        print(f"4. F12 ile console'da hata var mı kontrol edin")
                        print(f"5. Network sekmesinde API çağrıları kontrol edin")
                        
                        return venue_url, venue_name
                else:
                    print("❌ Hiçbir frontend portu çalışmıyor!")
                    return None, None
            else:
                print("❌ Test venue bulunamadı")
                return None, None
        else:
            print(f"❌ Backend API hatası: {response.status_code}")
            return None, None
    except Exception as e:
        print(f"❌ Test hatası: {e}")
        return None, None

if __name__ == "__main__":
    print("🚀 FRONTEND PORT VE NAVİGASYON TESTİ")
    print("=" * 60)
    
    venue_url, venue_name = test_venue_navigation_direct()
    
    if venue_url:
        print(f"\n🎉 TEST HAZIR!")
        print(f"🔗 Test URL: {venue_url}")
        print(f"🎯 Beklenen Venue: {venue_name}")
        
        print(f"\n🔧 SORUN TESPİT REHBERİ:")
        print(f"Eğer venue sayfası açılmıyorsa:")
        print(f"1. URL doğru mu? ✓")
        print(f"2. Frontend çalışıyor mu? ✓")
        print(f"3. Backend API çalışıyor mu? ✓")
        print(f"4. React Router çalışıyor mu? → F12 Console kontrol")
        print(f"5. VenuePage component yükleniyor mu? → F12 Console kontrol")
        print(f"6. API çağrıları başarılı mı? → F12 Network kontrol")
        
    else:
        print(f"\n❌ Test hazırlanamadı")
        print(f"Frontend veya Backend çalışmıyor")