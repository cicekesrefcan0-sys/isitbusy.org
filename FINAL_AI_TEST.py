#!/usr/bin/env python3
"""
Final AI Test - Tüm AI fonksiyonlarını test et
"""
import requests
import json

def test_all_ai_functions():
    """Tüm AI fonksiyonlarını test et"""
    print("🧠 FINAL AI TEST - AUTONOMOUS AI SİSTEMİ")
    print("=" * 50)
    
    test_cases = [
        {
            "name": "RiNo Breweries",
            "question": "Recommend breweries in RiNo district",
            "expected_keywords": ["RiNo", "The Source", "Ratio Beerworks"]
        },
        {
            "name": "Red Rocks Events", 
            "question": "Show me tonight's events at Red Rocks",
            "expected_keywords": ["Red Rocks", "redrocksonline.com", "parking"]
        },
        {
            "name": "Nightlife Neighborhoods",
            "question": "Which neighborhoods have the best nightlife?",
            "expected_keywords": ["LoDo", "RiNo", "Capitol Hill", "Highlands"]
        },
        {
            "name": "Best Bars Denver",
            "question": "What are the best bars in Denver?",
            "expected_keywords": ["Denver", "bars", "LoDo"]
        },
        {
            "name": "Hours Information",
            "question": "What are Red Rocks hours?",
            "expected_keywords": ["Red Rocks", "hours", "gates"]
        }
    ]
    
    passed = 0
    total = len(test_cases)
    
    for i, test in enumerate(test_cases, 1):
        print(f"\n🔍 TEST {i}: {test['name']}")
        print(f"Question: {test['question']}")
        print("-" * 40)
        
        payload = {
            "message": test['question'],
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
                confidence = data.get('confidence', 'unknown')
                
                print(f"✅ Response received!")
                print(f"Source: {source}")
                print(f"Confidence: {confidence}")
                
                # Check for expected keywords
                keywords_found = 0
                for keyword in test['expected_keywords']:
                    if keyword.lower() in answer.lower():
                        keywords_found += 1
                
                if keywords_found >= len(test['expected_keywords']) // 2:
                    print(f"✅ PASSED: Found {keywords_found}/{len(test['expected_keywords'])} keywords")
                    passed += 1
                else:
                    print(f"❌ FAILED: Only found {keywords_found}/{len(test['expected_keywords'])} keywords")
                
                print(f"Answer preview: {answer[:100]}...")
                
            else:
                print(f"❌ HTTP Error: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Test failed: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 FINAL RESULTS: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 ALL TESTS PASSED! AI SİSTEMİ MÜKEMMEL ÇALIŞIYOR!")
        print("\n✅ Autonomous AI özellikleri:")
        print("  • RiNo brewery önerileri")
        print("  • Red Rocks etkinlik bilgileri") 
        print("  • Nightlife neighborhood rehberi")
        print("  • Denver bar önerileri")
        print("  • Venue saat bilgileri")
        print("\n🚀 Frontend'de brain ikonu (🧠) ile test edebilirsin!")
    elif passed >= total * 0.8:
        print("✅ ÇOĞU TEST BAŞARILI! AI sistemi iyi çalışıyor.")
    else:
        print("❌ BAZI TESTLER BAŞARISIZ! Kontrol gerekli.")
    
    return passed == total

if __name__ == "__main__":
    test_all_ai_functions()