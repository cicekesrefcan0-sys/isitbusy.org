#!/usr/bin/env python3
"""
Performance Test Suite
Tests the optimized application performance improvements
"""
import asyncio
import aiohttp
import time
import json
from datetime import datetime
import statistics

class PerformanceTest:
    def __init__(self):
        self.base_url = "http://localhost:8001/api"
        self.results = {}
        
    async def test_trending_venues_performance(self):
        """Test trending venues API performance"""
        print("🔥 Testing Trending Venues Performance...")
        
        endpoints = [
            "/trending/venues?limit=10",
            "/trending/venues?limit=20", 
            "/trending/weekly?limit=10",
            "/trending/monthly?limit=10"
        ]
        
        async with aiohttp.ClientSession() as session:
            for endpoint in endpoints:
                times = []
                
                # Test 10 requests
                for i in range(10):
                    start = time.time()
                    try:
                        async with session.get(f"{self.base_url}{endpoint}") as response:
                            if response.status == 200:
                                await response.json()
                                duration = time.time() - start
                                times.append(duration)
                                print(f"  Request {i+1}: {duration:.3f}s")
                            else:
                                print(f"  Request {i+1}: ERROR {response.status}")
                    except Exception as e:
                        print(f"  Request {i+1}: ERROR {e}")
                
                if times:
                    avg_time = statistics.mean(times)
                    min_time = min(times)
                    max_time = max(times)
                    
                    self.results[endpoint] = {
                        "avg_time": avg_time,
                        "min_time": min_time,
                        "max_time": max_time,
                        "requests": len(times)
                    }
                    
                    print(f"  📊 {endpoint}:")
                    print(f"     Average: {avg_time:.3f}s")
                    print(f"     Min: {min_time:.3f}s") 
                    print(f"     Max: {max_time:.3f}s")
                    
                    # Performance expectations
                    if avg_time < 1.0:
                        print(f"     ✅ EXCELLENT (< 1s)")
                    elif avg_time < 2.0:
                        print(f"     ✅ GOOD (< 2s)")
                    elif avg_time < 5.0:
                        print(f"     ⚠️  ACCEPTABLE (< 5s)")
                    else:
                        print(f"     ❌ SLOW (> 5s)")
                print()
    
    async def test_concurrent_requests(self):
        """Test concurrent request handling"""
        print("🚀 Testing Concurrent Request Performance...")
        
        endpoint = "/trending/venues?limit=10"
        concurrent_levels = [5, 10, 20, 50]
        
        async with aiohttp.ClientSession() as session:
            for concurrent in concurrent_levels:
                print(f"  Testing {concurrent} concurrent requests...")
                
                start_time = time.time()
                
                # Create concurrent requests
                tasks = []
                for i in range(concurrent):
                    task = session.get(f"{self.base_url}{endpoint}")
                    tasks.append(task)
                
                # Execute all requests concurrently
                try:
                    responses = await asyncio.gather(*tasks, return_exceptions=True)
                    total_time = time.time() - start_time
                    
                    success_count = 0
                    error_count = 0
                    
                    for response in responses:
                        if isinstance(response, Exception):
                            error_count += 1
                        else:
                            if response.status == 200:
                                success_count += 1
                                response.close()
                            else:
                                error_count += 1
                    
                    throughput = success_count / total_time if total_time > 0 else 0
                    
                    print(f"    Total time: {total_time:.3f}s")
                    print(f"    Success: {success_count}/{concurrent}")
                    print(f"    Errors: {error_count}")
                    print(f"    Throughput: {throughput:.1f} req/s")
                    
                    if throughput > 20:
                        print(f"    ✅ EXCELLENT throughput")
                    elif throughput > 10:
                        print(f"    ✅ GOOD throughput")
                    elif throughput > 5:
                        print(f"    ⚠️  ACCEPTABLE throughput")
                    else:
                        print(f"    ❌ LOW throughput")
                        
                except Exception as e:
                    print(f"    ❌ ERROR: {e}")
                
                print()
                
                # Wait between tests
                await asyncio.sleep(1)
    
    async def test_cache_performance(self):
        """Test cache hit performance"""
        print("💾 Testing Cache Performance...")
        
        endpoint = "/trending/venues?limit=10"
        
        async with aiohttp.ClientSession() as session:
            # First request (cache miss)
            print("  First request (cache miss)...")
            start = time.time()
            async with session.get(f"{self.base_url}{endpoint}") as response:
                if response.status == 200:
                    await response.json()
                    cache_miss_time = time.time() - start
                    print(f"    Cache miss: {cache_miss_time:.3f}s")
            
            # Second request (cache hit)
            print("  Second request (cache hit)...")
            start = time.time()
            async with session.get(f"{self.base_url}{endpoint}") as response:
                if response.status == 200:
                    await response.json()
                    cache_hit_time = time.time() - start
                    print(f"    Cache hit: {cache_hit_time:.3f}s")
            
            # Calculate improvement
            if cache_miss_time > 0:
                improvement = ((cache_miss_time - cache_hit_time) / cache_miss_time) * 100
                print(f"    Cache improvement: {improvement:.1f}%")
                
                if improvement > 80:
                    print(f"    ✅ EXCELLENT cache performance")
                elif improvement > 50:
                    print(f"    ✅ GOOD cache performance")
                elif improvement > 20:
                    print(f"    ⚠️  ACCEPTABLE cache performance")
                else:
                    print(f"    ❌ POOR cache performance")
        print()
    
    async def test_memory_usage(self):
        """Test memory usage patterns"""
        print("🧠 Testing Memory Usage...")
        
        try:
            import psutil
            import os
            
            # Get current process
            process = psutil.Process(os.getpid())
            initial_memory = process.memory_info().rss / 1024 / 1024  # MB
            
            print(f"  Initial memory: {initial_memory:.1f} MB")
            
            # Make multiple requests to test memory leaks
            async with aiohttp.ClientSession() as session:
                for i in range(50):
                    async with session.get(f"{self.base_url}/trending/venues?limit=20") as response:
                        if response.status == 200:
                            await response.json()
                    
                    if i % 10 == 9:
                        current_memory = process.memory_info().rss / 1024 / 1024
                        print(f"  After {i+1} requests: {current_memory:.1f} MB")
            
            final_memory = process.memory_info().rss / 1024 / 1024
            memory_increase = final_memory - initial_memory
            
            print(f"  Final memory: {final_memory:.1f} MB")
            print(f"  Memory increase: {memory_increase:.1f} MB")
            
            if memory_increase < 10:
                print(f"  ✅ EXCELLENT memory management")
            elif memory_increase < 50:
                print(f"  ✅ GOOD memory management")
            elif memory_increase < 100:
                print(f"  ⚠️  ACCEPTABLE memory usage")
            else:
                print(f"  ❌ HIGH memory usage")
                
        except ImportError:
            print("  ⚠️  psutil not available, skipping memory test")
        print()
    
    def generate_report(self):
        """Generate performance test report"""
        print("📋 Performance Test Report")
        print("=" * 50)
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Test Date: {timestamp}")
        print()
        
        if self.results:
            print("API Endpoint Performance:")
            for endpoint, metrics in self.results.items():
                print(f"  {endpoint}:")
                print(f"    Average Response Time: {metrics['avg_time']:.3f}s")
                print(f"    Min Response Time: {metrics['min_time']:.3f}s")
                print(f"    Max Response Time: {metrics['max_time']:.3f}s")
                print(f"    Successful Requests: {metrics['requests']}")
                print()
        
        # Save results to file
        report_file = f"performance_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(report_file, 'w') as f:
            json.dump({
                "timestamp": timestamp,
                "results": self.results
            }, f, indent=2)
        
        print(f"📄 Detailed report saved to: {report_file}")

async def main():
    """Run all performance tests"""
    print("🚀 Starting Performance Test Suite")
    print("=" * 50)
    
    tester = PerformanceTest()
    
    try:
        await tester.test_trending_venues_performance()
        await tester.test_concurrent_requests()
        await tester.test_cache_performance()
        await tester.test_memory_usage()
        
        tester.generate_report()
        
        print("✅ Performance tests completed!")
        
    except Exception as e:
        print(f"❌ Test suite failed: {e}")

if __name__ == "__main__":
    asyncio.run(main())