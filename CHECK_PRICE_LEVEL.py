#!/usr/bin/env python3
"""
Check what price_level values are in the venue data
"""
import requests
import json

def check_price_levels():
    print("🔍 CHECKING VENUE PRICE LEVELS")
    print("=" * 60)
    
    try:
        # Get a few venues to check their price_level values
        response = requests.get('http://localhost:8001/api/venues?limit=10', timeout=10)
        if response.status_code == 200:
            data = response.json()
            venues = data.get('data', [])
            
            print(f"Found {len(venues)} venues. Checking price_level values:")
            print("-" * 60)
            
            price_level_counts = {}
            
            for i, venue in enumerate(venues[:5], 1):
                price_level = venue.get('price_level')
                print(f"{i}. {venue.get('name')}")
                print(f"   price_level: {price_level} (type: {type(price_level)})")
                
                # Count occurrences
                if price_level in price_level_counts:
                    price_level_counts[price_level] += 1
                else:
                    price_level_counts[price_level] = 1
                
                # Also check a specific venue detail
                if i == 1:
                    detail_response = requests.get(f'http://localhost:8001/api/venues/{venue.get("id")}', timeout=5)
                    if detail_response.status_code == 200:
                        detail_data = detail_response.json()
                        detail_price_level = detail_data.get('price_level')
                        print(f"   Detail page price_level: {detail_price_level} (type: {type(detail_price_level)})")
                
                print()
            
            print("Price Level Summary:")
            print("-" * 60)
            for price_level, count in price_level_counts.items():
                print(f"'{price_level}': {count} venues")
                
        else:
            print(f"❌ API Error: HTTP {response.status_code}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == '__main__':
    check_price_levels()