"""
Test Real Data Integration
Tests the new real data backend and compares with mock data
"""
import asyncio
import aiohttp
import json
from datetime import datetime
import sys
import os

async def test_backend(backend_url: str, backend_name: str):
    """Test a backend and return results"""
    print(f"\n🔧 TESTING {backend_name.upper()}")
    print(f"URL: {backend_url}")
    print("-" * 50)
    
    results = {
        'name': backend_name,
        'url': backend_url,
        'endpoints': {},
        'total_score': 0,
        'max_score': 0
    }
    
    endpoints = [
        {'path': '/health', 'name': 'Health Check'},
        {'path': '/api/venues', 'name': 'Venues List'},
        {'path': '/api/eventbrite/events', 'name': 'Events'},
        {'path': '/api/eventbrite/after-parties', 'name': 'After Parties'},
        {'path': '/api/trending/venues', 'name': 'Trending Venues'},
        {'path': '/api/analytics', 'name': 'Analytics'},
        {'path': '/api/news', 'name': 'News'}
    ]
    
    async with aiohttp.ClientSession() as session:
        for endpoint in endpoints:
            results['max_score'] += 1
            
            try:
                url = f"{backend_url}{endpoint['path']}"
                async with session.get(url, timeout=10) as response:
                    if response.status == 200:
                        data = await response.json()
                        
                        # Analyze response
                        analysis = analyze_response(endpoint['path'], data)
                        
                        results['endpoints'][endpoint['name']] = {
                            'status': 'SUCCESS',
                            'status_code': response.status,
                            'data_count': analysis['count'],
                            'data_source': analysis['source'],
                            'is_real_data': analysis['is_real'],
                            'details': analysis['details']
                        }
                        
                        results['total_score'] += 1
                        print(f"✅ {endpoint['name']}: {analysis['count']} items ({analysis['source']})")
                        
                    else:
                        results['endpoints'][endpoint['name']] = {
                            'status': 'ERROR',
                            'status_code': response.status,
                            'error': f"HTTP {response.status}"
                        }
                        print(f"❌ {endpoint['name']}: HTTP {response.status}")
                        
            except asyncio.TimeoutError:
                results['endpoints'][endpoint['name']] = {
                    'status': 'TIMEOUT',
                    'error': 'Request timeout'
                }
                print(f"⏰ {endpoint['name']}: Timeout")
                
            except Exception as e:
                results['endpoints'][endpoint['name']] = {
                    'status': 'ERROR',
                    'error': str(e)
                }
                print(f"❌ {endpoint['name']}: {str(e)}")
    
    success_rate = (results['total_score'] / results['max_score']) * 100
    print(f"\n📊 {backend_name} Success Rate: {success_rate:.1f}% ({results['total_score']}/{results['max_score']})")
    
    return results

def analyze_response(endpoint: str, data: dict) -> dict:
    """Analyze API response to determine data characteristics"""
    analysis = {
        'count': 0,
        'source': 'unknown',
        'is_real': False,
        'details': []
    }
    
    if endpoint == '/health':
        analysis['count'] = 1
        analysis['source'] = data.get('database', 'unknown')
        analysis['is_real'] = 'connected' in str(data.get('database', ''))
        
    elif endpoint == '/api/venues':
        venues = data.get('data', [])
        analysis['count'] = len(venues)
        analysis['source'] = data.get('source', 'unknown')
        analysis['is_real'] = 'real_data' in analysis['source'] or 'database' in analysis['source']
        
        if venues:
            # Check for real data indicators
            sample_venue = venues[0]
            if sample_venue.get('data_source') in ['google_places', 'database']:
                analysis['is_real'] = True
            
            # Count venues with websites
            with_websites = len([v for v in venues if v.get('website')])
            analysis['details'].append(f"{with_websites} venues have websites")
            
            # Count by city
            cities = {}
            for venue in venues:
                city = venue.get('city', 'Unknown')
                cities[city] = cities.get(city, 0) + 1
            analysis['details'].append(f"Cities: {', '.join(cities.keys())}")
            
    elif endpoint in ['/api/eventbrite/events', '/api/eventbrite/after-parties']:
        events = data.get('events', [])
        analysis['count'] = len(events)
        analysis['source'] = data.get('source', 'unknown')
        analysis['is_real'] = 'real_data' in analysis['source']
        
        if events:
            # Count by city
            cities = {}
            for event in events:
                city = event.get('city', 'Unknown')
                cities[city] = cities.get(city, 0) + 1
            analysis['details'].append(f"Cities: {', '.join(list(cities.keys())[:3])}")
            
    elif endpoint == '/api/trending/venues':
        venues = data.get('data', [])
        analysis['count'] = len(venues)
        analysis['source'] = data.get('source', 'unknown')
        analysis['is_real'] = 'real_data' in analysis['source']
        
    elif endpoint == '/api/analytics':
        analysis['count'] = data.get('total_venues', 0) + data.get('total_events', 0)
        analysis['source'] = data.get('source', 'unknown')
        analysis['is_real'] = 'real_data' in analysis['source']
        analysis['details'].append(f"Venues: {data.get('total_venues', 0)}")
        analysis['details'].append(f"Events: {data.get('total_events', 0)}")
        
    elif endpoint == '/api/news':
        news = data.get('data', [])
        analysis['count'] = len(news)
        analysis['source'] = data.get('source', 'unknown')
        analysis['is_real'] = 'real_data' in analysis['source']
    
    return analysis

