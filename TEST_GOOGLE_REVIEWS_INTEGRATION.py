#!/usr/bin/env python3
"""
Google Places Reviews Integration Test
Tests the complete Google Places Reviews system and daily updater
"""
import asyncio
import requests
import json
import time
from datetime import datetime
import sys
import os

# Add backend to path
sys.path.append('backend')

# Test configuration
BACKEND_URL = "http://localhost:8003"
TEST_VENUE_ID = "fallback-1"  # Red Rocks Amphitheatre

def print_header(title):
    """Print a formatted header"""
    print(f"\n{'='*60}")
    print(f"🧪 {title}")
    print(f"{'='*60}")

def print_step(step, description):
    """Print a test step"""
    print(f"\n{step}. {description}")
    print("-" * 40)

def test_backend_connection():
    """Test if backend is running"""
    print_step("1", "Testing Backend Connection")
    
    try:
        response = requests.get(f"{BACKEND_URL}/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Backend is running")
            print(f"   Status: {data.get('status')}")
            print(f"   Database: {data.get('database')}")
            return True
        else:
            print(f"❌ Backend returned status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Cannot connect to backend: {e}")
        print(f"   Make sure backend is running on {BACKEND_URL}")
        return False

def test_venue_reviews_endpoint():
    """Test venue reviews endpoint"""
    print_step("2", "Testing Venue Reviews Endpoint")
    
    try:
        response = requests.get(f"{BACKEND_URL}/api/venues/{TEST_VENUE_ID}/reviews", timeout=15)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Reviews endpoint working")
            print(f"   Success: {data.get('success')}")
            print(f"   Reviews count: {len(data.get('reviews', []))}")
            print(f"   Source: {data.get('source')}")
            print(f"   Rating: {data.get('rating')}")
            print(f"   Total ratings: {data.get('total_ratings')}")
            
            # Show sample review
            reviews = data.get('reviews', [])
            if reviews:
                sample_review = reviews[0]
                print(f"   Sample review by {sample_review.get('author_name')}: {sample_review.get('text', '')[:100]}...")
            
            return True, data
        else:
            print(f"❌ Reviews endpoint returned status {response.status_code}")
            return False, None
            
    except Exception as e:
        print(f"❌ Error testing reviews endpoint: {e}")
        return False, None

def test_refresh_reviews_endpoint():
    """Test refresh reviews endpoint"""
    print_step("3", "Testing Refresh Reviews Endpoint")
    
    try:
        response = requests.post(f"{BACKEND_URL}/api/venues/{TEST_VENUE_ID}/refresh-reviews", timeout=20)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Refresh reviews endpoint working")
            print(f"   Success: {data.get('success')}")
            print(f"   Reviews count: {len(data.get('reviews', []))}")
            print(f"   Rating: {data.get('rating')}")
            print(f"   Total ratings: {data.get('total_ratings')}")
            return True, data
        else:
            print(f"❌ Refresh endpoint returned status {response.status_code}")
            print(f"   Response: {response.text}")
            return False, None
            
    except Exception as e:
        print(f"❌ Error testing refresh endpoint: {e}")
        return False, None

