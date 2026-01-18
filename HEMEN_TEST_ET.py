#!/usr/bin/env python3
"""
Hemen Test Et - Şu anda backend'in durumunu kontrol et
"""
import requests
import json

def quick_test():
    """Hızlı test"""
    print("🔍 HEMEN TEST - BACKEND DURUMU")
    print("=" * 40)
    
    # Test 1: Backend çalışıyor mu?
    print("1. Backend kontrol...")
    try:
        response = requests.get("http://localhost:8003/health", timeout=3)
        if response.status_code == 200:
            print("✅ Backend çalışıyor")
        else:
            print(f"❌ Backend hata: {response.status_code}")
            return False
    except:
        print("❌ Backend çalışmıyor - Port 8003'te hiçbir şey yok!")
        print("\nÇÖZÜM:")
        print("cd esref1-main/backend")
        print("python real_data_backend.py")
        return False
    
    # Test 2: Autonomous AI endpoint var mı?
    print("2. Autonomous AI endpoint kontrol...")
    try:
        response = requests.get("http://localhost:8003/api/autonomous-ai/status", timeout=5)
        if response.status_code == 200:
            print("✅ Autonomous AI endpoint çalışıyor")
        else:
            print(f"❌ Autonomous AI endpoint hatası: {response.status_code}")
            print("Backend'de route import sorunu olabilir!")
            return False
    except Exception as e:
        print(f"❌ Autonomous AI endpoint erişilemez: {e}")
        print("Route'lar yüklenmemiş!")
        return False
    
    # Test 3: RiNo brewery sorusu
    print("3. RiNo brewery sorusu test...")
    try:
        payload = {
            "message": "Recommend breweries in RiNo district",
            "user_context": {"location": "Denver, Colorado"},
            "learning_enabled": True
        }
        
        response = requests.post(
            "http://localhost:8003/api/autonomous-ai/chat",
            json=payload,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            answer = data.get('answer', '')
            
            if answer.startswith("I'm continuously learning"):
                print("❌ SORUN: Generic fallback yanıtı alındı!")
                print("AI intent'i doğru algılamıyor")
                return False
            else:
                print("✅ Özelleştirilmiş yanıt alındı!")
                print(f"Answer preview: {answer[:100]}...")
                return True
        else:
            print(f"❌ Chat hatası: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Chat test hatası: {e}")
        return False

def main():
    """Ana fonksiyon"""
    success = quick_test()
    
    print("\n" + "=" * 40)
    if success:
        print("🎉 HER ŞEY ÇALIŞIYOR!")
        print("Sorun frontend cache'inde olabilir.")
        print("\nÇÖZÜM:")
        print("1. Browser'da Ctrl+F5 bas (hard refresh)")
        print("2. Brain ikonu (🧠) ile tekrar test et")
    else:
        print("❌ SORUN TESPİT EDİLDİ!")
        print("\nHEMEN ÇÖZÜM:")
        print("1. Backend'i başlat:")
        print("   cd esref1-main/backend")
        print("   python real_data_backend.py")
        print("2. 30 saniye bekle")
        print("3. Bu script'i tekrar çalıştır")

if __name__ == "__main__":
    main()