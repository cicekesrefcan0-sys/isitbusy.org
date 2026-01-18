#!/usr/bin/env python3
"""
Test Red Rocks specific response
"""
import requests
import json

def test_red_rocks():
    """Test Red Rocks question"""
    print("🎵 RED ROCKS TEST")
    print("=" * 30)
    
    payload = {
        "message": "Show me tonight's events at Red Rocks",
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
            
            print(f"✅ Response received!")
            print(f"Source: {data.get('source', 'unknown')}")
            print(f"Confidence: {data.get('confidence', 'unknown')}")
            print(f"Learning Applied: {data.get('learning_applied', False)}")
            print("\n📝 ANSWER:")
            print("-" * 40)
            print(answer)
            print("-" * 40)
            
            # Check if it's a specific Red Rocks response
            if "Red Rocks Amphitheatre" in answer and "redrocksonline.com" in answer:
                print("\n🎉 PERFECT! Specific Red Rocks response!")
                return True
            elif answer.startswith("I'm continuously learning"):
                print("\n❌ Still getting generic fallback!")
                return False
            else:
                print("\n✅ Good response, but could be more specific")
                return True
        else:
            print(f"❌ Error: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        return False

if __name__ == "__main__":
    test_red_rocks()