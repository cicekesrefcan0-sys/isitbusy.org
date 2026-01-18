@echo off
echo ========================================
echo 🕐 OTOMATIK SCHEDULER KURULUM
echo ========================================
echo.

echo 📋 1. Gerekli Python paketlerini yüklüyor...
pip install schedule

echo.
echo 📋 2. Scheduler servisini backend'e entegre ediyor...
cd backend

echo.
echo 📋 3. Server.py'ye scheduler route'u ekleniyor...
python -c "
import re

# Read server.py
try:
    with open('server.py', 'r', encoding='utf-8') as f:
        content = f.read()
except:
    print('❌ server.py bulunamadı')
    exit(1)

# Check if scheduler route already exists
if 'from routes import scheduler' not in content:
    # Add import
    if 'from routes import' in content:
        content = re.sub(r'(from routes import [^\\n]+)', r'\1, scheduler', content)
    else:
        # Find a good place to add import
        lines = content.split('\\n')
        for i, line in enumerate(lines):
            if 'from routes import' in line:
                lines.insert(i+1, 'from routes import scheduler')
                break
        content = '\\n'.join(lines)
    
    # Add router
    if 'app.include_router(' in content:
        # Find last router include
        lines = content.split('\\n')
        last_router_line = -1
        for i, line in enumerate(lines):
            if 'app.include_router(' in line:
                last_router_line = i
        
        if last_router_line >= 0:
            lines.insert(last_router_line + 1, 'app.include_router(scheduler.router)')
            content = '\\n'.join(lines)
    
    # Write back
    with open('server.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print('✅ Scheduler route server.py\\'ye eklendi')
else:
    print('✅ Scheduler route zaten mevcut')
"

echo.
echo 📋 4. Scheduler'ı server startup'a ekleniyor...
python -c "
import re

