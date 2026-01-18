"""
Website Link Test - Mekan websitelerinin çalışıp çalışmadığını test eder
"""
import requests
import json
from datetime import datetime

def test_venue_websites():
    """Mekan websitelerini test et"""
    print("=" * 80)
    print("🔗 MEKAN WEBSİTE LİNK TESTİ")
    print("=" * 80)
    print(f"Test Zamanı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    # Backend'den mekanları çek
    try:
        response = requests.get("http://localhost:8002/api/venues", timeout=10)
        if response.status_code != 200:
            print("❌ Backend'den mekan verisi alınamadı!")
            return
            
        data = response.json()
        venues = data.get('data', [])
        
        print(f"📍 {len(venues)} mekan bulundu, websiteleri test ediliyor...\n")
        
        successful_links = 0
        total_links = 0
        
        for venue in venues:
            venue_name = venue.get('name', 'Unknown')
            website = venue.get('website', '')
            venue_type = venue.get('type', 'unknown')
            city = venue.get('city', 'Unknown')
            
            print(f"🏢 {venue_name}")
            print(f"   📍 {city}, Colorado")
            print(f"   🏷️ {venue_type}")
            print(f"   🌐 {website}")
            
            if website:
                total_links += 1
                try:
                    # Website'i test et
                    website_response = requests.get(website, timeout=10, allow_redirects=True)
                    
                    if website_response.status_code == 200:
                        print(f"   ✅ Website çalışıyor! (HTTP {website_response.status_code})")
                        successful_links += 1
                        
                        # Content type kontrol et
                        content_type = website_response.headers.get('content-type', '')
                        if 'text/html' in content_type:
                            print(f"   📄 HTML sayfası başarıyla yüklendi")
                        else:
                            print(f"   📄 Content-Type: {content_type}")
                            
                    else:
                        print(f"   ⚠️ Website yanıt veriyor ama hata: HTTP {website_response.status_code}")
                        
                except requests.exceptions.Timeout:
                    print(f"   ⏰ Website timeout (10s)")
                except requests.exceptions.ConnectionError:
                    print(f"   ❌ Website'e bağlanılamıyor")
                except requests.exceptions.RequestException as e:
                    print(f"   ❌ Website hatası: {str(e)[:50]}...")
            else:
                print(f"   ⚠️ Website bilgisi yok")
                
            print()  # Boş satır
            
        # Özet
        print("=" * 80)
        print("📊 WEBSITE TEST ÖZETİ")
        print("=" * 80)
        print(f"Toplam Mekan:          {len(venues)}")
        print(f"Website Olan Mekan:    {total_links}")
        print(f"Çalışan Website:       {successful_links}")
        print(f"Başarı Oranı:          {(successful_links/total_links)*100:.1f}%" if total_links > 0 else "N/A")
        
        if successful_links == total_links and total_links > 0:
            print("\n🎉 MÜKEMMEL! Tüm mekan websiteleri çalışıyor!")
            print("✅ Kullanıcılar mekan websitelerine sorunsuz erişebilir")
        elif successful_links >= total_links * 0.8:
            print("\n✅ İYİ! Çoğu mekan websitesi çalışıyor")
            print("⚠️ Bazı websiteler sorunlu olabilir")
        else:
            print("\n⚠️ DİKKAT! Birçok mekan websitesi sorunlu")
            print("🔧 Website linklerini kontrol edin")
            
        print("=" * 80)
        
    except Exception as e:
        print(f"❌ Test hatası: {str(e)}")

def test_single_venue_website():
    """Tek bir mekanın website'ini detaylı test et"""
    print("\n" + "=" * 80)
    print("🔍 DETAYLI WEBSİTE TESTİ")
    print("=" * 80)
    
    try:
        # İlk mekanı al
        response = requests.get("http://localhost:8002/api/venues/venue-1", timeout=5)
        if response.status_code == 200:
            venue = response.json()
            venue_name = venue.get('name', 'Unknown')
            website = venue.get('website', '')
            
            print(f"🏢 Test Edilen Mekan: {venue_name}")
            print(f"🌐 Website: {website}")
            print()
            
            if website:
                try:
                    print("🔄 Website test ediliyor...")
                    start_time = datetime.now()
                    
                    website_response = requests.get(website, timeout=15, allow_redirects=True)
                    
                    end_time = datetime.now()
                    response_time = (end_time - start_time).total_seconds()
                    
                    print(f"⏱️ Yanıt Süresi: {response_time:.2f} saniye")
                    print(f"📊 HTTP Status: {website_response.status_code}")
                    print(f"🔗 Final URL: {website_response.url}")
                    print(f"📄 Content-Type: {website_response.headers.get('content-type', 'Unknown')}")
                    print(f"📏 Content Length: {len(website_response.content)} bytes")
                    
                    if website_response.status_code == 200:
                        print("✅ Website başarıyla yüklendi!")
                        
                        # Title'ı bulmaya çalış
                        content = website_response.text
                        if '<title>' in content.lower():
                            try:
                                title_start = content.lower().find('<title>') + 7
                                title_end = content.lower().find('</title>')
                                if title_end > title_start:
                                    title = content[title_start:title_end].strip()
                                    print(f"📝 Sayfa Başlığı: {title}")
                            except:
                                pass
                                
                        print("🎯 Bu website kullanıcılara gösterilebilir!")
                    else:
                        print(f"⚠️ Website hata döndürüyor: {website_response.status_code}")
                        
                except Exception as e:
                    print(f"❌ Website test hatası: {str(e)}")
            else:
                print("⚠️ Bu mekanın website bilgisi yok")
                
    except Exception as e:
        print(f"❌ Mekan bilgisi alınamadı: {str(e)}")

if __name__ == "__main__":
    test_venue_websites()
    test_single_venue_website()