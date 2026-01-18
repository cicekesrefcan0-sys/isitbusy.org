#!/usr/bin/env python3
"""
Gerçek Eventbrite Verileri Test Scripti
Web scraping ile gerçek Eventbrite etkinliklerini çeker ve test eder
"""
import asyncio
import sys
import os
import json
from datetime import datetime

# Add backend to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

from services.eventbrite_web_scraper import (
    scrape_real_eventbrite_data,
    test_web_scraper
)

async def test_real_eventbrite_data():
    """Gerçek Eventbrite verilerini test et"""
    print("🚀 GERÇEK EVENTBRITE VERİLERİ TEST BAŞLADI")
    print("=" * 60)
    print("Bu test gerçek Eventbrite web sitesinden veri çeker")
    print("Gerçek etkinlik linkleri ve bilgileri alır")
    print()
    
    try:
        # Test 1: Web scraper test (tek şehir)
        print("1️⃣ Testing web scraper (Denver only)...")
        test_results = await test_web_scraper()
        print(f"✅ Web scraper test completed")
        print(f"   Events found: {test_results['events_found']}")
        
        if test_results['sample_event']:
            sample = test_results['sample_event']
            print(f"   Sample event:")
            print(f"     Title: {sample.get('title', 'N/A')}")
            print(f"     Venue: {sample.get('venue', 'N/A')}")
            print(f"     City: {sample.get('city', 'N/A')}")
            print(f"     URL: {sample.get('url', 'N/A')}")
            print(f"     Is After Party: {sample.get('is_after_party', False)}")
            print(f"     Is Free: {sample.get('is_free', False)}")
        
        # Test 2: Full Colorado scraping
        print(f"\n2️⃣ Scraping ALL Colorado cities...")
        print("⏳ This may take a few minutes...")
        
        scrape_stats = await scrape_real_eventbrite_data()
        print(f"✅ Full scraping completed")
        print(f"   Cities searched: {scrape_stats['cities_searched']}")
        print(f"   Total events found: {scrape_stats['total_events_found']}")
        print(f"   Regular events: {scrape_stats['regular_events']}")
        print(f"   After parties: {scrape_stats['after_parties']}")
        print(f"   Events saved: {scrape_stats['events_saved']}")
        print(f"   Errors: {scrape_stats['errors']}")
        
        # Test 3: Verify saved data
        print(f"\n3️⃣ Verifying saved data...")
        from services.eventbrite_scraper import get_colorado_events, get_colorado_after_parties
        
        regular_events = await get_colorado_events('events', 10)
        after_parties = await get_colorado_after_parties(10)
        
        # Filter for web scraped events
        web_regular = [e for e in regular_events if e.get('source') == 'eventbrite_web']
        web_after_parties = [e for e in after_parties if e.get('source') == 'eventbrite_web']
        
        print(f"✅ Data verification completed")
        print(f"   Web scraped regular events: {len(web_regular)}")
        print(f"   Web scraped after parties: {len(web_after_parties)}")
        
        # Show sample real events
        if web_regular:
            print(f"\n📋 Sample REAL regular event:")
            sample = web_regular[0]
            print(f"   Title: {sample.get('title', 'N/A')}")
            print(f"   Venue: {sample.get('venue', 'N/A')}")
            print(f"   City: {sample.get('city', 'N/A')}")
            print(f"   URL: {sample.get('url', 'N/A')}")
            print(f"   Source: {sample.get('source', 'N/A')}")
        
        if web_after_parties:
            print(f"\n🎉 Sample REAL after party:")
            sample = web_after_parties[0]
            print(f"   Title: {sample.get('title', 'N/A')}")
            print(f"   Venue: {sample.get('venue', 'N/A')}")
            print(f"   City: {sample.get('city', 'N/A')}")
            print(f"   URL: {sample.get('url', 'N/A')}")
            print(f"   Source: {sample.get('source', 'N/A')}")
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 GERÇEK VERİ TEST SUMMARY:")
        print(f"   Cities Scraped: {scrape_stats['cities_searched']}")
        print(f"   Total Real Events: {scrape_stats['total_events_found']}")
        print(f"   Regular Events: {scrape_stats['regular_events']}")
        print(f"   After Parties: {scrape_stats['after_parties']}")
        print(f"   Successfully Saved: {scrape_stats['events_saved']}")
        print(f"   Errors: {scrape_stats['errors']}")
        
        # Save results
        results = {
            'timestamp': datetime.now().isoformat(),
            'test_type': 'real_eventbrite_web_scraping',
            'test_results': test_results,
            'scrape_stats': scrape_stats,
            'web_regular_events_count': len(web_regular),
            'web_after_parties_count': len(web_after_parties),
            'sample_real_event': web_regular[0] if web_regular else None,
            'sample_real_after_party': web_after_parties[0] if web_after_parties else None
        }
        
        with open('gercek_eventbrite_test_results.json', 'w') as f:
            json.dump(results, f, indent=2, default=str)
        
        print(f"\n💾 Results saved to: gercek_eventbrite_test_results.json")
        
        if scrape_stats['total_events_found'] > 0:
            print("✅ GERÇEK VERİLER BAŞARIYLA ÇEKİLDİ!")
            print("\n🎯 NEXT STEPS:")
            print("1. Frontend'i başlatın ve Events/After Party sayfalarını kontrol edin")
            print("2. Gerçek Eventbrite linklerine tıklayarak yönlendirmeyi test edin")
            print("3. API endpoints'leri test edin:")
            print("   curl http://localhost:8000/api/eventbrite/events")
            print("   curl http://localhost:8000/api/eventbrite/after-parties")
        else:
            print("⚠️  Hiç gerçek veri çekilemedi. Eventbrite sitesi değişmiş olabilir.")
            print("Demo verilerle devam edebilirsiniz.")
        
        return results
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return None

async def test_api_endpoints():
    """API endpoints'leri test et"""
    print("\n🌐 TESTING REAL DATA API ENDPOINTS")
    print("=" * 40)
    
    import httpx
    
    base_url = "http://localhost:8000/api/eventbrite"
    
    endpoints_to_test = [
        ("/test-web-scraper", "POST"),
        ("/scrape-real", "POST"),
        ("/events?limit=5", "GET"),
        ("/after-parties?limit=5", "GET"),
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
    print("🚀 GERÇEK EVENTBRITE VERİLERİ ENTEGRASYON TESTİ")
    print("Bu test gerçek Eventbrite web sitesinden veri çeker")
    print("Gerçek etkinlik linkleri ve after party tespiti yapar")
    print()
    
    # Run async tests
    results = asyncio.run(test_real_eventbrite_data())
    
    if results and results.get('scrape_stats', {}).get('total_events_found', 0) > 0:
        print("\n🎯 BAŞARILI! Gerçek veriler çekildi.")
        print("Frontend'de Events ve After Party sayfalarını kontrol edin.")
        
        # Test API endpoints if server is running
        try:
            print("\n🔄 Testing if server is running...")
            asyncio.run(test_api_endpoints())
        except:
            print("ℹ️  Server not running - start server to test API endpoints")
            print("   python backend/server.py")
    else:
        print("\n⚠️  Gerçek veri çekilemedi, demo verilerle devam edin.")

if __name__ == "__main__":
    main()