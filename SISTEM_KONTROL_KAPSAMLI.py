#!/usr/bin/env python3
"""
Sistem Kontrol Kapsamlı - Tüm AI sistemini detaylı kontrol eder
"""
import os
import sys
import json
import requests
import time
from pathlib import Path

def check_file_exists(file_path, description):
    """Dosya varlığını kontrol et"""
    if os.path.exists(file_path):
        size = os.path.getsize(file_path)
        print(f"✅ {description}: {file_path} ({size} bytes)")
        return True
    else:
        print(f"❌ {description}: {file_path} - DOSYA YOK!")
        return False

def check_critical_files():
    """Kritik dosyaları kontrol et"""
    print("🔍 KRİTİK DOSYALAR KONTROL EDİLİYOR...")
    print("-" * 50)
    
    files_to_check = [
        ("Backend Ana Dosya", "esref1-main/backend/real_data_backend.py"),
        ("Autonomous AI Manager", "esref1-main/backend/services/autonomous_ai_manager.py"),
        ("Autonomous AI Routes", "esref1-main/backend/routes/autonomous_ai.py"),
        ("Frontend AI Widget", "esref1-main/frontend/src/components/AutonomousAIChatWidget.jsx"),
        ("Frontend App.js", "esref1-main/frontend/src/App.js"),
        ("Backend Requirements", "esref1-main/backend/requirements.txt"),
        ("Frontend Package.json", "esref1-main/frontend/package.json"),
        ("Frontend .env", "esref1-main/frontend/.env"),
        ("Backend .env", "esref1-main/backend/.env")
    ]
    
    results = []
    for description, file_path in files_to_check:
        results.append(check_file_exists(file_path, description))
    
    return all(results)

def check_backend_imports():
    """Backend import'larını kontrol et"""
    print("\n🔍 BACKEND IMPORT'LARI KONTROL EDİLİYOR...")
    print("-" * 50)
    
    try:
        # Backend dizinini path'e ekle
        backend_path = os.path.join(os.getcwd(), "esref1-main", "backend")
        if backend_path not in sys.path:
            sys.path.insert(0, backend_path)
        
        print("1. Autonomous AI Manager import testi...")
        try:
            from services.autonomous_ai_manager import autonomous_ai, process_autonomous_conversation
            print("✅ Autonomous AI Manager başarıyla import edildi")
        except Exception as e:
            print(f"❌ Autonomous AI Manager import hatası: {e}")
            return False
        
        print("2. Autonomous AI Routes import testi...")
        try:
            from routes.autonomous_ai import router
            print("✅ Autonomous AI Routes başarıyla import edildi")
        except Exception as e:
            print(f"❌ Autonomous AI Routes import hatası: {e}")
            return False
        
        print("3. Real Data Backend import testi...")
        try:
            # Sadece import'ları test et, server'ı başlatma
            with open("esref1-main/backend/real_data_backend.py", "r", encoding="utf-8") as f:
                content = f.read()
                if "from routes.autonomous_ai import router as autonomous_ai_router" in content:
                    print("✅ Real Data Backend'de autonomous AI route import'u var")
                else:
                    print("❌ Real Data Backend'de autonomous AI route import'u YOK!")
                    return False
                
                if "app.include_router(autonomous_ai_router)" in content:
                    print("✅ Real Data Backend'de autonomous AI route include edilmiş")
                else:
                    print("❌ Real Data Backend'de autonomous AI route include EDİLMEMİŞ!")
                    return False
        except Exception as e:
            print(f"❌ Real Data Backend kontrol hatası: {e}")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Backend import kontrol genel hatası: {e}")
        return False

def check_frontend_config():
    """Frontend konfigürasyonunu kontrol et"""
    print("\n🔍 FRONTEND KONFİGÜRASYONU KONTROL EDİLİYOR...")
    print("-" * 50)
    
    try:
        # .env dosyasını kontrol et
        env_path = "esref1-main/frontend/.env"
        if os.path.exists(env_path):
            with open(env_path, "r") as f:
                env_content = f.read()
                if "REACT_APP_BACKEND_URL=http://localhost:8003" in env_content:
                    print("✅ Frontend .env dosyasında backend URL doğru")
                else:
                    print("❌ Frontend .env dosyasında backend URL yanlış veya yok!")
                    print(f"   İçerik: {env_content}")
                    return False
        else:
            print("❌ Frontend .env dosyası bulunamadı!")
            return False
        
        # App.js'de AutonomousAIChatWidget kontrol et
        app_js_path = "esref1-main/frontend/src/App.js"
        if os.path.exists(app_js_path):
            with open(app_js_path, "r", encoding="utf-8") as f:
                app_content = f.read()
                if "AutonomousAIChatWidget" in app_content:
                    print("✅ App.js'de AutonomousAIChatWidget import edilmiş")
                else:
                    print("❌ App.js'de AutonomousAIChatWidget import EDİLMEMİŞ!")
                    return False
                
                if "<AutonomousAIChatWidget" in app_content:
                    print("✅ App.js'de AutonomousAIChatWidget kullanılıyor")
                else:
                    print("❌ App.js'de AutonomousAIChatWidget KULLANILMIYOR!")
                    return False
        else:
            print("❌ App.js dosyası bulunamadı!")
            return False
        
        return True
        
    except Exception as e:
        print(f"❌ Frontend config kontrol hatası: {e}")
        return False

