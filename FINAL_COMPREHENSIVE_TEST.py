"""
Final Comprehensive Test - Tests all systems
Tests backend, frontend, database, and API connections
"""
import requests
import json
from datetime import datetime
import time

def test_all_systems():
    """Test all systems comprehensively"""
    print("=" * 100)
    print("🔬 FINAL COMPREHENSIVE SYSTEM TEST")
    print("=" * 100)
    print(f"Test Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 100)
    
    results = {
        "frontend": False,
        "backend": False,
        "api_endpoints": 0,
        "database": False,
        "total_score": 0
    }
    
    # 1. Test Frontend
    print("🌐 TESTING FRONTEND...")
    try:
        response = requests.get("http://localhost:3000", timeout=10)
        if response.status_code == 200:
            print("✅ Frontend is running on port 3000")
            results["frontend"] = True
        else:
            print(f"❌ Frontend error: {response.status_code}")
    except Exception as e:
        print(f"❌ Frontend not accessible: {str(e)}")
    
    # 2. Test Backend
    print("\n🔧 TESTING BACKEND...")
    try:
        response = requests.get("http://localhost:8002/api/health", timeout=5)
        if response.status_code == 200:
            print("✅ Backend is running on port 8002")
            results["backend"] = True
        else:
            print(f"❌ Backend error: {response.status_code}")
    except Exception as e:
        print(f"❌ Backend not accessible: {str(e)}")
    
    # 3. Test All API Endpoints
    print("\n📡 TESTING ALL API ENDPOINTS...")
    endpoints = [
        ("GET", "http://localhost:8002/", "Root"),
        ("GET", "http://localhost:8002/health", "Health Check"),
        ("GET", "http://localhost:8002/api/health", "API Health"),
        ("GET", "http://localhost:8002/api/venues", "Venues List"),
        ("GET", "http://localhost:8002/api/venues/venue-1", "Single Venue"),
        ("GET", "http://localhost:8002/api/eventbrite/events", "Events"),
        ("GET", "http://localhost:8002/api/eventbrite/after-parties", "After Parties"),
        ("GET", "http://localhost:8002/api/news", "News"),
        ("GET", "http://localhost:8002/api/trending/venues", "Trending"),
        ("GET", "http://localhost:8002/api/analytics", "Analytics"),
        ("GET", "http://localhost:8002/api/search", "Search")
    ]
    
    successful_endpoints = 0
    for method, url, name in endpoints:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"✅ {name:<15} - Working")
                successful_endpoints += 1
            else:
                print(f"❌ {name:<15} - Error {response.status_code}")
        except Exception as e:
            print(f"❌ {name:<15} - Failed: {str(e)[:30]}...")
    
    results["api_endpoints"] = successful_endpoints
    total_endpoints = len(endpoints)
    
    # 4. Test Database Connection
    print("\n🗄️ TESTING DATABASE...")
    try:
        # Test if we can connect to MongoDB through backend
        response = requests.get("http://localhost:8002/api/venues", timeout=5)
        if response.status_code == 200:
            data = response.json()
            if "data" in data and len(data["data"]) > 0:
                print("✅ Database connection working (venues data available)")
                results["database"] = True
            else:
                print("⚠️ Database connected but no data")
        else:
            print("❌ Cannot test database through API")
    except Exception as e:
        print(f"❌ Database test failed: {str(e)}")
    
    # 5. Test Frontend-Backend Integration
    print("\n🔗 TESTING FRONTEND-BACKEND INTEGRATION...")
    integration_score = 0
    if results["frontend"] and results["backend"]:
        print("✅ Both frontend and backend are running")
        integration_score += 1
        
        # Test if frontend can reach backend
        try:
            # Simulate frontend API call
            response = requests.get("http://localhost:8002/api/venues", 
                                  headers={"Origin": "http://localhost:3000"}, 
                                  timeout=5)
            if response.status_code == 200:
                print("✅ Frontend can successfully call backend APIs")
                integration_score += 1
            else:
                print("❌ Frontend-backend API calls failing")
        except Exception as e:
            print(f"❌ Frontend-backend integration error: {str(e)}")
    else:
        print("❌ Cannot test integration - frontend or backend not running")
    
    # Calculate total score
    max_score = 100
    score_breakdown = {
        "frontend": 20 if results["frontend"] else 0,
        "backend": 20 if results["backend"] else 0,
        "api_endpoints": int((successful_endpoints / total_endpoints) * 40),
        "database": 10 if results["database"] else 0,
        "integration": integration_score * 5
    }
    
    total_score = sum(score_breakdown.values())
    results["total_score"] = total_score
    
    # Print final results
    print("\n" + "=" * 100)
    print("📊 FINAL TEST RESULTS")
    print("=" * 100)
    
    print(f"🌐 Frontend Status:           {'✅ WORKING' if results['frontend'] else '❌ FAILED'} ({score_breakdown['frontend']}/20 points)")
    print(f"🔧 Backend Status:            {'✅ WORKING' if results['backend'] else '❌ FAILED'} ({score_breakdown['backend']}/20 points)")
    print(f"📡 API Endpoints:             {successful_endpoints}/{total_endpoints} working ({score_breakdown['api_endpoints']}/40 points)")
    print(f"🗄️ Database Connection:       {'✅ WORKING' if results['database'] else '❌ FAILED'} ({score_breakdown['database']}/10 points)")
    print(f"🔗 Frontend-Backend Integration: {integration_score}/2 tests passed ({score_breakdown['integration']}/10 points)")
    
    print(f"\n🎯 TOTAL SCORE: {total_score}/100")
    
    # Final verdict
    if total_score >= 90:
        print("\n🎉 EXCELLENT! System is working perfectly!")
        print("✅ All major components are functional")
        print("✅ Ready for production use")
        verdict = "EXCELLENT"
    elif total_score >= 75:
        print("\n✅ GOOD! System is mostly working!")
        print("✅ Core functionality is operational")
        print("⚠️ Minor issues may exist")
        verdict = "GOOD"
    elif total_score >= 50:
        print("\n⚠️ FAIR! System has some issues!")
        print("⚠️ Basic functionality works")
        print("🔧 Several components need attention")
        verdict = "FAIR"
    else:
        print("\n❌ POOR! System has major issues!")
        print("❌ Critical components are failing")
        print("🚨 Immediate attention required")
        verdict = "POOR"
    
    print("\n" + "=" * 100)
    print(f"FINAL VERDICT: {verdict} ({total_score}/100)")
    print("=" * 100)
    
    return results

if __name__ == "__main__":
    test_all_systems()