def test_daily_updater_status():
    """Test daily updater status endpoint"""
    print_step("4", "Testing Daily Updater Status")
    
    try:
        response = requests.get(f"{BACKEND_URL}/api/admin/daily-updater/status", timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Daily updater status endpoint working")
            print(f"   Service running: {data.get('service_running')}")
            print(f"   Status: {data.get('status')}")
            print(f"   Next update: {data.get('next_update')}")
            
            latest_update = data.get('latest_update')
            if latest_update:
                stats = latest_update.get('stats', {})
                print(f"   Latest update: {latest_update.get('timestamp')}")
                print(f"   Venues processed: {stats.get('venues_processed', 0)}")
                print(f"   Venues updated: {stats.get('venues_updated', 0)}")
                print(f"   Reviews added: {stats.get('reviews_added', 0)}")
            else:
                print(f"   No previous updates found")
            
            return True, data
        else:
            print(f"❌ Status endpoint returned status {response.status_code}")
            return False, None
            
    except Exception as e:
        print(f"❌ Error testing status endpoint: {e}")
        return False, None

def test_manual_daily_update():
    """Test manual daily update trigger"""
    print_step("5", "Testing Manual Daily Update Trigger")
    
    try:
        print("🔄 Triggering manual daily update...")
        response = requests.post(f"{BACKEND_URL}/api/admin/daily-updater/run-now", timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Manual update triggered successfully")
            print(f"   Success: {data.get('success')}")
            print(f"   Message: {data.get('message')}")
            print(f"   Status: {data.get('status')}")
            
            # Wait a bit and check logs
            print("⏳ Waiting 10 seconds for update to process...")
            time.sleep(10)
            
            # Check logs
            logs_response = requests.get(f"{BACKEND_URL}/api/admin/daily-updater/logs?limit=1", timeout=10)
            if logs_response.status_code == 200:
                logs_data = logs_response.json()
                logs = logs_data.get('logs', [])
                if logs:
                    latest_log = logs[0]
                    stats = latest_log.get('stats', {})
                    print(f"📊 Latest update results:")
                    print(f"   Timestamp: {latest_log.get('timestamp')}")
                    print(f"   Venues processed: {stats.get('venues_processed', 0)}")
                    print(f"   Venues updated: {stats.get('venues_updated', 0)}")
                    print(f"   Reviews added: {stats.get('reviews_added', 0)}")
                    print(f"   Duration: {stats.get('duration_seconds', 0):.1f} seconds")
            
            return True, data
        else:
            print(f"❌ Manual update returned status {response.status_code}")
            print(f"   Response: {response.text}")
            return False, None
            
    except Exception as e:
        print(f"❌ Error testing manual update: {e}")
        return False, None

def test_frontend_integration():
    """Test frontend integration"""
    print_step("6", "Testing Frontend Integration")
    
    try:
        # Test venue page data
        response = requests.get(f"{BACKEND_URL}/api/venues/{TEST_VENUE_ID}", timeout=10)
        
        if response.status_code == 200:
            venue_data = response.json()
            print(f"✅ Venue data available for frontend")
            print(f"   Venue: {venue_data.get('name')}")
            print(f"   Rating: {venue_data.get('rating')}")
            print(f"   Website: {venue_data.get('website')}")
            
            # Check if venue has reviews
            if 'reviews' in venue_data:
                print(f"   Reviews in venue data: {len(venue_data['reviews'])}")
            
            return True, venue_data
        else:
            print(f"❌ Venue endpoint returned status {response.status_code}")
            return False, None
            
    except Exception as e:
        print(f"❌ Error testing frontend integration: {e}")
        return False, None

async def test_google_places_service():
    """Test Google Places Reviews service directly"""
    print_step("7", "Testing Google Places Reviews Service Directly")
    
    try:
        from services.google_places_reviews import GooglePlacesReviewsService, test_reviews_service
        
        print("🔄 Testing Google Places Reviews service...")
        success = await test_reviews_service()
        
        if success:
            print("✅ Google Places Reviews service working correctly")
            return True
        else:
            print("❌ Google Places Reviews service test failed")
            return False
            
    except Exception as e:
        print(f"❌ Error testing Google Places service: {e}")
        print(f"   Make sure GOOGLE_PLACES_API_KEY is set in environment")
        return False

async def test_daily_updater_service():
    """Test Daily Data Updater service directly"""
    print_step("8", "Testing Daily Data Updater Service Directly")
    
    try:
        from services.daily_data_updater import test_daily_updater
        
        print("🔄 Testing Daily Data Updater service...")
        success = await test_daily_updater()
        
        if success:
            print("✅ Daily Data Updater service working correctly")
            return True
        else:
            print("❌ Daily Data Updater service test failed")
            return False
            
    except Exception as e:
        print(f"❌ Error testing Daily Updater service: {e}")
        return False

def generate_test_report(results):
    """Generate a comprehensive test report"""
    print_header("TEST REPORT")
    
    total_tests = len(results)
    passed_tests = sum(1 for result in results.values() if result)
    failed_tests = total_tests - passed_tests
    
    print(f"📊 Test Results Summary:")
    print(f"   Total Tests: {total_tests}")
    print(f"   Passed: {passed_tests} ✅")
    print(f"   Failed: {failed_tests} ❌")
    print(f"   Success Rate: {(passed_tests/total_tests)*100:.1f}%")
    
    print(f"\n📋 Detailed Results:")
    for test_name, result in results.items():
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"   {test_name}: {status}")
    
    # Overall assessment
    if passed_tests == total_tests:
        print(f"\n🎉 ALL TESTS PASSED!")
        print(f"   Google Places Reviews integration is working perfectly")
        print(f"   Daily updater system is operational")
        print(f"   Frontend integration is ready")
    elif passed_tests >= total_tests * 0.8:
        print(f"\n✅ MOSTLY WORKING")
        print(f"   Most features are working correctly")
        print(f"   Some minor issues may need attention")
    else:
        print(f"\n⚠️ NEEDS ATTENTION")
        print(f"   Several issues detected")
        print(f"   Check failed tests and fix issues")
    
    return passed_tests == total_tests

async def main():
    """Run all tests"""
    print_header("Google Places Reviews Integration Test")
    print(f"🕒 Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"🎯 Testing backend at: {BACKEND_URL}")
    print(f"🏢 Test venue ID: {TEST_VENUE_ID}")
    
    results = {}
    
    # Test 1: Backend Connection
    results["Backend Connection"] = test_backend_connection()
    
    if not results["Backend Connection"]:
        print(f"\n❌ Cannot continue tests without backend connection")
        return False
    
    # Test 2: Venue Reviews Endpoint
    results["Venue Reviews Endpoint"], _ = test_venue_reviews_endpoint()
    
    # Test 3: Refresh Reviews Endpoint
    results["Refresh Reviews Endpoint"], _ = test_refresh_reviews_endpoint()
    
    # Test 4: Daily Updater Status
    results["Daily Updater Status"], _ = test_daily_updater_status()
    
    # Test 5: Manual Daily Update
    results["Manual Daily Update"], _ = test_manual_daily_update()
    
    # Test 6: Frontend Integration
    results["Frontend Integration"], _ = test_frontend_integration()
    
    # Test 7: Google Places Service (Direct)
    results["Google Places Service"] = await test_google_places_service()
    
    # Test 8: Daily Updater Service (Direct)
    results["Daily Updater Service"] = await test_daily_updater_service()
    
    # Generate report
    all_passed = generate_test_report(results)
    
    print(f"\n🕒 Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    return all_passed

if __name__ == "__main__":
    try:
        success = asyncio.run(main())
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print(f"\n⚠️ Test interrupted by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Test failed with error: {e}")
        sys.exit(1)