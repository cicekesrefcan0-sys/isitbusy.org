#!/usr/bin/env python3
"""
Scheduler Test Scripti
Otomatik scheduler'ın çalışıp çalışmadığını test eder
"""
import asyncio
import aiohttp
import json
import sys
from datetime import datetime

async def test_scheduler_api():
    """Scheduler API'sini test et"""
    print("🕐 SCHEDULER API TEST")
    print("=" * 50)
    
    base_url = "http://localhost:8001/api/scheduler"
    
    async with aiohttp.ClientSession() as session:
        
        # 1. Status kontrolü
        print("\n📊 1. Scheduler Status Test")
        print("-" * 30)
        try:
            async with session.get(f"{base_url}/status") as response:
                if response.status == 200:
                    data = await response.json()
                    scheduler = data.get("scheduler", {})
                    
                    print(f"✅ Status API çalışıyor")
                    print(f"   Scheduler Running: {scheduler.get('scheduler_running', False)}")
                    print(f"   Tasks: {len(scheduler.get('tasks', {}))}")
                    
                    # Task durumlarını göster
                    for task_name, task_info in scheduler.get('tasks', {}).items():
                        status = task_info.get('status', 'unknown')
                        last_run = task_info.get('last_run', 'Never')
                        print(f"   • {task_name}: {status} (Son: {last_run})")
                else:
                    print(f"❌ Status API hatası: {response.status}")
        except Exception as e:
            print(f"❌ Status API bağlantı hatası: {e}")
        
        # 2. Available tasks
        print("\n📋 2. Available Tasks Test")
        print("-" * 30)
        try:
            async with session.get(f"{base_url}/tasks") as response:
                if response.status == 200:
                    data = await response.json()
                    tasks = data.get("tasks", {})
                    
                    print(f"✅ Tasks API çalışıyor")
                    print(f"   Mevcut task sayısı: {len(tasks)}")
                    
                    for task_name, task_info in tasks.items():
                        print(f"   • {task_name}: {task_info.get('name', 'N/A')}")
                        print(f"     Schedule: {task_info.get('schedule', 'N/A')}")
                        print(f"     Duration: {task_info.get('duration', 'N/A')}")
                else:
                    print(f"❌ Tasks API hatası: {response.status}")
        except Exception as e:
            print(f"❌ Tasks API bağlantı hatası: {e}")
        
        # 3. Config test
        print("\n⚙️  3. Config Test")
        print("-" * 30)
        try:
            async with session.get(f"{base_url}/config") as response:
                if response.status == 200:
                    data = await response.json()
                    config = data.get("config", {})
                    
                    print(f"✅ Config API çalışıyor")
                    print(f"   Daily venue time: {config.get('daily_venue_time', 'N/A')}")
                    print(f"   Daily event time: {config.get('daily_event_time', 'N/A')}")
                    print(f"   Cache warm interval: {config.get('cache_warm_interval', 'N/A')} min")
                    print(f"   Enabled: {config.get('enabled', False)}")
                else:
                    print(f"❌ Config API hatası: {response.status}")
        except Exception as e:
            print(f"❌ Config API bağlantı hatası: {e}")
        
        # 4. Results test
        print("\n📈 4. Results Test")
        print("-" * 30)
        try:
            async with session.get(f"{base_url}/results?limit=5") as response:
                if response.status == 200:
                    data = await response.json()
                    results = data.get("results", [])
                    
                    print(f"✅ Results API çalışıyor")
                    print(f"   Son {len(results)} sonuç:")
                    
                    for result in results:
                        task_name = result.get("task_name", "Unknown")
                        timestamp = result.get("timestamp", "Unknown")
                        print(f"   • {task_name} - {timestamp}")
                else:
                    print(f"❌ Results API hatası: {response.status}")
        except Exception as e:
            print(f"❌ Results API bağlantı hatası: {e}")
        
        # 5. Health check
        print("\n🏥 5. Health Check Test")
        print("-" * 30)
        try:
            async with session.get(f"{base_url}/health") as response:
                if response.status == 200:
                    data = await response.json()
                    health = data.get("health", {})
                    
                    print(f"✅ Health API çalışıyor")
                    print(f"   Overall health: {health.get('overall_health', 'unknown')}")
                    print(f"   Scheduler running: {health.get('scheduler_running', False)}")
                    print(f"   Successful tasks: {health.get('last_successful_tasks', 0)}")
                    print(f"   Failed tasks: {health.get('failed_tasks', 0)}")
                else:
                    print(f"❌ Health API hatası: {response.status}")
        except Exception as e:
            print(f"❌ Health API bağlantı hatası: {e}")

