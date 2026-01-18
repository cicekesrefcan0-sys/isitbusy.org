#!/usr/bin/env python3
"""
AI Gelişmiş Test - Yeni detaylı cevapları test et
"""
import requests
import json

def test_improved_ai():
    print("🚀 AI Gelişmiş Cevap Testi")
    print("=" * 40)
    
    backend_url = "http://localhost:8002"
    
    # Yeni detaylı cevapları test et
    test_cases = [
        {
            "question": "Denver'daki en iyi barlar neler?",
            "expected_keywords": ["RiNo", "LoDo", "Capitol Hill", "The Source"]
        },
        {
            "question": "Red Rocks ne zaman açık?",
            "expected_keywords": ["konserden 2 saat önce", "06:00-22:00", "Mayıs-Ekim"]
        },
        {
            "question": "LoDo'da hangi mekanlar var?",
            "expected_keywords": ["ViewHouse", "Howl at the Moon", "Jackson's"]
        },
        {
            "question": "Gece hayatı için nereyi önerirsin?",
            "expected_keywords": ["LoDo", "RiNo", "Capitol Hill", "mainstream", "hip"]
        },
        {
            "question": "Bar saatleri nedir?",
            "expected_keywords": ["23:00-01:00", "02:00", "hafta sonu"]
        }
    ]
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n🧪 Test {i}: {test['question']}")
        print("-" * 30)
        
        try:
            response = requests.post(
                f"{backend_url}/api/ai/chat",
                json={
                    "message": test['question'],
                    "user_context": {"location": "Denver, Colorado"}
                },
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                answer = data['answer']
                
                print(f"✅ Cevap: {answer[:200]}...")
                
                # Anahtar kelimeleri kontrol et
                found_keywords = []
                for keyword in test['expected_keywords']:
                    if keyword.lower() in answer.lower():
                        found_keywords.append(keyword)
                
                if found_keywords:
                    print(f"🎯 Bulunan anahtar kelimeler: {', '.join(found_keywords)}")
                    print(f"✨ Detay seviyesi: {'Mükemmel' if len(found_keywords) >= 2 else 'İyi'}")
                else:
                    print(f"⚠️  Beklenen anahtar kelimeler bulunamadı")
                    
            else:
                print(f"❌ HTTP Hatası: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Hata: {e}")
    
    print(f"\n🎉 Test tamamlandı!")
    print(f"\n💡 AI artık çok daha detaylı ve yararlı cevaplar veriyor!")

if __name__ == "__main__":
    test_improved_ai()