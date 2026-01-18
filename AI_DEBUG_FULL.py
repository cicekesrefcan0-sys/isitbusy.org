#!/usr/bin/env python3
"""
AI Debug Full - Autonomous AI sistemindeki tüm sorunları tespit eder
"""
import requests
import json
import time
import subprocess
import psutil
import os

def check_python_processes():
    """Çalışan Python process'lerini kontrol et"""
    print("🔍 Çalışan Python process'leri kontrol ediliyor...")
    
    python_processes = []
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['name'] and 'python' in proc.info['name'].lower():
                cmdline = ' '.join(proc.info['cmdline']) if proc.info['cmdline'] else ''
                if 'real_data_backend' in cmdline or 'backend' in cmdline:
                    python_processes.append({
                        'pid': proc.info['pid'],
                        'cmdline': cmdline
                    })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    
    if python_processes:
        print("✅ Backend process'leri bulundu:")
        for proc in python_processes:
            print(f"   PID {proc['pid']}: {proc['cmdline']}")
        return True
    else:
        print("❌ Backend process'i bulunamadı")
        return False

def check_port_8003():
    """Port 8003'ün kullanılıp kullanılmadığını kontrol et"""
    print("\n🔍 Port 8003 kontrol ediliyor...")
    
    try:
        for conn in psutil.net_connections():
            if conn.laddr.port == 8003:
                print(f"✅ Port 8003 kullanımda - PID: {conn.pid}")
                return True
        print("❌ Port 8003 boş - Backend çalışmıyor")
        return False
    except Exception as e:
        print(f"⚠️ Port kontrol hatası: {e}")
        return False

def test_basic_backend():
    """Temel backend endpoint'lerini test et"""
    print("\n🔍 Temel backend endpoint'leri test ediliyor...")
    
    endpoints = [
        ("Health Check", "http://localhost:8003/health"),
        ("API Health", "http://localhost:8003/api/health"),
        ("Root", "http://localhost:8003/"),
        ("Docs", "http://localhost:8003/docs")
    ]
    
    results = []
    for name, url in endpoints:
        try:
            response = requests.get(url, timeout=5)
            status = f"✅ {response.status_code}" if response.status_code == 200 else f"⚠️ {response.status_code}"
            print(f"   {status} - {name}")
            results.append(response.status_code == 200)
        except requests.exceptions.ConnectionError:
            print(f"   ❌ Bağlantı yok - {name}")
            results.append(False)
        except Exception as e:
            print(f"   ❌ Hata - {name}: {e}")
            results.append(False)
    
    return any(results)