def test_backend_connection():
    """Backend bağlantısını test et"""
    print("\n🔍 BACKEND BAĞLANTISI TEST EDİLİYOR...")
    print("-" * 50)
    
    try:
        # Ana health check
        print("1. Ana health check...")
        response = requests.get("http://localhost:8003/health", timeout=5)
        if response.status_code == 200:
            print("✅ Backend ana health check başarılı")
        else:
            print(f"❌ Backend ana health check başarısız: {response.status_code}")
            return False
        
        # API health check
        print("2. API health check...")
        response = requests.get("http://localhost:8003/api/health", timeout=5)
        if response.status_code == 200:
            print("✅ Backend API health check başarılı")
        else:
            print(f"⚠️ Backend API health check: {response.status_code}")
        
        # Docs endpoint
        print("3. Docs endpoint...")
        response = requests.get("http://localhost:8003/docs", timeout=5)
        if response.status_code == 200:
            print("✅ Backend docs endpoint erişilebilir")
        else:
            print(f"⚠️ Backend docs endpoint: {response.status_code}")
        
        return True
        
    except requests.exceptions.ConnectionError:
        print("❌ Backend'e bağlanılamıyor - Server çalışmıyor!")
        return False
    except Exception as e:
        print(f"❌ Backend bağlantı test hatası: {e}")
        return False

def test_autonomous_ai_endpoints():
    """Autonomous AI endpoint'lerini test et"""
    print("\n🔍 AUTONOMOUS AI ENDPOINT'LERİ TEST EDİLİYOR...")
    print("-" * 50)
    
    endpoints = [
        ("Status", "/api/autonomous-ai/status"),
        ("Suggestions", "/api/autonomous-ai/suggestions"),
        ("Learning Stats", "/api/autonomous-ai/learning-stats"),
        ("Health", "/api/autonomous-ai/health")
    ]
    
    results = []
    for name, endpoint in endpoints:
        try:
            print(f"Testing {name}...")
            response = requests.get(f"http://localhost:8003{endpoint}", timeout=10)
            if response.status_code == 200:
                print(f"✅ {name} endpoint çalışıyor")
                results.append(True)
            else:
                print(f"❌ {name} endpoint hatası: {response.status_code}")
                print(f"   Response: {response.text[:200]}")
                results.append(False)
        except Exception as e:
            print(f"❌ {name} endpoint test hatası: {e}")
            results.append(False)
    
    return all(results)

def test_ai_chat_functionality():
    """AI chat fonksiyonalitesini test et"""
    print("\n🔍 AI CHAT FONKSİYONALİTESİ TEST EDİLİYOR...")
    print("-" * 50)
    
    test_questions = [
        ("Basit Test", "Hello"),
        ("Denver Barları", "What are the best bars in Denver?"),
        ("Red Rocks Etkinlikleri", "Show me tonight's events at Red Rocks")
    ]
    
    results = []
    for test_name, question in test_questions:
        try:
            print(f"Testing: {test_name} - '{question}'")
            
            payload = {
                "message": question,
                "user_context": {"location": "Denver, Colorado"},
                "learning_enabled": True
            }
            
            start_time = time.time()
            response = requests.post(
                "http://localhost:8003/api/autonomous-ai/chat",
                json=payload,
                timeout=20
            )
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                data = response.json()
                answer = data.get('answer', '')
                source = data.get('source', 'unknown')
                confidence = data.get('confidence', 'unknown')
                
                print(f"✅ {test_name} başarılı ({response_time:.2f}s)")
                print(f"   Source: {source}, Confidence: {confidence}")
                print(f"   Answer length: {len(answer)} karakter")
                
                # Red Rocks özel kontrol
                if "Red Rocks" in question:
                    if "Red Rocks" in answer and len(answer) > 200 and not answer.startswith("I'm continuously learning"):
                        print("   🎯 Red Rocks sorusu DOĞRU yanıtlandı!")
                        results.append(True)
                    else:
                        print("   ⚠️ Red Rocks sorusu generic yanıt aldı!")
                        print(f"   Answer preview: {answer[:150]}...")
                        results.append(False)
                else:
                    results.append(True)
                
            else:
                print(f"❌ {test_name} başarısız: {response.status_code}")
                print(f"   Response: {response.text[:200]}")
                results.append(False)
                
        except Exception as e:
            print(f"❌ {test_name} test hatası: {e}")
            results.append(False)
        
        print()
    
    return results

