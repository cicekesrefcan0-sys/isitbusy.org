#!/usr/bin/env python3
"""
Debug nightlife detection
"""
import requests
import json

def test_nightlife_variations():
    """Test different nightlife question variations"""
    questions = [
        "Which neighborhoods have the best nightlife?",
        "Best nightlife areas in Denver?",
        "Where is the best night life in Denver?",
        "Denver nightlife recommendations",
        "Best neighborhoods for nightlife"
    ]
    
    for i, question in enumerate(questions, 1):
        print(f"\n🔍 TEST {i}: {question}")
        print("-" * 50)
        
        payload = {
            "message": question,
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
                
                print(f"Source: {source}")
                print(f"Answer preview: {answer[:100]}...")
                
                # Check if it's the detailed nightlife response
                if "LoDo (Lower Downtown)" in answer and "RiNo (River North Art District)" in answer:
                    print("✅ PERFECT: Detailed nightlife response!")
                elif "LoDo" in answer and "RiNo" in answer:
                    print("✅ GOOD: Mentions neighborhoods")
                else:
                    print("❌ GENERIC: Not specific enough")
            else:
                print(f"❌ Error: {response.status_code}")
                
        except Exception as e:
            print(f"❌ Failed: {e}")

if __name__ == "__main__":
    test_nightlife_variations()