#!/usr/bin/env python3
"""
Quick Test for Autonomous AI Integration
Verifies that the autonomous AI system is properly integrated
"""
import requests
import json
import time

# Backend URL
BACKEND_URL = "http://localhost:8003"

def test_backend_connection():
    """Test if backend is running"""
    print("🔍 Testing backend connection...")
    try:
        response = requests.get(f"{BACKEND_URL}/health", timeout=5)
        if response.status_code == 200:
            print("✅ Backend is running")
            return True
        else:
            print(f"❌ Backend returned status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend connection failed: {e}")
        return False

def test_autonomous_ai_status():
    """Test autonomous AI status endpoint"""
    print("\n🤖 Testing Autonomous AI Status...")
    try:
        response = requests.get(f"{BACKEND_URL}/api/autonomous-ai/status", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("✅ Autonomous AI Status endpoint working")
            print(f"   System: {data.get('system_name', 'Unknown')}")
            print(f"   Version: {data.get('version', 'Unknown')}")
            print(f"   Status: {data.get('status', 'Unknown')}")
            print(f"   Learning: {data.get('self_improvement', {}).get('enabled', False)}")
            return True
        else:
            print(f"❌ Status endpoint failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Status test failed: {e}")
        return False

def test_autonomous_ai_chat():
    """Test autonomous AI chat endpoint"""
    print("\n💬 Testing Autonomous AI Chat...")
    try:
        payload = {
            "message": "What are the best bars in Denver?",
            "user_context": {
                "location": "Denver, Colorado"
            },
            "learning_enabled": True
        }
        
        start_time = time.time()
        response = requests.post(
            f"{BACKEND_URL}/api/autonomous-ai/chat", 
            json=payload, 
            timeout=15
        )
        response_time = time.time() - start_time
        
        if response.status_code == 200:
            data = response.json()
            print("✅ Autonomous AI Chat working")
            print(f"   Response Time: {response_time:.2f}s")
            print(f"   Confidence: {data.get('confidence', 'unknown')}")
            print(f"   Source: {data.get('source', 'unknown')}")
            print(f"   Learning Applied: {data.get('learning_applied', False)}")
            print(f"   Answer Preview: {data.get('answer', '')[:100]}...")
            return True
        else:
            print(f"❌ Chat endpoint failed: {response.status_code}")
            print(f"   Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Chat test failed: {e}")
        return False

def test_autonomous_ai_suggestions():
    """Test autonomous AI suggestions endpoint"""
    print("\n💡 Testing Autonomous AI Suggestions...")
    try:
        response = requests.get(f"{BACKEND_URL}/api/autonomous-ai/suggestions", timeout=10)
        if response.status_code == 200:
            data = response.json()
            print("✅ Autonomous AI Suggestions working")
            print(f"   Popular Topics: {len(data.get('popular_topics', []))}")
            print(f"   Trending Questions: {len(data.get('trending_questions', []))}")
            if data.get('popular_topics'):
                print(f"   Example: {data['popular_topics'][0]}")
            return True
        else:
            print(f"❌ Suggestions endpoint failed: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Suggestions test failed: {e}")
        return False

def main():
    """Main test function"""
    print("🤖 AUTONOMOUS AI INTEGRATION - QUICK TEST")
    print("=" * 50)
    print(f"🌐 Testing backend at: {BACKEND_URL}")
    print()
    
    # Test backend connection
    if not test_backend_connection():
        print("\n❌ Backend not available. Please start the backend server first:")
        print("   cd backend && python real_data_backend.py")
        return
    
    # Test autonomous AI endpoints
    tests = [
        test_autonomous_ai_status,
        test_autonomous_ai_chat,
        test_autonomous_ai_suggestions
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
    
    # Results
    print("\n" + "=" * 50)
    print("📋 QUICK TEST RESULTS")
    print("=" * 50)
    print(f"✅ Passed: {passed}/{total}")
    print(f"🎯 Success Rate: {(passed/total)*100:.1f}%")
    
    if passed == total:
        print("\n🚀 Autonomous AI Integration: SUCCESSFUL!")
        print("   The self-learning AI system is ready to use.")
        print("   Frontend can now use the AutonomousAIChatWidget.")
    else:
        print(f"\n⚠️ Some tests failed ({total-passed}/{total})")
        print("   Check the backend logs for more details.")
    
    print(f"\n📚 API Documentation: {BACKEND_URL}/docs")
    print(f"🤖 Autonomous AI Status: {BACKEND_URL}/api/autonomous-ai/status")

if __name__ == "__main__":
    main()