async def test_manual_task_run():
    """Manuel task çalıştırma testi"""
    print("\n🔧 MANUEL TASK TEST")
    print("=" * 50)
    
    base_url = "http://localhost:8001/api/scheduler"
    
    # Cache warming task'ını test et (en hızlı olan)
    task_name = "hourly_cache_warm"
    
    async with aiohttp.ClientSession() as session:
        print(f"\n🚀 {task_name} manuel olarak çalıştırılıyor...")
        
        try:
            async with session.post(f"{base_url}/run/{task_name}") as response:
                if response.status == 200:
                    data = await response.json()
                    
                    print(f"✅ {task_name} başarıyla çalıştırıldı")
                    print(f"   Message: {data.get('message', 'N/A')}")
                    print(f"   Result: {data.get('result', 'N/A')}")
                    
                    return True
                else:
                    error_data = await response.text()
                    print(f"❌ {task_name} çalıştırma hatası: {response.status}")
                    print(f"   Error: {error_data}")
                    return False
                    
        except Exception as e:
            print(f"❌ {task_name} bağlantı hatası: {e}")
            return False

async def test_scheduler_control():
    """Scheduler start/stop testi"""
    print("\n🎛️  SCHEDULER CONTROL TEST")
    print("=" * 50)
    
    base_url = "http://localhost:8001/api/scheduler"
    
    async with aiohttp.ClientSession() as session:
        
        # Mevcut durumu kontrol et
        print("\n📊 Mevcut durum kontrol ediliyor...")
        try:
            async with session.get(f"{base_url}/status") as response:
                if response.status == 200:
                    data = await response.json()
                    is_running = data.get("scheduler", {}).get("scheduler_running", False)
                    print(f"   Scheduler durumu: {'Çalışıyor' if is_running else 'Durmuş'}")
                    
                    if not is_running:
                        # Scheduler'ı başlat
                        print("\n🚀 Scheduler başlatılıyor...")
                        async with session.post(f"{base_url}/start") as start_response:
                            if start_response.status == 200:
                                start_data = await start_response.json()
                                print(f"✅ Scheduler başlatıldı: {start_data.get('message', 'N/A')}")
                            else:
                                print(f"❌ Scheduler başlatma hatası: {start_response.status}")
                    else:
                        print("✅ Scheduler zaten çalışıyor")
                        
                else:
                    print(f"❌ Status kontrolü hatası: {response.status}")
                    
        except Exception as e:
            print(f"❌ Scheduler control bağlantı hatası: {e}")

def print_test_summary():
    """Test özeti"""
    print("\n" + "=" * 50)
    print("📋 SCHEDULER TEST ÖZETİ")
    print("=" * 50)
    print("\n✅ Test edilen özellikler:")
    print("   • Scheduler API endpoints")
    print("   • Task durumları")
    print("   • Konfigürasyon")
    print("   • Sonuç geçmişi")
    print("   • Sağlık kontrolü")
    print("   • Manuel task çalıştırma")
    print("   • Scheduler start/stop")
    
    print("\n🌐 Kontrol Paneli:")
    print("   • Web: SCHEDULER_KONTROL_PANELI.html")
    print("   • API: http://localhost:8001/api/scheduler/status")
    
    print("\n📋 Otomatik Schedule:")
    print("   • Venue güncelleme: Her gün 02:00")
    print("   • Event güncelleme: Her gün 03:00") 
    print("   • Cache warming: Her 30 dakika")
    print("   • Tam scraping: Her Pazar 01:00")
    print("   • Haber güncelleme: Her 60 dakika")

async def main():
    """Ana test fonksiyonu"""
    start_time = datetime.now()
    
    print("🕐 OTOMATIK SCHEDULER TEST BAŞLADI")
    print(f"Zaman: {start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 60)
    
    try:
        # API testleri
        await test_scheduler_api()
        
        # Manuel task testi
        await test_manual_task_run()
        
        # Scheduler control testi
        await test_scheduler_control()
        
        # Özet
        print_test_summary()
        
        duration = (datetime.now() - start_time).total_seconds()
        print(f"\n⏱️  Test süresi: {duration:.1f} saniye")
        print("\n🎉 Scheduler test tamamlandı!")
        
    except KeyboardInterrupt:
        print("\n⚠️  Test kullanıcı tarafından durduruldu")
    except Exception as e:
        print(f"\n❌ Test hatası: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    print("Scheduler test başlatılıyor...")
    print("Backend servisinin çalıştığından emin olun (http://localhost:8001)")
    print()
    
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Test başlatma hatası: {e}")
        sys.exit(1)