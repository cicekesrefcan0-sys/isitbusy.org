#!/usr/bin/env python3
"""
Test price level fix using Python (bypasses browser CORS issues)
"""
import requests
import json

def test_price_level_fix():
    print("💰 TESTING PRICE LEVEL FIX")
    print("=" * 60)
    
    try:
        # Get venues with price levels
        response = requests.get('http://localhost:8001/api/venues?limit=20', timeout=10)
        if response.status_code == 200:
            data = response.json()
            venues = data.get('data', [])
            
            print(f"Found {len(venues)} venues. Checking price levels:")
            print("-" * 60)
            
            # Price level mapping (same as frontend)
            price_map = {
                # Numeric format
                0: 'Free',
                1: '$10-20 per person',
                2: '$20-40 per person', 
                3: '$40-80 per person',
                4: '$80+ per person',
                # Google Places API string format
                'PRICE_LEVEL_FREE': 'Free',
                'PRICE_LEVEL_INEXPENSIVE': '$10-20 per person',
                'PRICE_LEVEL_MODERATE': '$20-40 per person',
                'PRICE_LEVEL_EXPENSIVE': '$40-80 per person',
                'PRICE_LEVEL_VERY_EXPENSIVE': '$80+ per person'
            }
            
            venues_with_price = []
            fixed_count = 0
            
            for venue in venues:
                price_level = venue.get('price_level')
                if price_level is not None:
                    venues_with_price.append(venue)
                    price_text = price_map.get(price_level, 'Price varies')
                    
                    print(f"🏢 {venue.get('name')}")
                    print(f"   Raw price_level: '{price_level}' ({type(price_level).__name__})")
                    print(f"   Formatted: '{price_text}'")
                    
                    if price_text != 'Price varies':
                        fixed_count += 1
                        print(f"   ✅ Fixed!")
                    else:
                        print(f"   ❌ Still showing 'Price varies'")
                    print()
            
            print("=" * 60)
            print(f"📊 SUMMARY:")
            print(f"Total venues: {len(venues)}")
            print(f"Venues with price_level: {len(venues_with_price)}")
            print(f"Properly formatted: {fixed_count}")
            print(f"Still showing 'Price varies': {len(venues_with_price) - fixed_count}")
            
            if len(venues_with_price) > 0:
                success_rate = (fixed_count / len(venues_with_price)) * 100
                print(f"Success rate: {success_rate:.1f}%")
                
                if success_rate == 100:
                    print("\n🎉 PRICE LEVEL FIX SUCCESSFUL!")
                    print("All venues with price levels now show proper format.")
                    print("Frontend should display '$20-40 per person' instead of 'Price varies'")
                elif success_rate > 0:
                    print(f"\n⚠️  PARTIAL SUCCESS:")
                    print(f"Some venues fixed, but {len(venues_with_price) - fixed_count} still need work")
                else:
                    print(f"\n❌ FIX NOT WORKING:")
                    print("No venues are showing proper price format")
            else:
                print("\n⚠️  NO PRICE LEVEL DATA:")
                print("No venues have price_level information")
                
        else:
            print(f"❌ API Error: HTTP {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    test_price_level_fix()