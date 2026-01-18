"""
API Test Script - Test all backend endpoints
Tests the simple backend server to ensure all APIs are working
"""
import requests
import json
from datetime import datetime

# Backend URL
BACKEND_URL = "http://localhost:8002"

def test_endpoint(method, url, description):
    """Test a single endpoint"""
    try:
        if method.upper() == "GET":
            response = requests.get(url, timeout=5)
        elif method.upper() == "POST":
            response = requests.post(url, timeout=5)
        
        status = "✅ SUCCESS" if response.status_code == 200 else f"❌ ERROR ({response.status_code})"
        
        print(f"{description:<30} | {status:<15} | {response.status_code}")
        
        if response.status_code == 200:
            try:
                data = response.json()
                if isinstance(data, dict):
                    if 'message' in data:
                        print(f"{'':>30} | Message: {data['message']}")
                    if 'total' in data:
                        print(f"{'':>30} | Total items: {data['total']}")
                    if 'count' in data:
                        print(f"{'':>30} | Count: {data['count']}")
            except:
                pass
        
        return response.status_code == 200
        
    except requests.exceptions.RequestException as e:
        print(f"{description:<30} | ❌ ERROR      | Connection failed: {str(e)}")
        return False

def main():
    print("=" * 80)
    print("🔧 BACKEND API TESTS")
    print("=" * 80)
    print(f"Testing backend at: {BACKEND_URL}")
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    # Test endpoints
    endpoints = [
        ("GET", f"{BACKEND_URL}/", "Root Endpoint"),
        ("GET", f"{BACKEND_URL}/health", "Health Check"),
        ("GET", f"{BACKEND_URL}/api/health", "API Health Check"),
        ("GET", f"{BACKEND_URL}/api/venues", "Venues List"),
        ("GET", f"{BACKEND_URL}/api/venues/venue-1", "Single Venue"),
        ("GET", f"{BACKEND_URL}/api/eventbrite/events", "Eventbrite Events"),
        ("GET", f"{BACKEND_URL}/api/eventbrite/after-parties", "After Parties"),
        ("GET", f"{BACKEND_URL}/api/news", "News"),
        ("GET", f"{BACKEND_URL}/api/trending/venues", "Trending Venues"),
        ("GET", f"{BACKEND_URL}/api/analytics", "Analytics"),
        ("GET", f"{BACKEND_URL}/api/search", "Search"),
    ]
    
    successful = 0
    total = len(endpoints)
    
    for method, url, description in endpoints:
        if test_endpoint(method, url, description):
            successful += 1
        print()
    
    print("=" * 80)
    print("📊 SUMMARY")
    print("=" * 80)
    print(f"Total Tests: {total}")
    print(f"Successful: {successful}")
    print(f"Failed: {total - successful}")
    print(f"Success Rate: {(successful/total)*100:.1f}%")
    
    if successful == total:
        print("🎉 ALL TESTS PASSED! Backend is working perfectly!")
    elif successful >= total * 0.8:
        print("✅ Most tests passed! Backend is mostly working.")
    else:
        print("⚠️ Many tests failed. Backend needs attention.")
    
    print("=" * 80)

if __name__ == "__main__":
    main()