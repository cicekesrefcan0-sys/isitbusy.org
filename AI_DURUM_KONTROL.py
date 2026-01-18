#!/usr/bin/env python3
"""
AI Durum Kontrol - Autonomous AI sisteminin çalışıp çalışmadığını kontrol eder
"""
import requests
import json
import time

def test_backend_connection():
    """Backend bağlantısını test et"""
    print("🔍 Backend bağlantısı kontrol ediliyor...")
    
    try:
        # Ana backend health check
        response = requests.get("http://localhost:8003/health", timeout=5)
        if response.status_code == 200:
            print("✅ Backend çalışıyor (port 8003)")
            return True
        else:
            print(f"❌ Backend yanıt verdi ama hata: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Backend'e bağlanılamıyor - Server çalışmıyor olabilir")
        return False
    except Exception as e:
        print(f"❌ Backend test hatası: {e}")
        return False

def test_autonomous_ai_routes():
    """Autonomous AI route'larını test et"""
    print("\n🤖 Autonomous AI route'ları kontrol ediliyor...")
    
    # Test 1: Status endpoint
    try:
        response = requests.get("http://localhost:8003/api/autonomous-ai/status", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("✅ Autonomous AI status endpoint çalışıyor")
            print(f"   System: {data.get('system_name', 'Bilinmiyor')}")
            print(f"   Version: {data.get('version', 'Bilinmiyor')}")
            print(f"   Status: {data.get('status', 'Bilinmiyor')}")
            return True
        else:
            print(f"❌ Status endpoint hatası: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Status endpoint test hatası: {e}")
        return False

def test_ai_chat_endpoint():
    """AI chat endpoint'ini test et"""
    print("\n💬 AI Chat endpoint kontrol ediliyor...")
    
    try:
        payload = {
            "message": "Test mesajı",
            "user_context": {"location": "Denver, Colorado"},
            "learning_enabled": True
        }
        
        response = requests.post(
            "http://localhost:8003/api/autonomous-ai/chat",
            json=payload,
            timeout=15
        )
        
        if response.status_code == 200:
            data = response.json()
            print("✅ AI Chat endpoint çalışıyor")
            print(f"   Answer preview: {data.get('answer', '')[:100]}...")
            print(f"   Source: {data.get('source', 'Bilinmiyor')}")
            print(f"   Confidence: {data.get('confidence', 'Bilinmiyor')}")
            return True
        else:
            print(f"❌ Chat endpoint hatası: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Chat endpoint test hatası: {e}")
        return False

def test_red_rocks_question():
    """Red Rocks sorusunu özellikle test et"""
    print("\n🎵 Red Rocks sorusu test ediliyor...")
    
    try:
        payload = {
            "message": "Show me tonight's events at Red Rocks",
            "user_context": {"location": "Denver, Colorado"},
            "learning_enabled": True
        }
        
        start_time = time.time()
        response = requests.post(
            "http://localhost:8003/api/autonomous-ai/chat",
            json=payload,
            timeout=15
        )
        response_time = time.time() - start_time
        
        if response.status_code == 200:
            data = response.json()
            answer = data.get('answer', '')
            
            print("✅ Red Rocks sorusu yanıtlandı")
            print(f"   Response time: {response_time:.2f}s")
            print(f"   Source: {data.get('source', 'Bilinmiyor')}")
            print(f"   Confidence: {data.get('confidence', 'Bilinmiyor')}")
            print(f"   Learning applied: {data.get('learning_applied', False)}")
            print(f"\n📝 Yanıt:")
            print("-" * 50)
            print(answer)
            print("-" * 50)
            
            # Yanıtın kalitesini kontrol et
            if "Red Rocks" in answer and len(answer) > 100:
                print("\n✅ Yanıt kaliteli görünüyor - Red Rocks bilgisi içeriyor")
                return True
            else:
                print("\n⚠️ Yanıt generic görünüyor - Red Rocks özel bilgisi yok")
                return False
        else:
            print(f"❌ Red Rocks sorusu hatası: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Red Rocks test hatası: {e}")
        return False

def check_frontend_connection():
    """Frontend'in backend'e bağlanıp bağlanmadığını kontrol et"""
    print("\n🌐 Frontend bağlantısı kontrol ediliyor...")
    
    try:
        # Frontend genelde 3000 portunda çalışır
        response = requests.get("http://localhost:3000", timeout=5)
        if response.status_code == 200:
            print("✅ Frontend çalışıyor (port 3000)")
            return True
        else:
            print(f"⚠️ Frontend yanıt verdi ama durum: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Frontend'e bağlanılamıyor - npm start yapılmış mı?")
        return False
    except Exception as e:
        print(f"⚠️ Frontend test hatası: {e}")
        return False

def main():
    """Ana kontrol fonksiyonu"""
    print("🔍 AI DURUM KONTROL - KAPSAMLI TEST")
    print("=" * 60)
    print("Bu script autonomous AI sisteminin çalışıp çalışmadığını kontrol eder")
    print()
    
    results = []
    
    # Test 1: Backend bağlantısı
    results.append(("Backend Connection", test_backend_connection()))
    
    # Test 2: Autonomous AI routes
    results.append(("Autonomous AI Routes", test_autonomous_ai_routes()))
    
    # Test 3: AI Chat endpoint
    results.append(("AI Chat Endpoint", test_ai_chat_endpoint()))
    
    # Test 4: Red Rocks özel sorusu
    results.append(("Red Rocks Question", test_red_rocks_question()))
    
    # Test 5: Frontend bağlantısı
    results.append(("Frontend Connection", check_frontend_connection()))
    
    # Sonuçları özetle
    print("\n" + "=" * 60)
    print("📋 TEST SONUÇLARI")
    print("=" * 60)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ BAŞARILI" if result else "❌ BAŞARISIZ"
        print(f"{status} - {test_name}")
        if result:
            passed += 1
    
    print(f"\n📊 Özet: {passed}/{total} test başarılı ({(passed/total)*100:.1f}%)")
    
    # Sorun giderme önerileri
    if passed < total:
        print(f"\n🔧 SORUN GİDERME ÖNERİLERİ:")
        print("-" * 40)
        
        if not results[0][1]:  # Backend connection failed
            print("1. Backend'i başlatın:")
            print("   cd backend")
            print("   python real_data_backend.py")
            print()
        
        if not results[1][1] or not results[2][1]:  # AI routes failed
            print("2. Autonomous AI route'ları kontrol edin:")
            print("   - backend/routes/autonomous_ai.py dosyası var mı?")
            print("   - real_data_backend.py'de import edilmiş mi?")
            print()
        
        if not results[3][1]:  # Red Rocks question failed
            print("3. AI yanıt kalitesi düşük:")
            print("   - Backend loglarını kontrol edin")
            print("   - autonomous_ai_manager.py'deki fix'ler uygulandı mı?")
            print()
        
        if not results[4][1]:  # Frontend connection failed
            print("4. Frontend'i başlatın:")
            print("   cd frontend")
            print("   npm start")
            print()
    else:
        print("\n🎉 TÜM TESTLER BAŞARILI!")
        print("Autonomous AI sistemi düzgün çalışıyor.")
        print("Frontend'de brain ikonu (🧠) ile AI'ya erişebilirsiniz.")

if __name__ == "__main__":
    main()