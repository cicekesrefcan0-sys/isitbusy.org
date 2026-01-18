#!/usr/bin/env python3
"""
Quick diagnostic to identify the exact issue
"""
import requests
import json

def test_connectivity():
    print("🔍 QUICK DIAGNOSTIC - VENUE LOADING ISSUE")
    print("=" * 60)
    
    # Test backend API
    print("\n1. Testing Backend API...")
    try:
        response = requests.get('http://localhost:8001/api/venues?limit=1', timeout=5)
        if response.status_code == 200:
            data = response.json()
            venues = data.get('data', [])
            print(f"✅ Backend API working: {len(venues)} venues returned")
            if venues:
                venue = venues[0]
                print(f"   Sample venue: {venue.get('name')} ({venue.get('id')})")
        else:
            print(f"❌ Backend API error: HTTP {response.status_code}")
    except Exception as e:
        print(f"❌ Backend API connection failed: {e}")
    
    # Test frontend ports
    print("\n2. Testing Frontend Ports...")
    for port in [3000, 3001]:
        try:
            response = requests.get(f'http://localhost:{port}', timeout=3)
            if response.status_code == 200:
                print(f"✅ Frontend accessible on port {port}")
                print(f"   URL: http://localhost:{port}")
            else:
                print(f"⚠️  Port {port}: HTTP {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"❌ Port {port}: Not accessible")
        except Exception as e:
            print(f"❌ Port {port}: {e}")
    
    # Test CORS and API from frontend perspective
    print("\n3. Testing Frontend-to-Backend Connection...")
    try:
        # This simulates what the React app does
        headers = {
            'Origin': 'http://localhost:3001',
            'Access-Control-Request-Method': 'GET',
            'Access-Control-Request-Headers': 'Content-Type'
        }
        
        # Test preflight request
        preflight = requests.options('http://localhost:8001/api/venues', headers=headers, timeout=5)
        print(f"   CORS Preflight: HTTP {preflight.status_code}")
        
        # Test actual request
        api_response = requests.get('http://localhost:8001/api/venues?limit=1', 
                                  headers={'Origin': 'http://localhost:3001'}, timeout=5)
        if api_response.status_code == 200:
            print(f"✅ Frontend can access backend API")
            cors_headers = api_response.headers.get('Access-Control-Allow-Origin', 'Not set')
            print(f"   CORS header: {cors_headers}")
        else:
            print(f"❌ Frontend-to-backend failed: HTTP {api_response.status_code}")
            
    except Exception as e:
        print(f"❌ Frontend-to-backend connection failed: {e}")
    
    # Check environment configuration
    print("\n4. Checking Configuration...")
    try:
        with open('frontend/.env', 'r') as f:
            env_content = f.read()
            print(f"   Frontend .env: {env_content.strip()}")
    except Exception as e:
        print(f"   Could not read frontend/.env: {e}")
    
    print("\n" + "=" * 60)
    print("💡 SOLUTION RECOMMENDATIONS:")
    print("1. Make sure you're accessing the correct frontend URL:")
    print("   - Try: http://localhost:3001 (current frontend port)")
    print("   - Not: http://localhost:3000")
    print("2. Clear browser cache: Ctrl+Shift+R")
    print("3. Check browser console for errors (F12)")
    print("4. If still failing, restart both frontend and backend")

if __name__ == '__main__':
    test_connectivity()