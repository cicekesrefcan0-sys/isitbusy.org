#!/usr/bin/env python3
"""
Check what data the venue detail API is returning
"""
import requests
import json

def check_venue_detail():
    print("🔍 CHECKING VENUE DETAIL API DATA")
    print("=" * 60)
    
    venue_id = "0551d9df-ea35-42e3-b70f-c22489e650e5"  # The Grizzly Rose
    
    try:
        response = requests.get(f'http://localhost:8001/api/venues/{venue_id}', timeout=10)
        if response.status_code == 200:
            venue_data = response.json()
            
            print(f"Venue: {venue_data.get('name')}")
            print(f"Type: {venue_data.get('type')}")
            print(f"Price Level: '{venue_data.get('price_level')}' (type: {type(venue_data.get('price_level'))})")
            
            print("\nFull venue data:")
            print(json.dumps(venue_data, indent=2))
            
            # Test the price mapping
            price_level = venue_data.get('price_level')
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
            
            price_text = price_map.get(price_level, 'Price varies')
            print(f"\nPrice mapping result: '{price_text}'")
            
            if price_text == 'Price varies':
                print("❌ Price level is not being mapped correctly!")
                print(f"Raw value: '{price_level}'")
                print("This explains why frontend shows 'Price varies'")
            else:
                print("✅ Price level mapping works correctly")
                
        else:
            print(f"❌ API Error: HTTP {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    check_venue_detail()