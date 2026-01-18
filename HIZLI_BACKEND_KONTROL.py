#!/usr/bin/env python3
"""
Hızlı Backend Kontrol - Backend'in çalışıp çalışmadığını hızlıca kontrol eder
"""
import requests
import json
import time

def quick_backend_check():
    """Hızlı backend kontrolü"""
    print("🔍 HIZLI BACKEND KONTROL")
    print("=" * 40)
    
    # Test 1: Backend çalışıyor mu?
    print("1. Backend bağlantısı kontrol ediliyor...")
    try:
        response = requests.get("http://localhost:8003/health", timeout=3)
        if response.status_code == 200:
            print("✅ Backend çalışıyor")
        else:
            print(f"⚠️ Backend yanıt verdi ama durum: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Backend çalışmıyor - Port 8003'te server yok")
        return False
    except Exception as e:
        print(f"❌ Backend kontrol hatası: {e}")
        return False
    
    # Test 2: Autonomous AI endpoint'i var mı?
    print("2. Autonomous AI endpoint kontrol ediliyor...")
    try:
        response = requests.get("http://localhost:8003/api/autonomous-ai/status", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Autonomous AI çalışıyor - {data.get('system_name', 'Unknown')}")
        else:
            print(f"❌ Autonomous AI endpoint hatası: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Autonomous AI endpoint test hatası: {e}")
        return False
    
    # Test 3: Basit AI chat testi
    print("3. Basit AI chat testi...")
    try:
        payload = {
            "message": "Hello test",
            "user_context": {"location": "Denver, Colorado"},
            "learning_enabled": True
        }
        
        start_time = time.time()
        response = requests.post(
            "http://localhost:8003/api/autonomous-ai/chat",
            json=payload,
            timeout=10
        )
        response_time = time.time() - start_time
        
        if response.status_code == 200:
            data = response.json()
            answer = data.get('answer', '')
            print(f"✅ AI chat çalışıyor ({response_time:.2f}s)")
            print(f"   Source: {data.get('source', 'unknown')}")
            print(f"   Answer length: {len(answer)} karakter")
        else:
            print(f"❌ AI chat hatası: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ AI chat test hatası: {e}")
        return False
    
    # Test 4: Red Rocks özel testi
    print("4. Red Rocks özel testi...")
    try:
        payload = {
            "message": "Show me tonight's events at Red Rocks",
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
            answer = data.get('answer', '')
            
            # Red Rocks yanıt kalitesi kontrolü
            if "Red Rocks" in answer and len(answer) > 200 and not answer.startswith("I'm continuously learning"):
                print("✅ Red Rocks sorusu DOĞRU yanıtlandı!")
                print(f"   Answer preview: {answer[:100]}...")
                return True
            else:
                print("❌ Red Rocks sorusu generic yanıt aldı!")
                print(f"   Answer: {answer[:150]}...")
                return False
        else:
            print(f"❌ Red Rocks test hatası: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Red Rocks test hatası: {e}")
        return False

def main():
    """Ana fonksiyon"""
    success = quick_backend_check()
    
    print("\n" + "=" * 40)
    if success:
        print("🎉 TÜM TESTLER BAŞARILI!")
        print("✅ Backend çalışıyor")
        print("✅ Autonomous AI aktif")
        print("✅ Red Rocks soruları doğru yanıtlanıyor")
        print("\n💡 Frontend'de brain ikonu (🧠) ile test edebilirsiniz")
    else:
        print("❌ SORUNLAR TESPİT EDİLDİ!")
        print("\n🔧 Çözüm önerileri:")
        print("1. Backend'i başlatın:")
        print("   cd esref1-main/backend")
        print("   python real_data_backend.py")
        print()
        print("2. Eğer hata alıyorsanız:")
        print("   pip install -r requirements.txt")
        print()
        print("3. Detaylı kontrol için:")
        print("   python SISTEM_KONTROL_KAPSAMLI.py")

if __name__ == "__main__":
    main()