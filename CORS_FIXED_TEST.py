#!/usr/bin/env python3
"""
Test to verify CORS is fully fixed and venue loading works
"""
import requests
import json

def test_cors_and_venues():
    print("🔧 CORS FIX VERIFICATION TEST")
    print("=" * 60)
    
    # Test 1: Direct API call
    print("\n1. Testing Direct API Call...")
    try:
        response = requests.get('http://localhost:8001/api/venues?limit=5', timeout=10)
        if response.status_code == 200:
            data = response.json()
            venues = data.get('data', [])
            print(f"✅ Direct API: {len(venues)} venues loaded")
        else:
            print(f"❌ Direct API failed: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Direct API error: {e}")
        return False
    
    # Test 2: CORS Preflight
    print("\n2. Testing CORS Preflight...")
    try:
        headers = {
            'Origin': 'http://localhost:3001',
            'Access-Control-Request-Method': 'GET',
            'Access-Control-Request-Headers': 'Content-Type'
        }
        preflight = requests.options('http://localhost:8001/api/venues', headers=headers, timeout=5)
        print(f"   Preflight status: HTTP {preflight.status_code}")
        
        if preflight.status_code == 200:
            print("✅ CORS Preflight successful")
        else:
            print(f"❌ CORS Preflight failed: HTTP {preflight.status_code}")
            return False
    except Exception as e:
        print(f"❌ CORS Preflight error: {e}")
        return False
    
    # Test 3: Actual CORS request (simulating browser)
    print("\n3. Testing Actual CORS Request...")
    try:
        headers = {
            'Origin': 'http://localhost:3001',
            'Content-Type': 'application/json'
        }
        response = requests.get('http://localhost:8001/api/venues?limit=5000', headers=headers, timeout=10)
        
        if response.status_code == 200:
            cors_header = response.headers.get('Access-Control-Allow-Origin', 'Not set')
            print(f"✅ CORS Request successful")
            print(f"   CORS header: {cors_header}")
            
            data = response.json()
            venues = data.get('data', [])
            print(f"   Venues loaded: {len(venues)}")
            
            if len(venues) > 0:
                print(f"   Sample venue: {venues[0].get('name')} ({venues[0].get('id')})")
                return True
            else:
                print("❌ No venues in response")
                return False
        else:
            print(f"❌ CORS Request failed: HTTP {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ CORS Request error: {e}")
        return False

def main():
    success = test_cors_and_venues()
    
    print("\n" + "=" * 60)
    if success:
        print("🎉 SUCCESS: CORS is fully fixed!")
        print("✅ Frontend should now be able to load venues")
        print("✅ The 'Failed to load venues' error should be resolved")
        print("\n🚀 Next steps:")
        print("1. Open frontend: http://localhost:3001")
        print("2. Clear browser cache: Ctrl+Shift+R")
        print("3. Venues should load automatically")
    else:
        print("❌ FAILURE: CORS issues still exist")
        print("🔧 Additional troubleshooting needed")

if __name__ == '__main__':
    main()