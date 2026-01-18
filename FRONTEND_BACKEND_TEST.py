"""
Frontend-Backend Connection Test
Tests if frontend can successfully connect to backend APIs
"""
import requests
import json
from datetime import datetime

def test_frontend_backend_connection():
    """Test frontend-backend connection"""
    print("=" * 80)
    print("🔗 FRONTEND-BACKEND CONNECTION TEST")
    print("=" * 80)
    print(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 80)
    
    # Test frontend
    try:
        frontend_response = requests.get("http://localhost:3000", timeout=5)
        frontend_status = "✅ RUNNING" if frontend_response.status_code == 200 else f"❌ ERROR ({frontend_response.status_code})"
        print(f"Frontend (React)         | {frontend_status:<15} | Port 3000")
    except:
        print(f"Frontend (React)         | ❌ NOT RUNNING   | Port 3000")
        return False
    
    # Test backend
    try:
        backend_response = requests.get("http://localhost:8002/api/health", timeout=5)
        backend_status = "✅ RUNNING" if backend_response.status_code == 200 else f"❌ ERROR ({backend_response.status_code})"
        print(f"Backend (FastAPI)        | {backend_status:<15} | Port 8002")
    except:
        print(f"Backend (FastAPI)        | ❌ NOT RUNNING   | Port 8002")
        return False
    
    print("\n" + "=" * 80)
    print("🧪 API ENDPOINT TESTS FROM FRONTEND PERSPECTIVE")
    print("=" * 80)
    
    # Test the exact endpoints frontend would call
    frontend_api_calls = [
        {
            "name": "Get Venues",
            "url": "http://localhost:8002/api/venues",
            "expected_fields": ["data", "total"]
        },
        {
            "name": "Get Single Venue", 
            "url": "http://localhost:8002/api/venues/venue-1",
            "expected_fields": ["id", "name", "type"]
        },
        {
            "name": "Get Events",
            "url": "http://localhost:8002/api/eventbrite/events",
            "expected_fields": ["success", "events", "count"]
        },
        {
            "name": "Get After Parties",
            "url": "http://localhost:8002/api/eventbrite/after-parties", 
            "expected_fields": ["success", "events", "count"]
        },
        {
            "name": "Get News",
            "url": "http://localhost:8002/api/news",
            "expected_fields": ["data", "total"]
        }
    ]
    
    successful_calls = 0
    total_calls = len(frontend_api_calls)
    
    for api_call in frontend_api_calls:
        try:
            response = requests.get(api_call["url"], timeout=5)
            
            if response.status_code == 200:
                data = response.json()
                
                # Check if expected fields exist
                missing_fields = []
                for field in api_call["expected_fields"]:
                    if field not in data:
                        missing_fields.append(field)
                
                if not missing_fields:
                    print(f"{api_call['name']:<20} | ✅ SUCCESS       | All fields present")
                    successful_calls += 1
                else:
                    print(f"{api_call['name']:<20} | ⚠️ PARTIAL       | Missing: {', '.join(missing_fields)}")
            else:
                print(f"{api_call['name']:<20} | ❌ ERROR         | Status: {response.status_code}")
                
        except Exception as e:
            print(f"{api_call['name']:<20} | ❌ FAILED        | Error: {str(e)[:30]}...")
    
    print("\n" + "=" * 80)
    print("📊 CONNECTION TEST SUMMARY")
    print("=" * 80)
    print(f"Frontend Status:         {'✅ Running' if frontend_response.status_code == 200 else '❌ Not Running'}")
    print(f"Backend Status:          {'✅ Running' if backend_response.status_code == 200 else '❌ Not Running'}")
    print(f"API Calls Successful:    {successful_calls}/{total_calls}")
    print(f"Success Rate:            {(successful_calls/total_calls)*100:.1f}%")
    
    if successful_calls == total_calls:
        print("\n🎉 PERFECT! Frontend can successfully connect to all backend APIs!")
        print("✅ Users can now use the application without any connection issues.")
    elif successful_calls >= total_calls * 0.8:
        print("\n✅ GOOD! Most frontend-backend connections are working.")
        print("⚠️ Some minor issues may exist but core functionality works.")
    else:
        print("\n❌ ISSUES! Frontend-backend connection has problems.")
        print("🔧 Backend APIs need attention for proper frontend functionality.")
    
    print("=" * 80)
    
    return successful_calls == total_calls

if __name__ == "__main__":
    test_frontend_backend_connection()