async def compare_backends():
    """Compare mock data backend vs real data backend"""
    print("🔄 REAL DATA INTEGRATION TEST")
    print("=" * 60)
    print(f"Test Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    # Test both backends
    mock_results = await test_backend("http://localhost:8002", "Mock Data Backend")
    real_results = await test_backend("http://localhost:8003", "Real Data Backend")
    
    # Comparison
    print("\n" + "=" * 60)
    print("📊 COMPARISON RESULTS")
    print("=" * 60)
    
    comparison = {
        'mock_backend': mock_results,
        'real_backend': real_results,
        'improvements': [],
        'issues': []
    }
    
    # Compare each endpoint
    for endpoint_name in mock_results['endpoints']:
        mock_ep = mock_results['endpoints'].get(endpoint_name, {})
        real_ep = real_results['endpoints'].get(endpoint_name, {})
        
        print(f"\n🔍 {endpoint_name}:")
        
        # Data count comparison
        mock_count = mock_ep.get('data_count', 0)
        real_count = real_ep.get('data_count', 0)
        
        if real_count > mock_count:
            improvement = f"Data increased: {mock_count} → {real_count}"
            comparison['improvements'].append(f"{endpoint_name}: {improvement}")
            print(f"   ✅ {improvement}")
        elif real_count < mock_count:
            issue = f"Data decreased: {mock_count} → {real_count}"
            comparison['issues'].append(f"{endpoint_name}: {issue}")
            print(f"   ⚠️ {issue}")
        else:
            print(f"   ➡️ Data count unchanged: {real_count}")
        
        # Data source comparison
        mock_source = mock_ep.get('data_source', 'unknown')
        real_source = real_ep.get('data_source', 'unknown')
        
        if real_ep.get('is_real_data', False) and not mock_ep.get('is_real_data', False):
            improvement = f"Now using real data ({real_source})"
            comparison['improvements'].append(f"{endpoint_name}: {improvement}")
            print(f"   ✅ {improvement}")
        
        # Status comparison
        if mock_ep.get('status') == 'SUCCESS' and real_ep.get('status') != 'SUCCESS':
            issue = f"Endpoint broken: {real_ep.get('status', 'unknown')}"
            comparison['issues'].append(f"{endpoint_name}: {issue}")
            print(f"   ❌ {issue}")
    
    # Overall summary
    print("\n" + "=" * 60)
    print("🏁 FINAL SUMMARY")
    print("=" * 60)
    
    mock_success = (mock_results['total_score'] / mock_results['max_score']) * 100
    real_success = (real_results['total_score'] / real_results['max_score']) * 100
    
    print(f"Mock Backend Success Rate: {mock_success:.1f}%")
    print(f"Real Backend Success Rate: {real_success:.1f}%")
    
    if real_success >= mock_success:
        print("✅ Real data backend is working as well as mock backend!")
    else:
        print("⚠️ Real data backend has some issues to fix")
    
    print(f"\n🎯 IMPROVEMENTS ({len(comparison['improvements'])}):")
    for improvement in comparison['improvements']:
        print(f"   ✅ {improvement}")
    
    if comparison['issues']:
        print(f"\n⚠️ ISSUES TO FIX ({len(comparison['issues'])}):")
        for issue in comparison['issues']:
            print(f"   ❌ {issue}")
    
    # Save detailed results
    with open('real_data_integration_test_results.json', 'w') as f:
        json.dump(comparison, f, indent=2, default=str)
    
    print(f"\n📄 Detailed results saved to: real_data_integration_test_results.json")
    
    # Recommendations
    print("\n" + "=" * 60)
    print("💡 RECOMMENDATIONS")
    print("=" * 60)
    
    if real_results['endpoints'].get('Venues List', {}).get('data_count', 0) < 50:
        print("1. 🏢 Run venue population script:")
        print("   python POPULATE_REAL_DATA.py")
        print("   cd backend && python fetch_real_venues.py")
    
    if real_results['endpoints'].get('Events', {}).get('data_count', 0) < 10:
        print("2. 🎉 Run event scraping:")
        print("   python POPULATE_REAL_DATA.py")
    
    if real_success < 80:
        print("3. 🔧 Check database connection and API keys")
        print("4. 🔄 Restart real data backend")
    
    print("\n🚀 To use real data backend:")
    print("   python backend/real_data_backend.py")
    print("   Update frontend/.env to use port 8003")
    
    return comparison

async def main():
    """Main test function"""
    try:
        results = await compare_backends()
        
        # Quick status check
        real_backend = results['real_backend']
        if real_backend['total_score'] >= real_backend['max_score'] * 0.8:
            print("\n🎉 REAL DATA INTEGRATION SUCCESSFUL!")
            print("✅ Ready to replace mock data with real data")
        else:
            print("\n⚠️ REAL DATA INTEGRATION NEEDS WORK")
            print("🔧 Fix the issues above before switching to real data")
            
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        print("💡 Make sure both backends are running:")
        print("   Terminal 1: python backend/simple_backend_start.py")
        print("   Terminal 2: python backend/real_data_backend.py")

if __name__ == "__main__":
    asyncio.run(main())