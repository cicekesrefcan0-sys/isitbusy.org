#!/usr/bin/env python3
"""
Gerçek Colorado Etkinlikleri Test Scripti
Gerçek Colorado mekanları ve Eventbrite-style linklerle etkinlik oluşturur
"""
import asyncio
import sys
import os
import json
from datetime import datetime

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from services.eventbrite_real_scraper import (
    generate_real_colorado_events,
    test_real_scraper
)

async def test_realistic_colorado_events():
    """Gerçekçi Colorado etkinliklerini test et"""
    print("🚀 GERÇEK COLORADO ETKİNLİKLERİ TEST BAŞLADI")
    print("=" * 60)
    print("Bu test gerçek Colorado mekanları kullanarak")
    print("Eventbrite-style linklerle etkinlik oluşturur")
    print()
    
    try:
        # Test 1: Realistic event generator test
        print("1️⃣ Testing realistic event generator...")
        test_results = await test_real_scraper()
        print(f"✅ Event generator test completed")
        print(f"   Total events: {test_results['total_events']}")
        print(f"   Regular events: {test_results['regular_events']}")
        print(f"   After parties: {test_results['after_parties']}")
        
        if test_results['sample_event']:
            sample = test_results['sample_event']
            print(f"   Sample event:")
            print(f"     Title: {sample.get('title', 'N/A')}")
            print(f"     Venue: {sample.get('venue', 'N/A')}")
            print(f"     City: {sample.get('city', 'N/A')}")
            print(f"     URL: {sample.get('url', 'N/A')}")
            print(f"     Price: {sample.get('price_info', 'N/A')}")
            print(f"     Is After Party: {sample.get('is_after_party', False)}")
        
        # Test 2: Full Colorado event generation
        print(f"\n2️⃣ Generating ALL Colorado events...")
        
        generation_stats = await generate_real_colorado_events()
        print(f"✅ Event generation completed")
        print(f"   Cities processed: {generation_stats['cities_searched']}")
        print(f"   Total events generated: {generation_stats['total_events_found']}")
        print(f"   Regular events: {generation_stats['regular_events']}")
        print(f"   After parties: {generation_stats['after_parties']}")
        print(f"   Events saved to DB: {generation_stats['events_saved']}")
        print(f"   Errors: {generation_stats['errors']}")
        
        # Test 3: Verify saved data
        print(f"\n3️⃣ Verifying saved data...")
        from services.eventbrite_scraper import get_colorado_events, get_colorado_after_parties
        
        regular_events = await get_colorado_events('events', 20)
        after_parties = await get_colorado_after_parties(20)
        
        # Filter for realistic events
        real_regular = [e for e in regular_events if e.get('source') == 'eventbrite_real']
        real_after_parties = [e for e in after_parties if e.get('source') == 'eventbrite_real']
        
        print(f"✅ Data verification completed")
        print(f"   Realistic regular events in DB: {len(real_regular)}")
        print(f"   Realistic after parties in DB: {len(real_after_parties)}")
        
        # Show sample real events with real venues
        if real_regular:
            print(f"\n📋 Sample REALISTIC regular event:")
            sample = real_regular[0]
            print(f"   Title: {sample.get('title', 'N/A')}")
            print(f"   Venue: {sample.get('venue', 'N/A')} (REAL Colorado venue)")
            print(f"   City: {sample.get('city', 'N/A')}")
            print(f"   URL: {sample.get('url', 'N/A')} (Eventbrite-style)")
            print(f"   Price: {sample.get('price_info', 'N/A')}")
            print(f"   Source: {sample.get('source', 'N/A')}")
        
        if real_after_parties:
            print(f"\n🎉 Sample REALISTIC after party:")
            sample = real_after_parties[0]
            print(f"   Title: {sample.get('title', 'N/A')}")
            print(f"   Venue: {sample.get('venue', 'N/A')} (REAL Colorado venue)")
            print(f"   City: {sample.get('city', 'N/A')}")
            print(f"   URL: {sample.get('url', 'N/A')} (Eventbrite-style)")
            print(f"   Price: {sample.get('price_info', 'N/A')}")
            print(f"   Source: {sample.get('source', 'N/A')}")
        
        # Show real venues being used
        print(f"\n🏢 REAL COLORADO VENUES USED:")
        venues = set()
        for event in real_regular + real_after_parties:
            venues.add(f"{event.get('venue', 'N/A')} ({event.get('city', 'N/A')})")
        
        for venue in sorted(list(venues))[:10]:  # Show first 10
            print(f"   • {venue}")
        
        if len(venues) > 10:
            print(f"   ... and {len(venues) - 10} more venues")
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 GERÇEK COLORADO ETKİNLİKLERİ SUMMARY:")
        print(f"   Cities Processed: {generation_stats['cities_searched']}")
        print(f"   Total Realistic Events: {generation_stats['total_events_found']}")
        print(f"   Regular Events: {generation_stats['regular_events']}")
        print(f"   After Parties: {generation_stats['after_parties']}")
        print(f"   Successfully Saved: {generation_stats['events_saved']}")
        print(f"   Real Venues Used: {len(venues)}")
        print(f"   Errors: {generation_stats['errors']}")
        
        # Save results
        results = {
            'timestamp': datetime.now().isoformat(),
            'test_type': 'realistic_colorado_events',
            'test_results': test_results,
            'generation_stats': generation_stats,
            'real_regular_events_count': len(real_regular),
            'real_after_parties_count': len(real_after_parties),
            'real_venues_count': len(venues),
            'sample_real_event': real_regular[0] if real_regular else None,
            'sample_real_after_party': real_after_parties[0] if real_after_parties else None,
            'venues_used': list(venues)
        }
        
        with open('gercek_colorado_etkinlikleri_results.json', 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        print(f"\n💾 Results saved to: gercek_colorado_etkinlikleri_results.json")
        
        if generation_stats['total_events_found'] > 0:
            print("✅ GERÇEK COLORADO ETKİNLİKLERİ BAŞARIYLA OLUŞTURULDU!")
            print("\n🎯 NEXT STEPS:")
            print("1. Frontend'i başlatın:")
            print("   cd frontend && npm start")
            print("2. Events sayfasında gerçek Colorado mekanlarını görün")
            print("3. After Party sayfasında after party'leri kontrol edin")
            print("4. Eventbrite-style linklere tıklayın (yeni sekmede açılır)")
            print("5. API endpoints'leri test edin:")
            print("   curl http://localhost:8000/api/eventbrite/events")
            print("   curl http://localhost:8000/api/eventbrite/after-parties")
            print("\n🏢 GERÇEK COLORADO MEKANLARI:")
            print("   • Red Rocks Amphitheatre (Denver)")
            print("   • Ball Arena (Denver)")
            print("   • Boulder Theater (Boulder)")
            print("   • Pikes Peak Center (Colorado Springs)")
            print("   • ve daha fazlası...")
        else:
            print("❌ Etkinlik oluşturulamadı.")
        
        return results
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return None

async def test_api_endpoints():
    """API endpoints'leri test et"""
    print("\n🌐 TESTING REALISTIC DATA API ENDPOINTS")
    print("=" * 50)
    
    import httpx
    
    base_url = "http://localhost:8000/api/eventbrite"
    
    endpoints_to_test = [
        ("/test-real-scraper", "POST"),
        ("/scrape-real", "POST"),
        ("/events?limit=10", "GET"),
        ("/after-parties?limit=10", "GET"),
        ("/stats", "GET")
    ]
    
    async with httpx.AsyncClient() as client:
        for endpoint, method in endpoints_to_test:
            try:
                print(f"Testing {method} {base_url}{endpoint}")
                
                if method == "POST":
                    response = await client.post(f"{base_url}{endpoint}")
                else:
                    response = await client.get(f"{base_url}{endpoint}")
                
                if response.status_code == 200:
                    data = response.json()
                    if 'stats' in data:
                        print(f"✅ {endpoint}: {data['stats']}")
                    elif 'count' in data:
                        print(f"✅ {endpoint}: {data['count']} items")
                    else:
                        print(f"✅ {endpoint}: Success")
                else:
                    print(f"❌ {endpoint}: Status {response.status_code}")
                    
            except Exception as e:
                print(f"❌ {endpoint}: Error - {e}")

def main():
    """Main test function"""
    print("🚀 GERÇEK COLORADO ETKİNLİKLERİ ENTEGRASYON TESTİ")
    print("Bu test gerçek Colorado mekanlarını kullanır:")
    print("• Red Rocks Amphitheatre, Ball Arena, Boulder Theater")
    print("• Pikes Peak Center, Fox Theatre, Aggie Theatre")
    print("• ve daha fazla gerçek Colorado mekanı")
    print("Eventbrite-style linklerle yönlendirme yapar")
    print()
    
    # Run async tests
    results = asyncio.run(test_realistic_colorado_events())
    
    if results and results.get('generation_stats', {}).get('total_events_found', 0) > 0:
        print("\n🎯 BAŞARILI! Gerçek Colorado etkinlikleri oluşturuldu.")
        print("Frontend'de Events ve After Party sayfalarını kontrol edin.")
        print("Gerçek Colorado mekanlarını ve Eventbrite linklerini göreceksiniz.")
        
        # Test API endpoints if server is running
        try:
            print("\n🔄 Testing if server is running...")
            asyncio.run(test_api_endpoints())
        except:
            print("ℹ️  Server not running - start server to test API endpoints")
            print("   python backend/server.py")
    else:
        print("\n❌ Etkinlik oluşturulamadı.")

if __name__ == "__main__":
    main()