# Read server.py
with open('server.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add scheduler startup
if 'start_auto_scheduler' not in content:
    # Add import
    if 'from services.auto_scheduler import start_auto_scheduler' not in content:
        # Find imports section
        lines = content.split('\\n')
        for i, line in enumerate(lines):
            if line.startswith('from services') or line.startswith('import'):
                lines.insert(i, 'from services.auto_scheduler import start_auto_scheduler')
                break
        content = '\\n'.join(lines)
    
    # Add startup event
    startup_code = '''
@app.on_event(\"startup\")
async def startup_event():
    \"\"\"Application startup\"\"\"
    await start_auto_scheduler()
'''
    
    if '@app.on_event(\"startup\")' not in content:
        # Add before main
        content = content.replace('if __name__ == \"__main__\":', startup_code + '\\nif __name__ == \"__main__\":')
    
    # Write back
    with open('server.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print('✅ Scheduler startup event eklendi')
else:
    print('✅ Scheduler startup zaten mevcut')
"

echo.
echo 📋 5. Database collection'ları oluşturuluyor...
python -c "
import asyncio
from database import db

async def create_scheduler_collections():
    try:
        # Create scheduler_results collection
        await db.create_collection('scheduler_results')
        
        # Create indexes
        await db.scheduler_results.create_index('task_name')
        await db.scheduler_results.create_index('timestamp')
        await db.scheduler_results.create_index([('task_name', 1), ('timestamp', -1)])
        
        print('✅ Scheduler database collections oluşturuldu')
    except Exception as e:
        print(f'⚠️  Collection zaten mevcut olabilir: {e}')

asyncio.run(create_scheduler_collections())
"

echo.
echo 📋 6. Scheduler test sayfası oluşturuluyor...
cd ..

echo ^<!DOCTYPE html^> > SCHEDULER_KONTROL_PANELI.html
echo ^<html^> >> SCHEDULER_KONTROL_PANELI.html
echo ^<head^> >> SCHEDULER_KONTROL_PANELI.html
echo     ^<title^>Scheduler Kontrol Paneli^</title^> >> SCHEDULER_KONTROL_PANELI.html
echo     ^<style^> >> SCHEDULER_KONTROL_PANELI.html
echo         body { font-family: Arial, sans-serif; margin: 20px; background: #f5f5f5; } >> SCHEDULER_KONTROL_PANELI.html
echo         .container { max-width: 1200px; margin: 0 auto; } >> SCHEDULER_KONTROL_PANELI.html
echo         .card { background: white; padding: 20px; margin: 10px 0; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); } >> SCHEDULER_KONTROL_PANELI.html
echo         .status { padding: 5px 10px; border-radius: 4px; color: white; font-weight: bold; } >> SCHEDULER_KONTROL_PANELI.html
echo         .running { background: #22c55e; } >> SCHEDULER_KONTROL_PANELI.html
echo         .stopped { background: #ef4444; } >> SCHEDULER_KONTROL_PANELI.html
echo         .completed { background: #3b82f6; } >> SCHEDULER_KONTROL_PANELI.html
echo         .error { background: #f59e0b; } >> SCHEDULER_KONTROL_PANELI.html
echo         button { padding: 10px 20px; margin: 5px; cursor: pointer; border: none; border-radius: 4px; } >> SCHEDULER_KONTROL_PANELI.html
echo         .btn-primary { background: #3b82f6; color: white; } >> SCHEDULER_KONTROL_PANELI.html
echo         .btn-success { background: #22c55e; color: white; } >> SCHEDULER_KONTROL_PANELI.html
echo         .btn-danger { background: #ef4444; color: white; } >> SCHEDULER_KONTROL_PANELI.html
echo         .task-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 15px; } >> SCHEDULER_KONTROL_PANELI.html
echo         .log { background: #1f2937; color: #f3f4f6; padding: 15px; border-radius: 4px; font-family: monospace; max-height: 300px; overflow-y: auto; } >> SCHEDULER_KONTROL_PANELI.html
echo     ^</style^> >> SCHEDULER_KONTROL_PANELI.html
echo ^</head^> >> SCHEDULER_KONTROL_PANELI.html
echo ^<body^> >> SCHEDULER_KONTROL_PANELI.html
echo     ^<div class="container"^> >> SCHEDULER_KONTROL_PANELI.html
echo         ^<h1^>🕐 Otomatik Scheduler Kontrol Paneli^</h1^> >> SCHEDULER_KONTROL_PANELI.html
echo. >> SCHEDULER_KONTROL_PANELI.html
echo         ^<div class="card"^> >> SCHEDULER_KONTROL_PANELI.html
echo             ^<h2^>Scheduler Durumu^</h2^> >> SCHEDULER_KONTROL_PANELI.html
echo             ^<div id="scheduler-status"^>Yükleniyor...^</div^> >> SCHEDULER_KONTROL_PANELI.html
echo             ^<div style="margin-top: 15px;"^> >> SCHEDULER_KONTROL_PANELI.html
echo                 ^<button class="btn-success" onclick="startScheduler()"^>Başlat^</button^> >> SCHEDULER_KONTROL_PANELI.html
echo                 ^<button class="btn-danger" onclick="stopScheduler()"^>Durdur^</button^> >> SCHEDULER_KONTROL_PANELI.html
echo                 ^<button class="btn-primary" onclick="refreshStatus()"^>Yenile^</button^> >> SCHEDULER_KONTROL_PANELI.html
echo             ^</div^> >> SCHEDULER_KONTROL_PANELI.html
echo         ^</div^> >> SCHEDULER_KONTROL_PANELI.html
echo. >> SCHEDULER_KONTROL_PANELI.html
echo         ^<div class="card"^> >> SCHEDULER_KONTROL_PANELI.html
echo             ^<h2^>Görevler^</h2^> >> SCHEDULER_KONTROL_PANELI.html
echo             ^<div id="tasks" class="task-grid"^>^</div^> >> SCHEDULER_KONTROL_PANELI.html
echo         ^</div^> >> SCHEDULER_KONTROL_PANELI.html
echo. >> SCHEDULER_KONTROL_PANELI.html
echo         ^<div class="card"^> >> SCHEDULER_KONTROL_PANELI.html
echo             ^<h2^>Son Sonuçlar^</h2^> >> SCHEDULER_KONTROL_PANELI.html
echo             ^<div id="results"^>^</div^> >> SCHEDULER_KONTROL_PANELI.html
echo         ^</div^> >> SCHEDULER_KONTROL_PANELI.html
echo. >> SCHEDULER_KONTROL_PANELI.html
echo         ^<div class="card"^> >> SCHEDULER_KONTROL_PANELI.html
echo             ^<h2^>Loglar^</h2^> >> SCHEDULER_KONTROL_PANELI.html
echo             ^<div id="logs" class="log"^>^</div^> >> SCHEDULER_KONTROL_PANELI.html
echo         ^</div^> >> SCHEDULER_KONTROL_PANELI.html
echo     ^</div^> >> SCHEDULER_KONTROL_PANELI.html
echo. >> SCHEDULER_KONTROL_PANELI.html
echo     ^<script^> >> SCHEDULER_KONTROL_PANELI.html
echo         const API_BASE = 'http://localhost:8001/api/scheduler'; >> SCHEDULER_KONTROL_PANELI.html
echo. >> SCHEDULER_KONTROL_PANELI.html
echo         async function refreshStatus() { >> SCHEDULER_KONTROL_PANELI.html
echo             try { >> SCHEDULER_KONTROL_PANELI.html
echo                 const response = await fetch(`${API_BASE}/status`); >> SCHEDULER_KONTROL_PANELI.html
echo                 const data = await response.json(); >> SCHEDULER_KONTROL_PANELI.html
echo                 displayStatus(data.scheduler); >> SCHEDULER_KONTROL_PANELI.html
echo                 displayTasks(data.scheduler.tasks); >> SCHEDULER_KONTROL_PANELI.html
echo                 await loadResults(); >> SCHEDULER_KONTROL_PANELI.html
echo             } catch (error) { >> SCHEDULER_KONTROL_PANELI.html
echo                 console.error('Status yükleme hatası:', error); >> SCHEDULER_KONTROL_PANELI.html
echo                 document.getElementById('scheduler-status').innerHTML = '^<span class="status error"^>HATA^</span^> Bağlantı hatası'; >> SCHEDULER_KONTROL_PANELI.html
echo             } >> SCHEDULER_KONTROL_PANELI.html
echo         } >> SCHEDULER_KONTROL_PANELI.html
echo. >> SCHEDULER_KONTROL_PANELI.html
echo         function displayStatus(scheduler) { >> SCHEDULER_KONTROL_PANELI.html
echo             const statusEl = document.getElementById('scheduler-status'); >> SCHEDULER_KONTROL_PANELI.html
echo             const isRunning = scheduler.scheduler_running; >> SCHEDULER_KONTROL_PANELI.html
echo             const statusClass = isRunning ? 'running' : 'stopped'; >> SCHEDULER_KONTROL_PANELI.html
echo             const statusText = isRunning ? 'ÇALIŞIYOR' : 'DURMUŞ'; >> SCHEDULER_KONTROL_PANELI.html
echo             statusEl.innerHTML = `^<span class="status ${statusClass}"^>${statusText}^</span^> Son güncelleme: ${new Date().toLocaleString()}`; >> SCHEDULER_KONTROL_PANELI.html
echo         } >> SCHEDULER_KONTROL_PANELI.html
echo. >> SCHEDULER_KONTROL_PANELI.html
echo         function displayTasks(tasks) { >> SCHEDULER_KONTROL_PANELI.html
echo             const tasksEl = document.getElementById('tasks'); >> SCHEDULER_KONTROL_PANELI.html
echo             tasksEl.innerHTML = Object.entries(tasks).map(([name, task]) =^> `^<div class="card"^>^<h3^>${name}^</h3^>^<p^>Durum: ^<span class="status ${task.status}"^>${task.status}^</span^>^</p^>^<p^>Son çalışma: ${task.last_run ^|^| 'Hiç'}^</p^>^<p^>Sonraki: ${task.next_run ^|^| 'Bilinmiyor'}^</p^>^<button class="btn-primary" onclick="runTask('${name}')"^>Manuel Çalıştır^</button^>^</div^>`).join(''); >> SCHEDULER_KONTROL_PANELI.html
echo         } >> SCHEDULER_KONTROL_PANELI.html
echo. >> SCHEDULER_KONTROL_PANELI.html
echo         async function startScheduler() { >> SCHEDULER_KONTROL_PANELI.html
echo             try { >> SCHEDULER_KONTROL_PANELI.html
echo                 await fetch(`${API_BASE}/start`, { method: 'POST' }); >> SCHEDULER_KONTROL_PANELI.html
echo                 await refreshStatus(); >> SCHEDULER_KONTROL_PANELI.html
echo             } catch (error) { >> SCHEDULER_KONTROL_PANELI.html
echo                 alert('Scheduler başlatma hatası: ' + error.message); >> SCHEDULER_KONTROL_PANELI.html
echo             } >> SCHEDULER_KONTROL_PANELI.html
echo         } >> SCHEDULER_KONTROL_PANELI.html
echo. >> SCHEDULER_KONTROL_PANELI.html
echo         async function stopScheduler() { >> SCHEDULER_KONTROL_PANELI.html
echo             try { >> SCHEDULER_KONTROL_PANELI.html
echo                 await fetch(`${API_BASE}/stop`, { method: 'POST' }); >> SCHEDULER_KONTROL_PANELI.html
echo                 await refreshStatus(); >> SCHEDULER_KONTROL_PANELI.html
echo             } catch (error) { >> SCHEDULER_KONTROL_PANELI.html
echo                 alert('Scheduler durdurma hatası: ' + error.message); >> SCHEDULER_KONTROL_PANELI.html
echo             } >> SCHEDULER_KONTROL_PANELI.html
echo         } >> SCHEDULER_KONTROL_PANELI.html
echo. >> SCHEDULER_KONTROL_PANELI.html
echo         async function runTask(taskName) { >> SCHEDULER_KONTROL_PANELI.html
echo             try { >> SCHEDULER_KONTROL_PANELI.html
echo                 await fetch(`${API_BASE}/run/${taskName}`, { method: 'POST' }); >> SCHEDULER_KONTROL_PANELI.html
echo                 await refreshStatus(); >> SCHEDULER_KONTROL_PANELI.html
echo             } catch (error) { >> SCHEDULER_KONTROL_PANELI.html
echo                 alert('Task çalıştırma hatası: ' + error.message); >> SCHEDULER_KONTROL_PANELI.html
echo             } >> SCHEDULER_KONTROL_PANELI.html
echo         } >> SCHEDULER_KONTROL_PANELI.html
echo. >> SCHEDULER_KONTROL_PANELI.html
echo         async function loadResults() { >> SCHEDULER_KONTROL_PANELI.html
echo             try { >> SCHEDULER_KONTROL_PANELI.html
echo                 const response = await fetch(`${API_BASE}/results?limit=10`); >> SCHEDULER_KONTROL_PANELI.html
echo                 const data = await response.json(); >> SCHEDULER_KONTROL_PANELI.html
echo                 const resultsEl = document.getElementById('results'); >> SCHEDULER_KONTROL_PANELI.html
echo                 resultsEl.innerHTML = data.results.map(result =^> `^<div style="margin: 10px 0; padding: 10px; border-left: 3px solid #3b82f6;"^>^<strong^>${result.task_name}^</strong^> - ${result.timestamp}^<br^>^<small^>${JSON.stringify(result.result)}^</small^>^</div^>`).join(''); >> SCHEDULER_KONTROL_PANELI.html
echo             } catch (error) { >> SCHEDULER_KONTROL_PANELI.html
echo                 console.error('Results yükleme hatası:', error); >> SCHEDULER_KONTROL_PANELI.html
echo             } >> SCHEDULER_KONTROL_PANELI.html
echo         } >> SCHEDULER_KONTROL_PANELI.html
echo. >> SCHEDULER_KONTROL_PANELI.html
echo         // Sayfa yüklendiğinde ve her 30 saniyede bir yenile >> SCHEDULER_KONTROL_PANELI.html
echo         refreshStatus(); >> SCHEDULER_KONTROL_PANELI.html
echo         setInterval(refreshStatus, 30000); >> SCHEDULER_KONTROL_PANELI.html
echo     ^</script^> >> SCHEDULER_KONTROL_PANELI.html
echo ^</body^> >> SCHEDULER_KONTROL_PANELI.html
echo ^</html^> >> SCHEDULER_KONTROL_PANELI.html

echo ✅ Scheduler kontrol paneli oluşturuldu

echo.
echo 📋 7. Scheduler konfigürasyon dosyası oluşturuluyor...
echo { > scheduler_config.json
echo   "daily_venue_time": "02:00", >> scheduler_config.json
echo   "daily_event_time": "03:00", >> scheduler_config.json
echo   "cache_warm_interval": 30, >> scheduler_config.json
echo   "weekly_scrape_day": "sunday", >> scheduler_config.json
echo   "weekly_scrape_time": "01:00", >> scheduler_config.json
echo   "news_update_interval": 60, >> scheduler_config.json
echo   "enabled": true >> scheduler_config.json
echo } >> scheduler_config.json

echo ✅ Scheduler konfigürasyonu oluşturuldu

echo.
echo ========================================
echo ✅ OTOMATIK SCHEDULER KURULUMU TAMAMLANDI!
echo ========================================
echo.
echo 📊 Özellikler:
echo   • Günlük venue güncelleme (02:00)
echo   • Günlük event güncelleme (03:00)
echo   • 30 dakikada bir cache warming
echo   • Haftalık tam scraping (Pazar 01:00)
echo   • Saatlik haber güncelleme
echo.
echo 🌐 Kontrol Paneli:
echo   • Web: SCHEDULER_KONTROL_PANELI.html
echo   • API: http://localhost:8001/api/scheduler/status
echo.
echo 🚀 Başlatma:
echo   1. Backend servisi başlatın
echo   2. Scheduler otomatik başlayacak
echo   3. Kontrol panelinden yönetin
echo.
echo 📋 API Endpoints:
echo   GET  /api/scheduler/status
echo   POST /api/scheduler/start
echo   POST /api/scheduler/stop
echo   POST /api/scheduler/run/{task_name}
echo   GET  /api/scheduler/results
echo.
echo 💡 Manuel Çalıştırma:
echo   • Venue güncelleme: POST /api/scheduler/run/daily_venue_update
echo   • Event güncelleme: POST /api/scheduler/run/daily_event_update
echo   • Cache warming: POST /api/scheduler/run/hourly_cache_warm
echo.
pause