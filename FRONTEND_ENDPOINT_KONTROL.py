#!/usr/bin/env python3
"""
Frontend'in hangi endpoint'e bağlandığını kontrol et
"""
import requests
import json

def test_frontend_connection():
    """Frontend'in bağlandığı endpoint'i test et"""
    print("🔍 FRONTEND ENDPOINT KONTROL")
    print("=" * 40)
    
    # Test 1: Autonomous AI endpoint
    print("1. Autonomous AI endpoint test...")
    try:
        response = requests.get("http://localhost:8003/api/autonomous-ai/status", timeout=5)
        if response.status_code == 200:
            print("✅ Autonomous AI endpoint aktif")
            data = response.json()
            print(f"   System: {data.get('system_name', 'Unknown')}")
            print(f"   Version: {data.get('version', 'Unknown')}")
        else:
            print(f"❌ Autonomous AI endpoint hatası: {response.status_code}")
    except Exception as e:
        print(f"❌ Autonomous AI endpoint erişilemez: {e}")
    
    # Test 2: Eski AI endpoint (olmamalı)
    print("\n2. Eski AI endpoint test...")
    try:
        response = requests.get("http://localhost:8003/api/ai/status", timeout=5)
        if response.status_code == 200:
            print("⚠️  ESKİ AI ENDPOINT HALA AKTİF!")
            print("   Bu sorunun kaynağı olabilir")
        else:
            print("✅ Eski AI endpoint kapalı")
    except Exception as e:
        print("✅ Eski AI endpoint erişilemez (normal)")
    
    # Test 3: Frontend'in kullandığı exact request
    print("\n3. Frontend exact request test...")
    payload = {
        "message": "hey",
        "user_context": {"location": "Denver, Colorado"},
        "learning_enabled": True
    }
    
    try:
        response = requests.post(
            "http://localhost:8003/api/autonomous-ai/chat",
            json=payload,
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            answer = data.get('answer', '')
            source = data.get('source', 'unknown')
            
            print(f"✅ Response alındı!")
            print(f"   Source: {source}")
            print(f"   Answer: {answer[:100]}...")
            
            if answer.startswith("I'm continuously learning"):
                print("❌ SORUN: Generic fallback yanıtı!")
                print("   Frontend yanlış endpoint kullanıyor olabilir")
                return False
            else:
                print("✅ Spesifik yanıt alındı!")
                return True
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return False

def check_frontend_config():
    """Frontend konfigürasyonunu kontrol et"""
    print("\n" + "=" * 40)
    print("FRONTEND KONFİGÜRASYON KONTROL")
    print("=" * 40)
    
    try:
        with open("frontend/.env", "r") as f:
            env_content = f.read()
            print("Frontend .env dosyası:")
            print(env_content)
            
            if "localhost:8003" in env_content:
                print("✅ Backend URL doğru")
            else:
                print("❌ Backend URL yanlış!")
                
    except Exception as e:
        print(f"❌ .env dosyası okunamadı: {e}")

if __name__ == "__main__":
    success = test_frontend_connection()
    check_frontend_config()
    
    print("\n" + "=" * 40)
    if success:
        print("✅ Backend doğru çalışıyor!")
        print("Sorun frontend cache'inde olabilir.")
        print("\nÇÖZÜM:")
        print("1. Browser'da Ctrl+F5 (hard refresh)")
        print("2. Developer tools açıp Network tab'ını kontrol et")
        print("3. Hangi endpoint'e request gönderdiğini gör")
    else:
        print("❌ Sorun tespit edildi!")
        print("Frontend yanlış endpoint kullanıyor olabilir.")