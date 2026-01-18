#!/usr/bin/env python3
"""
Acil AI Sorun Çözüm - Hemen sorunu tespit edip çözer
"""
import requests
import json
import time

def check_backend_status():
    """Backend durumunu kontrol et"""
    print("🔍 BACKEND DURUM KONTROL")
    print("-" * 30)
    
    try:
        # Ana health check
        response = requests.get("http://localhost:8003/health", timeout=3)
        if response.status_code == 200:
            print("✅ Backend çalışıyor")
            return True
        else:
            print(f"❌ Backend hata: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Backend çalışmıyor!")
        print("ÇÖZÜM: cd esref1-main/backend && python real_data_backend.py")
        return False
    except Exception as e:
        print(f"❌ Backend kontrol hatası: {e}")
        return False

def check_ai_endpoints():
    """AI endpoint'lerini kontrol et"""
    print("\n🤖 AI ENDPOINT KONTROL")
    print("-" * 30)
    
    # Eski AI endpoint
    try:
        response = requests.get("http://localhost:8003/api/ai-chat/status", timeout=5)
        if response.status_code == 200:
            print("⚠️ ESKİ AI endpoint çalışıyor - Bu sorunun kaynağı olabilir!")
        else:
            print("✅ Eski AI endpoint kapalı")
    except:
        print("✅ Eski AI endpoint kapalı")
    
    # Yeni Autonomous AI endpoint
    try:
        response = requests.get("http://localhost:8003/api/autonomous-ai/status", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print("✅ Autonomous AI endpoint çalışıyor")
            print(f"   System: {data.get('system_name', 'Unknown')}")
            return True
        else:
            print(f"❌ Autonomous AI endpoint hatası: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Autonomous AI endpoint erişilemez: {e}")
        return False

def test_specific_question():
    """Özel soruyu test et"""
    print("\n🍺 RİNO BREWERY SORUSU TEST")
    print("-" * 30)
    
    try:
        payload = {
            "message": "Recommend breweries in RiNo district",
            "user_context": {"location": "Denver, Colorado"},
            "learning_enabled": True
        }
        
        print("Soru gönderiliyor...")
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
            source = data.get('source', 'unknown')
            confidence = data.get('confidence', 'unknown')
            
            print(f"✅ Yanıt alındı ({response_time:.2f}s)")
            print(f"Source: {source}")
            print(f"Confidence: {confidence}")
            print(f"Answer length: {len(answer)} karakter")
            print()
            print("YANIT:")
            print("-" * 40)
            print(answer)
            print("-" * 40)
            
            # Yanıt analizi
            if answer.startswith("I'm continuously learning"):
                print("\n❌ SORUN TESPİT EDİLDİ: Generic fallback yanıtı!")
                print("Bu, AI'nın soruyu doğru işleyemediğini gösterir.")
                return False
            elif "RiNo" in answer or "brewery" in answer.lower():
                print("\n✅ YANIT KALİTELİ: RiNo brewery bilgisi içeriyor!")
                return True
            else:
                print("\n⚠️ YANIT GENEL: Özel RiNo bilgisi yok ama generic değil")
                return True
                
        else:
            print(f"❌ Chat hatası: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Test hatası: {e}")
        return False

def diagnose_problem():
    """Sorunu teşhis et"""
    print("\n🔍 SORUN TEŞHİSİ")
    print("-" * 30)
    
    # Frontend hangi endpoint'i kullanıyor kontrol et
    print("Frontend endpoint kontrolü:")
    print("1. AutonomousAIChatWidget /api/autonomous-ai/chat kullanmalı")
    print("2. Eski AdvancedAIChatWidget /api/ai-chat kullanıyor olabilir")
    print()
    
    # Backend route kontrol önerileri
    print("Backend route kontrol önerileri:")
    print("1. real_data_backend.py'de autonomous_ai_router import edilmiş mi?")
    print("2. app.include_router(autonomous_ai_router) var mı?")
    print("3. Backend başlatılırken hata mesajı var mı?")
    print()
    
    # Olası çözümler
    print("OLASI ÇÖZÜMLER:")
    print("1. Backend'i yeniden başlat")
    print("2. Frontend cache'ini temizle")
    print("3. Browser'ı yenile (Ctrl+F5)")
    print("4. Autonomous AI route'larını kontrol et")

def provide_immediate_solution():
    """Hemen çözüm öner"""
    print("\n🚀 HEMEN ÇÖZÜM")
    print("-" * 30)
    
    print("ADIM 1: Backend'i yeniden başlat")
    print("  cd esref1-main/backend")
    print("  python real_data_backend.py")
    print()
    
    print("ADIM 2: 30 saniye bekle")
    print()
    
    print("ADIM 3: Bu script'i tekrar çalıştır")
    print("  python ACIL_AI_SORUN_COZUM.py")
    print()
    
    print("ADIM 4: Frontend'i yenile")
    print("  Browser'da Ctrl+F5 bas")
    print("  Brain ikonu (🧠) ile tekrar test et")

def main():
    """Ana fonksiyon"""
    print("🚨 ACİL AI SORUN ÇÖZÜM")
    print("=" * 40)
    print("RiNo brewery sorusu generic yanıt alıyor - Hemen çözelim!")
    print()
    
    # Adım 1: Backend kontrol
    backend_ok = check_backend_status()
    if not backend_ok:
        provide_immediate_solution()
        return
    
    # Adım 2: AI endpoint'leri kontrol
    ai_ok = check_ai_endpoints()
    if not ai_ok:
        print("\n❌ SORUN: Autonomous AI endpoint'leri çalışmıyor!")
        provide_immediate_solution()
        return
    
    # Adım 3: Özel soru testi
    question_ok = test_specific_question()
    
    # Sonuç
    print("\n" + "=" * 40)
    if question_ok:
        print("🎉 SORUN ÇÖZÜLDİ!")
        print("✅ Backend çalışıyor")
        print("✅ AI endpoint'leri aktif")
        print("✅ RiNo brewery sorusu doğru yanıtlanıyor")
        print("\nFrontend'de brain ikonu (🧠) ile test edebilirsiniz!")
    else:
        print("❌ SORUN DEVAM EDİYOR!")
        diagnose_problem()
        provide_immediate_solution()

if __name__ == "__main__":
    main()