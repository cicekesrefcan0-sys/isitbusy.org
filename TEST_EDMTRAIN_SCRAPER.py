#!/usr/bin/env python3
"""
EDM Train Scraper Test
Tests the EDM Train event scraping functionality
"""
import asyncio
import sys
import os
sys.path.append('backend')

from backend.services.edmtrain_scraper import EDMTrainScraper
import json
from datetime import datetime

async def test_edmtrain_scraper():
    """
    Test EDM Train scraper functionality
    """
    print("🎵 EDM TRAIN SCRAPER TEST")
    print("=" * 50)
    
    async with EDMTrainScraper() as scraper:
        # Test 1: Get Denver EDM events
        print("\n📍 Test 1: Denver EDM Events")
        print("-" * 30)
        
        denver_events = await scraper.get_events_by_location("denver", limit=10)
        
        if denver_events:
            print(f"✅ Found {len(denver_events)} EDM events in Denver")
            
            for i, event in enumerate(denver_events[:3], 1):
                print(f"\n{i}. {event.get('name', 'Unknown Event')}")
                print(f"   📅 Date: {event.get('date', 'TBD')}")
                print(f"   🏢 Venue: {event.get('venue', 'TBD')}")
                print(f"   🎤 Artists: {', '.join(event.get('artists', []))}")
                print(f"   🔗 URL: {event.get('url', 'N/A')}")
                print(f"   🏷️  Category: {event.get('category', 'N/A')}")
        else:
            print("❌ No EDM events found in Denver")
        
        # Test 2: Get Chicago EDM events
        print("\n📍 Test 2: Chicago EDM Events")
        print("-" * 30)
        
        chicago_events = await scraper.get_events_by_location("chicago", limit=5)
        
        if chicago_events:
            print(f"✅ Found {len(chicago_events)} EDM events in Chicago")
            
            for i, event in enumerate(chicago_events[:2], 1):
                print(f"\n{i}. {event.get('name', 'Unknown Event')}")
                print(f"   📅 Date: {event.get('date', 'TBD')}")
                print(f"   🏢 Venue: {event.get('venue', 'TBD')}")
        else:
            print("❌ No EDM events found in Chicago")
        
        # Test 3: Get Los Angeles EDM events
        print("\n📍 Test 3: Los Angeles EDM Events")
        print("-" * 30)
        
        la_events = await scraper.get_events_by_location("los-angeles", limit=5)
        
        if la_events:
            print(f"✅ Found {len(la_events)} EDM events in Los Angeles")
            
            for i, event in enumerate(la_events[:2], 1):
                print(f"\n{i}. {event.get('name', 'Unknown Event')}")
                print(f"   📅 Date: {event.get('date', 'TBD')}")
                print(f"   🏢 Venue: {event.get('venue', 'TBD')}")
        else:
            print("❌ No EDM events found in Los Angeles")
        
        # Test 4: Event details (if we have an event with ID)
        test_event = None
        for event in denver_events + chicago_events + la_events:
            if event.get('event_id'):
                test_event = event
                break
        
        if test_event:
            print(f"\n🔍 Test 4: Event Details")
            print("-" * 30)
            print(f"Getting details for: {test_event.get('name')}")
            
            details = await scraper.get_event_details(test_event['event_id'])
            
            if details:
                print("✅ Event details retrieved:")
                print(f"   📝 Description: {details.get('description', 'N/A')[:100]}...")
                print(f"   🖼️  Image: {details.get('image_url', 'N/A')}")
                print(f"   🎫 Tickets: {details.get('ticket_url', 'N/A')}")
            else:
                print("❌ Could not retrieve event details")
        
        # Save results to file
        all_events = denver_events + chicago_events + la_events
        
        if all_events:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"edmtrain_test_results_{timestamp}.json"
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump({
                    "test_date": datetime.now().isoformat(),
                    "total_events": len(all_events),
                    "denver_events": len(denver_events),
                    "chicago_events": len(chicago_events),
                    "la_events": len(la_events),
                    "events": all_events
                }, f, indent=2, ensure_ascii=False)
            
            print(f"\n💾 Results saved to: {filename}")
        
        # Summary
        print(f"\n📊 SUMMARY")
        print("=" * 50)
        print(f"Total EDM events found: {len(all_events)}")
        print(f"Denver: {len(denver_events)} events")
        print(f"Chicago: {len(chicago_events)} events")
        print(f"Los Angeles: {len(la_events)} events")
        
        if all_events:
            print("\n✅ EDM Train scraper is working!")
            
            # Show sample event structure
            print(f"\n📋 Sample Event Structure:")
            sample_event = all_events[0]
            for key, value in sample_event.items():
                if isinstance(value, list):
                    print(f"   {key}: {value[:2]}..." if len(value) > 2 else f"   {key}: {value}")
                elif isinstance(value, str) and len(value) > 50:
                    print(f"   {key}: {value[:50]}...")
                else:
                    print(f"   {key}: {value}")
        else:
            print("\n❌ No events found - check scraper implementation")

async def test_api_integration():
    """
    Test API integration if API key is available
    """
    api_key = os.environ.get('EDMTRAIN_API_KEY')
    
    if api_key:
        print(f"\n🔑 API Key found - testing API integration")
        print("-" * 40)
        
        async with EDMTrainScraper() as scraper:
            # Test API endpoints
            events = await scraper.get_events_by_location("denver", limit=5)
            
            if events:
                print(f"✅ API integration working - found {len(events)} events")
            else:
                print("❌ API integration failed or no events")
    else:
        print(f"\n⚠️  No EDMTRAIN_API_KEY found - using web scraping only")
        print("   To use API, set environment variable:")
        print("   export EDMTRAIN_API_KEY=your_api_key_here")

if __name__ == "__main__":
    print("Starting EDM Train scraper test...")
    
    try:
        asyncio.run(test_edmtrain_scraper())
        asyncio.run(test_api_integration())
        
        print(f"\n🎉 Test completed successfully!")
        
    except KeyboardInterrupt:
        print(f"\n⚠️  Test interrupted by user")
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()