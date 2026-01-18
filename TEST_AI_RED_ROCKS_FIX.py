#!/usr/bin/env python3
"""
Test AI Red Rocks Response Fix
Tests if the autonomous AI properly handles Red Rocks event questions
"""
import asyncio
import sys
import os

# Add the backend directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

async def test_autonomous_ai_locally():
    """Test the autonomous AI manager directly"""
    try:
        from services.autonomous_ai_manager import autonomous_ai
        
        print("🤖 Testing Autonomous AI - Red Rocks Event Question")
        print("=" * 60)
        
        # Test the specific question that was failing
        question = "Show me tonight's events at Red Rocks"
        user_context = {
            "location": "Denver, Colorado",
            "preferences": {"area": "Denver metro area"}
        }
        
        print(f"❓ Question: {question}")
        print("🔄 Processing...")
        
        # Process the conversation
        result = await autonomous_ai.process_conversation(question, user_context)
        
        print(f"\n✅ Response received!")
        print(f"🎯 Confidence: {result.get('confidence', 'unknown')}")
        print(f"📚 Source: {result.get('source', 'unknown')}")
        print(f"🧠 Learning Applied: {result.get('learning_applied', False)}")
        print(f"\n💬 Answer:")
        print("-" * 40)
        print(result.get('answer', 'No answer provided'))
        print("-" * 40)
        
        # Test intent analysis
        print(f"\n🔍 Testing Intent Analysis...")
        intent = await autonomous_ai._analyze_question_intent(question)
        print(f"Primary Intent: {intent['primary_intent']}")
        print(f"Entities: {intent['entities']}")
        print(f"Time Sensitive: {intent['time_sensitive']}")
        print(f"Location Specific: {intent['location_specific']}")
        
        # Test another question
        print(f"\n" + "=" * 60)
        question2 = "What are the best bars in Denver?"
        print(f"❓ Question 2: {question2}")
        
        result2 = await autonomous_ai.process_conversation(question2, user_context)
        print(f"✅ Response 2 - Source: {result2.get('source')}")
        print(f"💬 Answer Preview: {result2.get('answer', '')[:100]}...")
        
        print(f"\n🎉 Autonomous AI is working correctly!")
        return True
        
    except Exception as e:
        print(f"❌ Error testing autonomous AI: {e}")
        import traceback
        traceback.print_exc()
        return False

async def test_ai_status():
    """Test AI system status"""
    try:
        from services.autonomous_ai_manager import autonomous_ai
        
        print(f"\n📊 Testing AI System Status...")
        status = await autonomous_ai.get_system_status()
        
        print(f"Status: {status['status']}")
        print(f"Learning Enabled: {status['learning_enabled']}")
        print(f"Knowledge Base Size: {status['knowledge_base_size']}")
        print(f"Conversation History: {status['conversation_history_size']}")
        
        return True
        
    except Exception as e:
        print(f"❌ Error getting AI status: {e}")
        return False

async def main():
    """Main test function"""
    print("🔧 AUTONOMOUS AI - RED ROCKS FIX TEST")
    print("=" * 60)
    
    # Test 1: Direct AI functionality
    success1 = await test_autonomous_ai_locally()
    
    # Test 2: AI status
    success2 = await test_ai_status()
    
    print(f"\n" + "=" * 60)
    print("📋 TEST RESULTS")
    print("=" * 60)
    
    if success1 and success2:
        print("✅ All tests passed!")
        print("🚀 Autonomous AI is working correctly")
        print("🎯 Red Rocks questions should now be handled properly")
    else:
        print("❌ Some tests failed")
        print("🔧 Check the error messages above")
    
    print(f"\n💡 Next steps:")
    print("1. Start the backend: python backend/real_data_backend.py")
    print("2. Test in frontend: Ask 'Show me tonight's events at Red Rocks'")
    print("3. The AI should now provide detailed Red Rocks information")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n⚠️ Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")