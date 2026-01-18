#!/usr/bin/env python3
"""
Final AI System Test - Test the improved AI with web search
"""
import requests
import json
import time
from datetime import datetime

# Configuration
BACKEND_URL = "http://localhost:8002"
API_BASE = f"{BACKEND_URL}/api"

def test_ai_chat():
    """Test the AI chat endpoint with various questions"""
    
    print("🤖 Testing Advanced AI Chat System")
    print("=" * 50)
    
    # Test questions covering different scenarios
    test_questions = [
        {
            "message": "What are the best bars in Denver right now?",
            "description": "Venue recommendation query"
        },
        {
            "message": "What time does Red Rocks Amphitheatre open?",
            "description": "Specific venue hours query"
        },
        {
            "message": "Are there any concerts this weekend in Colorado?",
            "description": "Event search query"
        },
        {
            "message": "What's the weather like in Denver today?",
            "description": "Current information query"
        },
        {
            "message": "Best restaurants near downtown Denver",
            "description": "Location-specific recommendation"
        },
        {
            "message": "Tell me about nightlife in LoDo",
            "description": "Area-specific query"
        }
    ]
    
    for i, test in enumerate(test_questions, 1):
        print(f"\n🧪 Test {i}: {test['description']}")
        print(f"Question: {test['message']}")
        print("-" * 40)
        
        try:
            # Send request to AI chat endpoint
            response = requests.post(
                f"{API_BASE}/ai/chat",
                json={
                    "message": test['message'],
                    "user_context": {
                        "location": "Denver, Colorado",
                        "preferences": {"area": "Denver metro area"}
                    }
                },
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                
                print(f"✅ Status: SUCCESS")
                print(f"📝 Answer: {data['answer']}")
                print(f"🔍 Sources used: {data['sources_used']}")
                print(f"🎯 Confidence: {data['confidence']}")
                print(f"🧠 Intent: {data['intent']['type']}")
                
                if data['search_results']:
                    print(f"📚 Search results:")
                    for j, result in enumerate(data['search_results'][:2], 1):
                        print(f"   {j}. {result['title']}")
                        print(f"      {result['snippet'][:100]}...")
                
                # Check if response is helpful
                answer_length = len(data['answer'])
                if answer_length < 20:
                    print(f"⚠️  Warning: Response seems too short ({answer_length} chars)")
                elif "I couldn't find" in data['answer'] and data['sources_used'] > 0:
                    print(f"⚠️  Warning: Has sources but says couldn't find info")
                else:
                    print(f"✨ Response quality: Good")
                    
            else:
                print(f"❌ Status: FAILED ({response.status_code})")
                print(f"Error: {response.text}")
                
        except requests.exceptions.Timeout:
            print(f"⏰ Status: TIMEOUT (>30s)")
        except Exception as e:
            print(f"💥 Status: ERROR - {e}")
        
        # Small delay between tests
        time.sleep(2)
    
    print(f"\n🎉 AI Chat Test Completed!")

def test_ai_status():
    """Test AI service status"""
    print(f"\n🔍 Checking AI Service Status...")
    
    try:
        response = requests.get(f"{API_BASE}/ai/status", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ AI Service Status: {data['status']}")
            print(f"🧠 AI Model: {data['ai_model']}")
            print(f"🔍 Web Search APIs: {', '.join(data['web_search'])}")
            
            features = data['features']
            print(f"🚀 Features:")
            for feature, enabled in features.items():
                status = "✅" if enabled else "❌"
                print(f"   {status} {feature.replace('_', ' ').title()}")
                
        else:
            print(f"❌ Status check failed: {response.status_code}")
            
    except Exception as e:
        print(f"💥 Status check error: {e}")

def test_web_search():
    """Test web search functionality"""
    print(f"\n🌐 Testing Web Search...")
    
    try:
        response = requests.post(
            f"{API_BASE}/ai/search",
            json={
                "query": "best bars Denver Colorado",
                "num_results": 3
            },
            timeout=15
        )
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Web Search: SUCCESS")
            print(f"📊 Results found: {data['total_results']}")
            
            for i, result in enumerate(data['results'][:2], 1):
                print(f"   {i}. {result['title']}")
                print(f"      {result['snippet'][:80]}...")
                
        else:
            print(f"❌ Web Search failed: {response.status_code}")
            
    except Exception as e:
        print(f"💥 Web Search error: {e}")

def main():
    """Run all AI tests"""
    print("🚀 Advanced AI System - Final Test Suite")
    print("=" * 60)
    print(f"⏰ Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🌐 Backend URL: {BACKEND_URL}")
    
    # Test AI service status first
    test_ai_status()
    
    # Test web search functionality
    test_web_search()
    
    # Test AI chat with various questions
    test_ai_chat()
    
    print(f"\n" + "=" * 60)
    print(f"✅ All tests completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"")
    print(f"📋 Summary:")
    print(f"   • AI service status checked")
    print(f"   • Web search functionality tested")
    print(f"   • AI chat responses evaluated")
    print(f"")
    print(f"🎯 Next steps if issues found:")
    print(f"   1. Check backend server is running on port 8002")
    print(f"   2. Verify API keys in backend/.env file")
    print(f"   3. Check network connectivity")
    print(f"   4. Review backend logs for errors")

if __name__ == "__main__":
    main()