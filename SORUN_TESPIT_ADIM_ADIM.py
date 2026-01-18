#!/usr/bin/env python3
"""
Sorun Tespit Adım Adım - Her adımı tek tek kontrol eder
"""
import os
import sys
import requests
import json

def step1_check_files():
    """Adım 1: Dosyaların varlığını kontrol et"""
    print("🔍 ADIM 1: DOSYA VARLIĞI KONTROL")
    print("-" * 40)
    
    critical_files = [
        "esref1-main/backend/real_data_backend.py",
        "esref1-main/backend/services/autonomous_ai_manager.py", 
        "esref1-main/backend/routes/autonomous_ai.py",
        "esref1-main/frontend/src/components/AutonomousAIChatWidget.jsx"
    ]
    
    all_exist = True
    for file_path in critical_files:
        if os.path.exists(file_path):
            print(f"✅ {file_path}")
        else:
            print(f"❌ {file_path} - DOSYA YOK!")
            all_exist = False
    
    return all_exist

def step2_check_backend_running():
    """Adım 2: Backend'in çalışıp çalışmadığını kontrol et"""
    print("\n🔍 ADIM 2: BACKEND ÇALIŞIYOR MU?")
    print("-" * 40)
    
    try:
        response = requests.get("http://localhost:8003/health", timeout=3)
        if response.status_code == 200:
            print("✅ Backend çalışıyor (port 8003)")
            return True
        else:
            print(f"⚠️ Backend yanıt verdi ama durum: {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Backend çalışmıyor - Port 8003'te hiçbir şey yok")
        print("   Çözüm: cd esref1-main/backend && python real_data_backend.py")
        return False
    except Exception as e:
        print(f"❌ Backend kontrol hatası: {e}")
        return False