def generate_comprehensive_report(file_check, import_check, frontend_check, backend_conn, ai_endpoints, chat_results):
    """Kapsamlı rapor oluştur"""
    print("\n" + "=" * 60)
    print("📋 KAPSAMLI SİSTEM KONTROL RAPORU")
    print("=" * 60)
    
    total_tests = 6 + len(chat_results)
    passed_tests = sum([
        file_check, import_check, frontend_check, 
        backend_conn, ai_endpoints, sum(chat_results)
    ])
    
    print(f"📊 Genel Durum: {passed_tests}/{total_tests} test başarılı ({(passed_tests/total_tests)*100:.1f}%)")
    print()
    
    # Detaylı sonuçlar
    tests = [
        ("Kritik Dosyalar", file_check),
        ("Backend Import'ları", import_check),
        ("Frontend Konfigürasyonu", frontend_check),
        ("Backend Bağlantısı", backend_conn),
        ("AI Endpoint'leri", ai_endpoints),
        ("Basit Chat Testi", chat_results[0] if len(chat_results) > 0 else False),
        ("Denver Barları Testi", chat_results[1] if len(chat_results) > 1 else False),
        ("Red Rocks Testi", chat_results[2] if len(chat_results) > 2 else False)
    ]
    
    print("🔍 Detaylı Test Sonuçları:")
    for test_name, result in tests:
        status = "✅ BAŞARILI" if result else "❌ BAŞARISIZ"
        print(f"   {status} - {test_name}")
    
    # Sorun analizi
    failed_tests = [name for name, result in tests if not result]
    if failed_tests:
        print(f"\n🚨 TESPİT EDİLEN SORUNLAR:")
        for i, test_name in enumerate(failed_tests, 1):
            print(f"   {i}. {test_name}")
        
        print(f"\n🔧 ÖNERİLEN ÇÖZÜMLER:")
        
        if not file_check:
            print("• Kritik dosyalar eksik - Proje dosyalarını kontrol edin")
        
        if not import_check:
            print("• Backend import sorunları - Python path ve dependencies kontrol edin")
            print("  pip install -r esref1-main/backend/requirements.txt")
        
        if not frontend_check:
            print("• Frontend konfigürasyon sorunları - .env ve App.js kontrol edin")
        
        if not backend_conn:
            print("• Backend çalışmıyor - Başlatın:")
            print("  cd esref1-main/backend && python real_data_backend.py")
        
        if not ai_endpoints:
            print("• AI endpoint'leri çalışmıyor - Backend'de route import'larını kontrol edin")
        
        if len(chat_results) > 2 and not chat_results[2]:
            print("• Red Rocks sorusu düzgün yanıtlanmıyor - AI manager fix'lerini kontrol edin")
    
    else:
        print(f"\n🎉 TÜM TESTLER BAŞARILI!")
        print("✅ Autonomous AI sistemi tamamen çalışıyor")
        print("✅ Frontend'de brain ikonu (🧠) ile AI'ya erişebilirsiniz")
        print("✅ Red Rocks soruları doğru yanıtlanıyor")
        print("✅ Sistem production'a hazır!")

def main():
    """Ana kontrol fonksiyonu"""
    print("🔍 SİSTEM KONTROL KAPSAMLI - FULL DIAGNOSTIC")
    print("=" * 60)
    print("Bu script tüm AI sistemini detaylı olarak kontrol eder")
    print()
    
    # Test 1: Kritik dosyalar
    file_check = check_critical_files()
    
    # Test 2: Backend import'ları
    import_check = check_backend_imports()
    
    # Test 3: Frontend konfigürasyonu
    frontend_check = check_frontend_config()
    
    # Test 4: Backend bağlantısı
    backend_conn = test_backend_connection()
    
    # Test 5: AI endpoint'leri (sadece backend çalışıyorsa)
    ai_endpoints = False
    if backend_conn:
        ai_endpoints = test_autonomous_ai_endpoints()
    
    # Test 6: AI chat fonksiyonalitesi (sadece AI endpoint'leri çalışıyorsa)
    chat_results = []
    if ai_endpoints:
        chat_results = test_ai_chat_functionality()
    else:
        chat_results = [False, False, False]  # Placeholder
    
    # Kapsamlı rapor
    generate_comprehensive_report(
        file_check, import_check, frontend_check, 
        backend_conn, ai_endpoints, chat_results
    )

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️ Kontrol kullanıcı tarafından durduruldu")
    except Exception as e:
        print(f"\n❌ Kontrol script hatası: {e}")
        import traceback
        traceback.print_exc()