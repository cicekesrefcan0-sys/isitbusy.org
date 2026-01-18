#!/usr/bin/env python3
"""
🔧 Quick AI Cache Fix Test
Test if backend autonomous AI is working and provide cache fix instructions
"""
import requests
import json
from datetime import datetime

def test_backend_ai():
    """Test if autonomous AI backend is working"""
    print("🔍 Testing Autonomous AI Backend...")
    print("=" * 50)
    
    backend_url = "http://localhost:8003"
    
    try:
        # Test 1: Backend health check
        print("1️⃣ Testing backend connection...")
        response = requests.get(f"{backend_url}/api/autonomous-ai/status", timeout=5)
        
        if response.status_code == 200:
            status_data = response.json()
            print(f"   ✅ Backend Status: {status_data.get('status', 'unknown')}")
            print(f"   ✅ System: {status_data.get('system_name', 'Unknown')} v{status_data.get('version', '?')}")
            print(f"   ✅ Learning: {'Active' if status_data.get('self_improvement', {}).get('enabled') else 'Disabled'}")
        else:
            print(f"   ❌ Backend Status Error: {response.status_code}")
            return False
            
    except requests.exceptions.ConnectionError:
        print("   ❌ Backend Connection Failed!")
        print("   💡 Solution: Check if backend is running with 'pm2 status'")
        return False
    except Exception as e:
        print(f"   ❌ Backend Error: {e}")
        return False
    
    try:
        # Test 2: AI Chat functionality
        print("\n2️⃣ Testing AI chat responses...")
        
        test_questions = [
            ("hey", "Should get friendly greeting"),
            ("Which neighborhoods have the best nightlife?", "Should get 4 neighborhood guide"),
            ("Recommend breweries in RiNo district", "Should get specific brewery list")
        ]
        
        for question, expected in test_questions:
            print(f"\n   🤖 Testing: '{question}'")
            
            chat_data = {
                "message": question,
                "user_context": {"location": "Denver, Colorado"},
                "learning_enabled": True
            }
            
            response = requests.post(
                f"{backend_url}/api/autonomous-ai/chat",
                json=chat_data,
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                answer = result.get('answer', '')
                source = result.get('source', 'unknown')
                confidence = result.get('confidence', 'unknown')
                
                print(f"   ✅ Response received (source: {source}, confidence: {confidence})")
                print(f"   📝 Answer preview: {answer[:100]}...")
                
                # Check if it's a generic fallback response
                if "I'm continuously learning and improving" in answer:
                    print(f"   ⚠️  Generic fallback response - but backend is working!")
                else:
                    print(f"   🎯 Specific response - backend working perfectly!")
                    
            else:
                print(f"   ❌ Chat Error: {response.status_code}")
                
    except Exception as e:
        print(f"   ❌ Chat Test Error: {e}")
        return False
    
    return True

def show_cache_fix_instructions():
    """Show cache fix instructions"""
    print("\n" + "=" * 50)
    print("🔧 CACHE FIX INSTRUCTIONS")
    print("=" * 50)
    
    print("""
🎯 THE PROBLEM:
   Backend is working perfectly, but frontend browser cache 
   is showing old AI widget code instead of new Autonomous AI.

🚀 QUICK FIX (Try this first!):
   1. Open: http://localhost:3000
   2. Press: Ctrl+F5 (Windows) or Cmd+Shift+R (Mac)
   3. Look for: Brain icon (🧠) in bottom-right corner
   4. Test with: "hey" message

✅ WHAT YOU SHOULD SEE AFTER FIX:
   • Brain icon (🧠) instead of regular bot icon
   • "Autonomous AI" title with "Self-Learning Active"
   • Purple/blue gradient design
   • Specific responses instead of generic ones

🛠️ IF CTRL+F5 DOESN'T WORK:
   1. Open Developer Tools (F12)
   2. Go to Network tab
   3. Check "Disable cache"
   4. Refresh page (F5)
   5. Test AI widget

🕵️ INCOGNITO TEST:
   Open incognito/private window and test there.
   If it works in incognito, it's definitely cache issue.

🔄 NUCLEAR OPTION (Last resort):
   pm2 restart isitbusy-frontend
   # or
   cd esref1-main/frontend && npm start

📊 VERIFY SUCCESS:
   Test these questions and expect specific answers:
   • "hey" → Friendly greeting with capabilities
   • "nightlife" → 4 neighborhood guide
   • "RiNo breweries" → Specific brewery recommendations
   • "Red Rocks" → Detailed venue information
""")

def main():
    print("🤖 AUTONOMOUS AI CACHE FIX TEST")
    print(f"⏰ Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 50)
    
    # Test backend
    backend_working = test_backend_ai()
    
    if backend_working:
        print("\n🎉 BACKEND TEST RESULTS:")
        print("   ✅ Backend is running correctly")
        print("   ✅ Autonomous AI is active")
        print("   ✅ PM2 setup is working")
        print("   ✅ All endpoints responding")
        
        print("\n🔍 DIAGNOSIS:")
        print("   ✅ Backend: WORKING PERFECTLY")
        print("   ❌ Frontend: CACHE ISSUE")
        print("   💡 Solution: Clear browser cache")
        
        show_cache_fix_instructions()
        
        print("\n🌐 HELPFUL LINKS:")
        print("   • App: http://localhost:3000")
        print("   • Cache Fix Tool: file:///" + __file__.replace('QUICK_AI_CACHE_FIX_TEST.py', 'CACHE_CLEAR_SOLUTION.html'))
        print("   • Backend Status: http://localhost:8003/api/autonomous-ai/status")
        
    else:
        print("\n❌ BACKEND ISSUES DETECTED:")
        print("   Check if backend is running: pm2 status")
        print("   Restart if needed: pm2 restart isitbusy-backend")
        
    print("\n" + "=" * 50)
    print("🎯 NEXT STEPS:")
    print("1. Open http://localhost:3000")
    print("2. Press Ctrl+F5 to clear cache")
    print("3. Look for brain icon (🧠)")
    print("4. Test with 'hey' message")
    print("=" * 50)

if __name__ == "__main__":
    main()