def step3_check_ai_routes():
    """Adım 3: AI route'larının yüklenip yüklenmediğini kontrol et"""
    print("\n🔍 ADIM 3: AI ROUTE'LARI YÜKLÜ MÜ?")
    print("-" * 40)
    
    # Eski AI route'u kontrol et
    try:
        response = requests.get("http://localhost:8003/api/ai-chat/status", timeout=5)
        if response.status_code == 200:
            print("✅ Eski AI Chat route'u çalışıyor")
        else:
            print(f"⚠️ Eski AI Chat route'u: {response.status_code}")
    except:
        print("❌ Eski AI Chat route'u erişilemez")
    
    # Yeni Autonomous AI route'u kontrol et
    try:
        response = requests.get("http://localhost:8003/api/autonomous-ai/status", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print("✅ Autonomous AI route'u çalışıyor")
            print(f"   System: {data.get('system_name', 'Unknown')}")
            return True
        else:
            print(f"❌ Autonomous AI route'u hatası: {response.status_code}")
            print(f"   Response: {response.text[:200]}")
            return False
    except Exception as e:
        print(f"❌ Autonomous AI route'u test hatası: {e}")
        return False

def step4_test_simple_chat():
    """Adım 4: Basit chat testi"""
    print("\n🔍 ADIM 4: BASİT CHAT TESTİ")
    print("-" * 40)
    
    try:
        payload = {
            "message": "Hello",
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
            print("✅ Basit chat çalışıyor")
            print(f"   Source: {data.get('source', 'unknown')}")
            print(f"   Confidence: {data.get('confidence', 'unknown')}")
            print(f"   Answer: {answer[:100]}...")
            return True
        else:
            print(f"❌ Chat hatası: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Chat test hatası: {e}")
        return False

def step5_test_red_rocks():
    """Adım 5: Red Rocks özel testi"""
    print("\n🔍 ADIM 5: RED ROCKS ÖZELLEŞTİRİLMİŞ TEST")
    print("-" * 40)
    
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
            source = data.get('source', 'unknown')
            
            print(f"✅ Red Rocks sorusu yanıtlandı")
            print(f"   Source: {source}")
            print(f"   Answer length: {len(answer)} karakter")
            
            # Yanıt kalitesi analizi
            if answer.startswith("I'm continuously learning"):
                print("❌ SORUN: Generic fallback yanıtı alındı!")
                print("   Bu, AI'nın intent'i doğru algılamadığını gösterir")
                return False
            elif "Red Rocks" in answer and len(answer) > 200:
                print("✅ MÜKEMMEL: Özelleştirilmiş Red Rocks yanıtı!")
                return True
            elif "Red Rocks" in answer:
                print("⚠️ KISMEN İYİ: Red Rocks bahsedildi ama kısa yanıt")
                return True
            else:
                print("❌ SORUN: Red Rocks hakkında bilgi yok")
                return False
        else:
            print(f"❌ Red Rocks test hatası: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Red Rocks test hatası: {e}")
        return False

def step6_analyze_problem():
    """Adım 6: Sorun analizi"""
    print("\n🔍 ADIM 6: SORUN ANALİZİ")
    print("-" * 40)
    
    # Backend loglarını kontrol etmeye çalış
    print("Backend log analizi (manuel kontrol gerekli):")
    print("1. Backend çalışırken console'da hata mesajları var mı?")
    print("2. 'ModuleNotFoundError' veya 'ImportError' var mı?")
    print("3. 'autonomous_ai_manager' import edilirken hata var mı?")
    print("4. Route'lar yüklenirken hata var mı?")
    
    # Frontend kontrol önerileri
    print("\nFrontend kontrol önerileri:")
    print("1. Browser console'da JavaScript hatası var mı?")
    print("2. Network tab'da API istekleri gidiyor mu?")
    print("3. Brain ikonu (🧠) görünüyor mu?")

def main():
    """Ana test fonksiyonu"""
    print("🔍 SORUN TESPİT - ADIM ADIM ANALİZ")
    print("=" * 50)
    print("Her adımı tek tek kontrol ederek sorunu bulacağız")
    print()
    
    # Adım 1: Dosya varlığı
    step1_ok = step1_check_files()
    if not step1_ok:
        print("\n❌ SORUN BULUNDU: Kritik dosyalar eksik!")
        print("Çözüm: Proje dosyalarının tam olduğundan emin olun")
        return
    
    # Adım 2: Backend çalışıyor mu?
    step2_ok = step2_check_backend_running()
    if not step2_ok:
        print("\n❌ SORUN BULUNDU: Backend çalışmıyor!")
        print("Çözüm: Backend'i başlatın:")
        print("  cd esref1-main/backend")
        print("  python real_data_backend.py")
        return
    
    # Adım 3: AI route'ları yüklü mü?
    step3_ok = step3_check_ai_routes()
    if not step3_ok:
        print("\n❌ SORUN BULUNDU: Autonomous AI route'ları yüklenmemiş!")
        print("Çözüm: Backend'de import hatası olabilir")
        print("  1. Backend'i yeniden başlatın")
        print("  2. Console'da hata mesajlarını kontrol edin")
        print("  3. pip install -r requirements.txt")
        return
    
    # Adım 4: Basit chat çalışıyor mu?
    step4_ok = step4_test_simple_chat()
    if not step4_ok:
        print("\n❌ SORUN BULUNDU: AI chat çalışmıyor!")
        print("Çözüm: AI manager'da kod hatası olabilir")
        return
    
    # Adım 5: Red Rocks özel testi
    step5_ok = step5_test_red_rocks()
    if not step5_ok:
        print("\n❌ SORUN BULUNDU: Red Rocks sorusu düzgün yanıtlanmıyor!")
        print("Çözüm: AI manager'daki fix'ler uygulanmamış olabilir")
        print("  1. autonomous_ai_manager.py'deki güncellemeleri kontrol edin")
        print("  2. Backend'i yeniden başlatın")
        return
    
    # Tüm testler başarılı
    print("\n🎉 TÜM ADIMLAR BAŞARILI!")
    print("✅ Dosyalar mevcut")
    print("✅ Backend çalışıyor") 
    print("✅ AI route'ları yüklü")
    print("✅ Chat fonksiyonu çalışıyor")
    print("✅ Red Rocks soruları doğru yanıtlanıyor")
    print("\n💡 Sistem tamamen çalışıyor - Frontend'de test edebilirsiniz!")
    
    # Son kontrol önerisi
    step6_analyze_problem()

if __name__ == "__main__":
    main()