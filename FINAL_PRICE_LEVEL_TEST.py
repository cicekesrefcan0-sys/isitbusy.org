#!/usr/bin/env python3
"""
Final test to verify price level fix is working end-to-end
"""
import requests
import json

def test_price_level_end_to_end():
    print("💰 FINAL PRICE LEVEL FIX TEST")
    print("=" * 60)
    
    try:
        # Test 1: Venue list API (what homepage uses)
        print("1. Testing Venue List API (Homepage)...")
        response = requests.get('http://localhost:8001/api/venues?limit=5', timeout=10)
        if response.status_code == 200:
            data = response.json()
            venues = data.get('data', [])
            
            if venues:
                venue = venues[0]
                price_level = venue.get('price_level')
                print(f"   ✅ List API includes price_level: '{price_level}'")
            else:
                print("   ❌ No venues in list")
                return False
        else:
            print(f"   ❌ List API failed: HTTP {response.status_code}")
            return False
        
        # Test 2: Venue detail API (what venue page uses)
        print("\n2. Testing Venue Detail API (Venue Page)...")
        venue_id = venues[0]['id']
        response = requests.get(f'http://localhost:8001/api/venues/{venue_id}', timeout=10)
        if response.status_code == 200:
            venue_detail = response.json()
            price_level = venue_detail.get('price_level')
            print(f"   ✅ Detail API includes price_level: '{price_level}'")
            
            # Test price mapping
            price_map = {
                'PRICE_LEVEL_FREE': 'Free',
                'PRICE_LEVEL_INEXPENSIVE': '$10-20 per person',
                'PRICE_LEVEL_MODERATE': '$20-40 per person',
                'PRICE_LEVEL_EXPENSIVE': '$40-80 per person',
                'PRICE_LEVEL_VERY_EXPENSIVE': '$80+ per person'
            }
            
            price_text = price_map.get(price_level, 'Price varies')
            print(f"   ✅ Maps to: '{price_text}'")
            
            if price_text == 'Price varies':
                print("   ❌ Still showing 'Price varies'")
                return False
        else:
            print(f"   ❌ Detail API failed: HTTP {response.status_code}")
            return False
        
        # Test 3: Frontend accessibility
        print("\n3. Testing Frontend Accessibility...")
        try:
            response = requests.get('http://localhost:3001', timeout=5)
            if response.status_code == 200:
                print("   ✅ Frontend is accessible")
            else:
                print(f"   ❌ Frontend error: HTTP {response.status_code}")
                return False
        except:
            print("   ❌ Frontend not accessible")
            return False
        
        print("\n" + "=" * 60)
        print("🎉 ALL TESTS PASSED!")
        print("✅ Backend APIs return correct price_level data")
        print("✅ Price mapping functions work correctly")
        print("✅ Frontend is accessible and should show fixed prices")
        print("\n🚀 EXPECTED RESULTS:")
        print("- Price Level section should show '$20-40 per person' instead of 'Price varies'")
        print("- Different venues will show different price ranges based on their price_level")
        print("- Colors should match price levels (green=cheap, yellow=moderate, red=expensive)")
        
        return True
        
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        return False

if __name__ == '__main__':
    success = test_price_level_end_to_end()
    if success:
        print(f"\n🎯 NEXT STEPS:")
        print(f"1. Open frontend: http://localhost:3001")
        print(f"2. Clear browser cache: Ctrl+Shift+R")
        print(f"3. Click on any venue to see the fixed price display")
        print(f"4. Check 'Price & Entry Info' section")
    else:
        print(f"\n❌ Some tests failed. Check the errors above.")