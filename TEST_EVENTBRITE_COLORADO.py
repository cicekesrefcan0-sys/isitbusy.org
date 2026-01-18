#!/usr/bin/env python3
"""
Eventbrite Colorado Test Script
Tests the Eventbrite scraper for Colorado events with after party detection
"""
import asyncio
import sys
import os
import json
from datetime import datetime

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from services.eventbrite_scraper import (
    scrape_eventbrite_colorado,
    get_colorado_events,
    get_colorado_after_parties,
    get_colorado_regular_events,
    test_eventbrite_scraper
)

async def test_eventbrite_full():
    """Full test of Eventbrite Colorado functionality"""
    print("🧪 EVENTBRITE COLORADO TEST BAŞLADI")
    print("=" * 50)
    
    try:
        # Test 1: Scraper test
        print("\n1️⃣ Testing Eventbrite scraper...")
        test_results = await test_eventbrite_scraper()
        print(f"✅ Scraper test completed: {test_results}")
        
        # Test 2: Scrape Colorado events (demo mode)
        print("\n2️⃣ Scraping Colorado events (demo mode)...")
        scrape_stats = await scrape_eventbrite_colorado()
        print(f"✅ Scraping completed: {scrape_stats}")
        
        # Test 3: Get regular events
        print("\n3️⃣ Getting regular events...")
        regular_events = await get_colorado_regular_events(10)
        print(f"✅ Found {len(regular_events)} regular events")
        
        if regular_events:
            print("📋 Sample regular event:")
            sample_event = regular_events[0]
            print(f"   Title: {sample_event.get('title', 'N/A')}")
            print(f"   City: {sample_event.get('city', 'N/A')}")
            print(f"   Venue: {sample_event.get('venue', 'N/A')}")
            print(f"   Date: {sample_event.get('start_time', 'N/A')}")
            print(f"   Category: {sample_event.get('category', 'N/A')}")
        
        # Test 4: Get after parties
        print("\n4️⃣ Getting after parties...")
        after_parties = await get_colorado_after_parties(10)
        print(f"✅ Found {len(after_parties)} after parties")
        
        if after_parties:
            print("🎉 Sample after party:")
            sample_party = after_parties[0]
            print(f"   Title: {sample_party.get('title', 'N/A')}")
            print(f"   City: {sample_party.get('city', 'N/A')}")
            print(f"   Venue: {sample_party.get('venue', 'N/A')}")
            print(f"   Date: {sample_party.get('start_time', 'N/A')}")
            print(f"   Is After Party: {sample_party.get('is_after_party', False)}")
        
        # Test 5: Get all events
        print("\n5️⃣ Getting all events...")
        all_events = await get_colorado_events('events', 20)
        print(f"✅ Found {len(all_events)} total events")
        
        # Summary
        print("\n" + "=" * 50)
        print("📊 TEST SUMMARY:")
        print(f"   Regular Events: {len(regular_events)}")
        print(f"   After Parties: {len(after_parties)}")
        print(f"   Total Events: {len(all_events)}")
        print(f"   Scraping Stats: {scrape_stats}")
        
        # Save results to file
        results = {
            'timestamp': datetime.now().isoformat(),
            'test_results': test_results,
            'scrape_stats': scrape_stats,
            'regular_events_count': len(regular_events),
            'after_parties_count': len(after_parties),
            'total_events_count': len(all_events),
            'sample_regular_event': regular_events[0] if regular_events else None,
            'sample_after_party': after_parties[0] if after_parties else None
        }
        
        with open('eventbrite_test_results.json', 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        print(f"\n💾 Results saved to: eventbrite_test_results.json")
        print("✅ ALL TESTS COMPLETED SUCCESSFULLY!")
        
        return results
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return None

async def test_api_endpoints():
    """Test API endpoints"""
    print("\n🌐 TESTING API ENDPOINTS")
    print("=" * 30)
    
    import httpx
    
    base_url = "http://localhost:8000/api/eventbrite"
    
    endpoints_to_test = [
        "/cities",
        "/stats", 
        "/events?limit=5",
        "/after-parties?limit=5",
        "/regular-events?limit=5"
    ]
    
    async with httpx.AsyncClient() as client:
        for endpoint in endpoints_to_test:
            try:
                print(f"Testing: {base_url}{endpoint}")
                response = await client.get(f"{base_url}{endpoint}")
                
                if response.status_code == 200:
                    data = response.json()
                    print(f"✅ {endpoint}: {data.get('count', 'N/A')} items")
                else:
                    print(f"❌ {endpoint}: Status {response.status_code}")
                    
            except Exception as e:
                print(f"❌ {endpoint}: Error - {e}")

def main():
    """Main test function"""
    print("🚀 EVENTBRITE COLORADO INTEGRATION TEST")
    print("Testing Eventbrite scraper for Colorado events")
    print("Includes after party detection and categorization")
    print()
    
    # Run async tests
    results = asyncio.run(test_eventbrite_full())
    
    if results:
        print("\n🎯 NEXT STEPS:")
        print("1. Add your Eventbrite API key to .env file:")
        print("   EVENTBRITE_API_KEY=your_api_key_here")
        print("2. Start the backend server:")
        print("   python backend/server.py")
        print("3. Test API endpoints:")
        print("   curl http://localhost:8000/api/eventbrite/cities")
        print("4. Scrape real data:")
        print("   curl -X POST http://localhost:8000/api/eventbrite/scrape")
        
        # Test API endpoints if server is running
        try:
            print("\n🔄 Testing if server is running...")
            asyncio.run(test_api_endpoints())
        except:
            print("ℹ️  Server not running - start server to test API endpoints")

if __name__ == "__main__":
    main()