"""
User Experience Test - Gerçek kullanıcı senaryolarını test eder
Uygulamanın tüm özelliklerini kullanıcı gözünden test eder
"""
import requests
import json
import time
from datetime import datetime

class UserExperienceTest:
    def __init__(self):
        self.frontend_url = "http://localhost:3000"
        self.backend_url = "http://localhost:8002"
        self.test_results = []
        
    def log_test(self, test_name, success, details="", response_time=0):
        """Test sonucunu logla"""
        status = "✅ PASS" if success else "❌ FAIL"
        self.test_results.append({
            "test": test_name,
            "status": status,
            "details": details,
            "response_time": f"{response_time:.2f}s" if response_time > 0 else "N/A"
        })
        print(f"{test_name:<35} | {status:<8} | {details}")
        
    def test_user_journey_1_discover_venues(self):
        """Senaryo 1: Kullanıcı mekanları keşfediyor"""
        print("\n🎯 SENARYO 1: MEKAN KEŞFİ")
        print("=" * 70)
        
        # 1. Ana sayfaya giriş
        try:
            start_time = time.time()
            response = requests.get(self.frontend_url, timeout=10)
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                self.log_test("Ana sayfaya erişim", True, "Frontend yüklendi", response_time)
            else:
                self.log_test("Ana sayfaya erişim", False, f"HTTP {response.status_code}")
                return False
        except Exception as e:
            self.log_test("Ana sayfaya erişim", False, f"Bağlantı hatası: {str(e)[:30]}")
            return False
            
        # 2. Mekan listesini çekme
        try:
            start_time = time.time()
            response = requests.get(f"{self.backend_url}/api/venues", timeout=5)
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                data = response.json()
                venue_count = len(data.get('data', []))
                self.log_test("Mekan listesi yükleme", True, f"{venue_count} mekan bulundu", response_time)
                
                # İlk mekanı al
                if venue_count > 0:
                    first_venue = data['data'][0]
                    venue_id = first_venue.get('id')
                    venue_name = first_venue.get('name', 'Unknown')
                    
                    # 3. Tek mekan detayını çekme
                    try:
                        start_time = time.time()
                        detail_response = requests.get(f"{self.backend_url}/api/venues/{venue_id}", timeout=5)
                        response_time = time.time() - start_time
                        
                        if detail_response.status_code == 200:
                            venue_detail = detail_response.json()
                            self.log_test("Mekan detayı yükleme", True, f"{venue_name} detayları", response_time)
                            return True
                        else:
                            self.log_test("Mekan detayı yükleme", False, f"HTTP {detail_response.status_code}")
                    except Exception as e:
                        self.log_test("Mekan detayı yükleme", False, f"Hata: {str(e)[:30]}")
                else:
                    self.log_test("Mekan detayı yükleme", False, "Hiç mekan bulunamadı")
            else:
                self.log_test("Mekan listesi yükleme", False, f"HTTP {response.status_code}")
        except Exception as e:
            self.log_test("Mekan listesi yükleme", False, f"Hata: {str(e)[:30]}")
            
        return False
        
    def test_user_journey_2_check_events(self):
        """Senaryo 2: Kullanıcı etkinlikleri kontrol ediyor"""
        print("\n🎉 SENARYO 2: ETKİNLİK KONTROLÜ")
        print("=" * 70)
        
        # 1. Eventbrite etkinliklerini çekme
        try:
            start_time = time.time()
            response = requests.get(f"{self.backend_url}/api/eventbrite/events", timeout=5)
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                data = response.json()
                event_count = len(data.get('events', []))
                self.log_test("Etkinlik listesi", True, f"{event_count} etkinlik bulundu", response_time)
                
                # İlk etkinliğin detaylarını kontrol et
                if event_count > 0:
                    first_event = data['events'][0]
                    event_name = first_event.get('name', 'Unknown')
                    venue_name = first_event.get('venue_name', 'Unknown')
                    self.log_test("Etkinlik detayları", True, f"{event_name} @ {venue_name}")
                else:
                    self.log_test("Etkinlik detayları", False, "Hiç etkinlik yok")
            else:
                self.log_test("Etkinlik listesi", False, f"HTTP {response.status_code}")
        except Exception as e:
            self.log_test("Etkinlik listesi", False, f"Hata: {str(e)[:30]}")
            
        # 2. After party etkinliklerini çekme
        try:
            start_time = time.time()
            response = requests.get(f"{self.backend_url}/api/eventbrite/after-parties", timeout=5)
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                data = response.json()
                party_count = len(data.get('events', []))
                self.log_test("After party listesi", True, f"{party_count} after party bulundu", response_time)
            else:
                self.log_test("After party listesi", False, f"HTTP {response.status_code}")
        except Exception as e:
            self.log_test("After party listesi", False, f"Hata: {str(e)[:30]}")
            
    def test_user_journey_3_trending_news(self):
        """Senaryo 3: Kullanıcı trending mekanları ve haberleri kontrol ediyor"""
        print("\n📈 SENARYO 3: TRENDİNG VE HABERLER")
        print("=" * 70)
        
        # 1. Trending mekanları çekme
        try:
            start_time = time.time()
            response = requests.get(f"{self.backend_url}/api/trending/venues", timeout=5)
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                data = response.json()
                trending_count = len(data.get('data', []))
                self.log_test("Trending mekanlar", True, f"{trending_count} trending mekan", response_time)
            else:
                self.log_test("Trending mekanlar", False, f"HTTP {response.status_code}")
        except Exception as e:
            self.log_test("Trending mekanlar", False, f"Hata: {str(e)[:30]}")
            
        # 2. Haberleri çekme
        try:
            start_time = time.time()
            response = requests.get(f"{self.backend_url}/api/news", timeout=5)
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                data = response.json()
                news_count = len(data.get('data', []))
                self.log_test("Haber listesi", True, f"{news_count} haber bulundu", response_time)
                
                if news_count > 0:
                    first_news = data['data'][0]
                    news_title = first_news.get('title', 'Unknown')
                    self.log_test("Haber detayları", True, f"'{news_title[:30]}...'")
            else:
                self.log_test("Haber listesi", False, f"HTTP {response.status_code}")
        except Exception as e:
            self.log_test("Haber listesi", False, f"Hata: {str(e)[:30]}")
            
    def test_user_journey_4_search_analytics(self):
        """Senaryo 4: Kullanıcı arama yapıyor ve analytics kontrol ediyor"""
        print("\n🔍 SENARYO 4: ARAMA VE ANALİTİKS")
        print("=" * 70)
        
        # 1. Arama fonksiyonu
        try:
            start_time = time.time()
            response = requests.get(f"{self.backend_url}/api/search", timeout=5)
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                data = response.json()
                search_results = len(data.get('results', []))
                self.log_test("Arama fonksiyonu", True, f"{search_results} sonuç döndü", response_time)
            else:
                self.log_test("Arama fonksiyonu", False, f"HTTP {response.status_code}")
        except Exception as e:
            self.log_test("Arama fonksiyonu", False, f"Hata: {str(e)[:30]}")
            
        # 2. Analytics verisi
        try:
            start_time = time.time()
            response = requests.get(f"{self.backend_url}/api/analytics", timeout=5)
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                data = response.json()
                self.log_test("Analytics verisi", True, "Analytics data mevcut", response_time)
            else:
                self.log_test("Analytics verisi", False, f"HTTP {response.status_code}")
        except Exception as e:
            self.log_test("Analytics verisi", False, f"Hata: {str(e)[:30]}")
            
    def test_performance_metrics(self):
        """Performans metriklerini test et"""
        print("\n⚡ PERFORMANS METRİKLERİ")
        print("=" * 70)
        
        # API response time testi
        api_endpoints = [
            ("/api/health", "Health Check"),
            ("/api/venues", "Venues API"),
            ("/api/eventbrite/events", "Events API"),
            ("/api/news", "News API")
        ]
        
        total_response_time = 0
        successful_calls = 0
        
        for endpoint, name in api_endpoints:
            try:
                start_time = time.time()
                response = requests.get(f"{self.backend_url}{endpoint}", timeout=5)
                response_time = time.time() - start_time
                
                if response.status_code == 200:
                    total_response_time += response_time
                    successful_calls += 1
                    
                    # Performans değerlendirmesi
                    if response_time < 1.0:
                        perf_status = "Mükemmel"
                    elif response_time < 2.0:
                        perf_status = "İyi"
                    elif response_time < 3.0:
                        perf_status = "Orta"
                    else:
                        perf_status = "Yavaş"
                        
                    self.log_test(f"{name} performans", True, f"{perf_status} ({response_time:.2f}s)", response_time)
                else:
                    self.log_test(f"{name} performans", False, f"HTTP {response.status_code}")
            except Exception as e:
                self.log_test(f"{name} performans", False, f"Timeout/Error")
                
        # Ortalama response time
        if successful_calls > 0:
            avg_response_time = total_response_time / successful_calls
            if avg_response_time < 1.0:
                self.log_test("Ortalama API hızı", True, f"Mükemmel ({avg_response_time:.2f}s)")
            elif avg_response_time < 2.0:
                self.log_test("Ortalama API hızı", True, f"İyi ({avg_response_time:.2f}s)")
            else:
                self.log_test("Ortalama API hızı", False, f"Yavaş ({avg_response_time:.2f}s)")
                
    def run_all_tests(self):
        """Tüm testleri çalıştır"""
        print("=" * 100)
        print("🧪 KULLANICI DENEYİMİ TESTİ")
        print("=" * 100)
        print(f"Test Zamanı: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Frontend URL: {self.frontend_url}")
        print(f"Backend URL: {self.backend_url}")
        print("=" * 100)
        
        # Testleri çalıştır
        self.test_user_journey_1_discover_venues()
        self.test_user_journey_2_check_events()
        self.test_user_journey_3_trending_news()
        self.test_user_journey_4_search_analytics()
        self.test_performance_metrics()
        
        # Sonuçları özetle
        self.print_summary()
        
    def print_summary(self):
        """Test sonuçlarını özetle"""
        print("\n" + "=" * 100)
        print("📊 TEST SONUÇLARI ÖZETİ")
        print("=" * 100)
        
        total_tests = len(self.test_results)
        passed_tests = len([r for r in self.test_results if "✅ PASS" in r["status"]])
        failed_tests = total_tests - passed_tests
        success_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
        
        print(f"Toplam Test:           {total_tests}")
        print(f"Başarılı:              {passed_tests}")
        print(f"Başarısız:             {failed_tests}")
        print(f"Başarı Oranı:          {success_rate:.1f}%")
        
        # Başarısız testleri listele
        if failed_tests > 0:
            print(f"\n❌ BAŞARISIZ TESTLER:")
            for result in self.test_results:
                if "❌ FAIL" in result["status"]:
                    print(f"   • {result['test']}: {result['details']}")
        
        # Genel değerlendirme
        print(f"\n🎯 GENEL DEĞERLENDİRME:")
        if success_rate >= 90:
            print("🎉 MÜKEMMEL! Uygulama kullanıcı deneyimi açısından hazır!")
            print("✅ Tüm temel özellikler çalışıyor")
            print("✅ Performans kabul edilebilir seviyede")
            print("✅ Kullanıcılar uygulamayı sorunsuz kullanabilir")
        elif success_rate >= 75:
            print("✅ İYİ! Uygulama çoğunlukla çalışıyor")
            print("⚠️ Bazı küçük sorunlar var ama kritik değil")
            print("✅ Temel kullanıcı deneyimi sağlanıyor")
        elif success_rate >= 50:
            print("⚠️ ORTA! Uygulama temel seviyede çalışıyor")
            print("🔧 Birkaç önemli sorun var")
            print("⚠️ Kullanıcı deneyimi etkilenebilir")
        else:
            print("❌ ZAYIF! Uygulama ciddi sorunlar yaşıyor")
            print("🚨 Çok sayıda kritik sorun var")
            print("❌ Kullanıcı deneyimi kabul edilemez")
            
        print("=" * 100)

if __name__ == "__main__":
    tester = UserExperienceTest()
    tester.run_all_tests()