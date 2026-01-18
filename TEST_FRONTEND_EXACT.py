#!/usr/bin/env python3
"""
Test the exact same request the frontend makes
"""
import requests
import json

def test_frontend_request():
    """Test exact frontend request"""
    print("🔍 FRONTEND EXACT REQUEST TEST")
    print("=" * 40)
    
    # Exact payload that frontend sends
    payload = {
        "message": "Which neighborhoods have the best nightlife?",
        "user_context": {
            "location": "Denver, Colorado",
            "venue": None,
            "preferences": {
                "area": "Denver metro area"
            }
        },
        "learning_enabled": True
    }
    
    print(f"🚀 Sending request to: http://localhost:8003/api/autonomous-ai/chat")
    print(f"📝 Payload: {json.dumps(payload, indent=2)}")
    
    try:
        response = requests.post(
            "http://localhost:8003/api/autonomous-ai/chat",
            json=payload,
            timeout=10,
            headers={'Content-Type': 'application/json'}
        )
        
        print(f"\n📊 Response Status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Success!")
            print(f"Source: {data.get('source', 'unknown')}")
            print(f"Confidence: {data.get('confidence', 'unknown')}")
            print(f"Learning Applied: {data.get('learning_applied', False)}")
            
            answer = data.get('answer', '')
            print(f"\n📝 ANSWER:")
            print("-" * 50)
            print(answer)
            print("-" * 50)
            
            # Check if it's the generic fallback
            if answer.startswith("I'm continuously learning"):
                print("\n❌ PROBLEM: Getting generic fallback!")
                print("This means the AI intent analysis is not working")
                return False
            else:
                print("\n🎉 SUCCESS: Getting specific response!")
                return True
        else:
            print(f"❌ HTTP Error: {response.status_code}")
            print(f"Response: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Request failed: {e}")
        return False

if __name__ == "__main__":
    test_frontend_request()