def test_ai_endpoints():
    """AI endpoint'lerini detaylı test et"""
    print("\n🤖 AI endpoint'leri detaylı test ediliyor...")
    
    # Test 1: Old AI Chat
    print("1. Eski AI Chat endpoint'i test ediliyor...")
    try:
        response = requests.get("http://localhost:8003/api/ai-chat/status", timeout=5)
        if response.status_code == 200:
            print("   ✅ Eski AI Chat endpoint çalışıyor")
        else:
            print(f"   ⚠️ Eski AI Chat endpoint: {response.status_code}")
    except:
        print("   ❌ Eski AI Chat endpoint erişilemez")
    
    # Test 2: Autonomous AI Status
    print("2. Autonomous AI Status endpoint'i test ediliyor...")
    try:
        response = requests.get("http://localhost:8003/api/autonomous-ai/status", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("   ✅ Autonomous AI Status çalışıyor")
            print(f"      System: {data.get('system_name', 'N/A')}")
            print(f"      Version: {data.get('version', 'N/A')}")
            return True
        else:
            print(f"   ❌ Autonomous AI Status hatası: {response.status_code}")
            print(f"      Response: {response.text[:200]}")
            return False
    except Exception as e:
        print(f"   ❌ Autonomous AI Status exception: {e}")
        return False

def test_ai_chat_detailed():
    """AI chat'i detaylı test et"""
    print("\n💬 AI Chat detaylı test ediliyor...")
    
    test_messages = [
        "Hello",
        "What are the best bars in Denver?",
        "Show me tonight's events at Red Rocks"
    ]
    
    for i, message in enumerate(test_messages, 1):
        print(f"{i}. Test mesajı: '{message}'")
        
        try:
            payload = {
                "message": message,
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
                print(f"   ✅ Yanıt alındı ({response_time:.2f}s)")
                print(f"      Source: {data.get('source', 'N/A')}")
                print(f"      Confidence: {data.get('confidence', 'N/A')}")
                print(f"      Answer length: {len(answer)} karakter")
                
                # Red Rocks sorusu için özel kontrol
                if "Red Rocks" in message:
                    if "Red Rocks" in answer and len(answer) > 200:
                        print("      🎯 Red Rocks sorusu doğru yanıtlandı")
                    else:
                        print("      ⚠️ Red Rocks sorusu generic yanıt aldı")
                        print(f"      Answer preview: {answer[:150]}...")
                
            else:
                print(f"   ❌ Chat hatası: {response.status_code}")
                print(f"      Response: {response.text[:200]}")
                
        except Exception as e:
            print(f"   ❌ Chat test exception: {e}")
        
        print()

def check_frontend_files():
    """Frontend dosyalarını kontrol et"""
    print("🌐 Frontend dosyaları kontrol ediliyor...")
    
    files_to_check = [
        "frontend/src/components/AutonomousAIChatWidget.jsx",
        "frontend/src/App.js",
        "frontend/.env"
    ]
    
    for file_path in files_to_check:
        full_path = os.path.join("esref1-main", file_path)
        if os.path.exists(full_path):
            print(f"   ✅ {file_path}")
        else:
            print(f"   ❌ {file_path} - Dosya bulunamadı")

def check_backend_files():
    """Backend dosyalarını kontrol et"""
    print("\n🔧 Backend dosyaları kontrol ediliyor...")
    
    files_to_check = [
        "backend/real_data_backend.py",
        "backend/services/autonomous_ai_manager.py",
        "backend/routes/autonomous_ai.py"
    ]
    
    for file_path in files_to_check:
        full_path = os.path.join("esref1-main", file_path)
        if os.path.exists(full_path):
            print(f"   ✅ {file_path}")
        else:
            print(f"   ❌ {file_path} - Dosya bulunamadı")

def main():
    """Ana debug fonksiyonu"""
    print("🔍 AI DEBUG FULL - KAPSAMLI SORUN TESPİTİ")
    print("=" * 60)
    print("Bu script autonomous AI sistemindeki tüm sorunları tespit eder")
    print()
    
    # 1. Process kontrolleri
    process_running = check_python_processes()
    port_active = check_port_8003()
    
    # 2. Dosya kontrolleri
    check_backend_files()
    check_frontend_files()
    
    # 3. Backend endpoint testleri
    backend_working = test_basic_backend()
    
    # 4. AI endpoint testleri
    ai_working = False
    if backend_working:
        ai_working = test_ai_endpoints()
        if ai_working:
            test_ai_chat_detailed()
    
    # Sonuç özeti
    print("\n" + "=" * 60)
    print("📋 SORUN TESPİT SONUÇLARI")
    print("=" * 60)
    
    issues = []
    
    if not process_running:
        issues.append("Backend process çalışmıyor")
    
    if not port_active:
        issues.append("Port 8003 boş")
    
    if not backend_working:
        issues.append("Backend endpoint'leri yanıt vermiyor")
    
    if not ai_working:
        issues.append("Autonomous AI endpoint'leri çalışmıyor")
    
    if issues:
        print("❌ TESPİT EDİLEN SORUNLAR:")
        for i, issue in enumerate(issues, 1):
            print(f"   {i}. {issue}")
        
        print(f"\n🔧 ÖNERİLEN ÇÖZÜMLER:")
        print("1. Backend'i yeniden başlatın:")
        print("   cd esref1-main/backend")
        print("   python real_data_backend.py")
        print()
        print("2. Eğer hata alıyorsanız:")
        print("   pip install -r requirements.txt")
        print()
        print("3. Port çakışması varsa:")
        print("   taskkill /f /im python.exe")
        print("   Sonra backend'i tekrar başlatın")
        
    else:
        print("✅ SORUN TESPİT EDİLMEDİ!")
        print("Autonomous AI sistemi çalışıyor olmalı.")
        print("Frontend'de brain ikonu (🧠) ile test edin.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️ Test kullanıcı tarafından durduruldu")
    except Exception as e:
        print(f"\n❌ Debug script hatası: {e}")
        import traceback
        traceback.print_exc()