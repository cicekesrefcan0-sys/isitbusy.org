#!/usr/bin/env python3
"""
AI Cevap Düzeltme Test - AI'nin artık doğru cevap verip vermediğini test et
"""
import requests
import json
import time

# Test soruları
test_questions = [
    "Denver'daki en iyi barlar neler?",
    "Bu akşam hangi etkinlikler var?", 
    "Red Rocks ne zaman açık?",
    "Hava durumu nasıl?",
    "LoDo'da hangi restoranlar var?"
]

def test_ai_responses():
    print("🤖 AI Cevap Kalitesi Testi")
    print("=" * 40)
    
    backend_url = "http://localhost:8002"
    
    for i, question in enumerate(test_questions, 1):
        print(f"\n🧪 Test {i}: {question}")
        print("-" * 30)
        
        try:
            response = requests.post(
                f"{backend_url}/api/ai/chat",
                json={
                    "message": question,
                    "user_context": {
                        "location": "Denver, Colorado"
                    }
                },
                timeout=15
            )
            
            if response.status_code == 200:
                data = response.json()
                answer = data['answer']
                
                print(f"✅ Cevap: {answer}")
                print(f"🔍 Kaynak sayısı: {data['sources_used']}")
                print(f"🎯 Güven: {data['confidence']}")
                
                # Cevap kalitesini değerlendir
                if len(answer) < 20:
                    print("⚠️  Cevap çok kısa")
                elif "I'm having trouble" in answer:
                    print("❌ Hala eski hata mesajı veriyor")
                elif any(word in answer.lower() for word in ['denver', 'colorado', 'bar', 'restaurant', 'event']):
                    print("✨ İyi cevap!")
                else:
                    print("🤔 Cevap belirsiz")
                    
            else:
                print(f"❌ HTTP Hatası: {response.status_code}")
                print(f"Detay: {response.text}")
                
        except requests.exceptions.ConnectionError:
            print("❌ Backend'e bağlanılamıyor - Port 8002'de çalışıyor mu?")
        except Exception as e:
            print(f"❌ Hata: {e}")
        
        time.sleep(1)
    
    print(f"\n🎉 Test tamamlandı!")
    print(f"\n💡 Eğer hala 'I'm having trouble' cevabı alıyorsan:")
    print(f"   1. Backend'i yeniden başlat: python backend/real_data_backend.py")
    print(f"   2. Frontend'i yeniden başlat: cd frontend && npm start")
    print(f"   3. Browser cache'ini temizle (Ctrl+Shift+R)")

if __name__ == "__main__":
    test_ai_responses()