@echo off
echo ========================================
echo 🎵 EDM TRAIN ENTEGRASYONU
echo ========================================
echo.

echo 📋 1. EDM Train scraper test ediliyor...
python TEST_EDMTRAIN_SCRAPER.py

echo.
echo 📋 2. Backend'e EDM Train route'u ekleniyor...
cd backend

echo.
echo 📋 3. Server.py'ye EDM Train route'u ekleniyor...
python -c "
import re

# Read server.py
with open('server.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if edmtrain route already exists
if 'from routes import edmtrain' not in content:
    # Add import
    import_pattern = r'(from routes import [^\\n]+)'
    if re.search(import_pattern, content):
        content = re.sub(import_pattern, r'\1, edmtrain', content)
    else:
        # Add new import line
        content = re.sub(r'(from routes import [^\\n]+)', r'\1\\nfrom routes import edmtrain', content)
    
    # Add router
    router_pattern = r'(app\.include_router\([^\\n]+\))'
    last_router = None
    for match in re.finditer(router_pattern, content):
        last_router = match
    
    if last_router:
        insert_pos = last_router.end()
        content = content[:insert_pos] + '\\napp.include_router(edmtrain.router)' + content[insert_pos:]
    
    # Write back
    with open('server.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print('✅ EDM Train route added to server.py')
else:
    print('✅ EDM Train route already exists in server.py')
"

echo.
echo 📋 4. Database collection oluşturuluyor...
python -c "
import asyncio
from database import db

async def create_collection():
    try:
        # Create edmtrain_events collection with indexes
        await db.create_collection('edmtrain_events')
        
        # Create indexes
        await db.edmtrain_events.create_index('event_id')
        await db.edmtrain_events.create_index('location')
        await db.edmtrain_events.create_index('platform')
        await db.edmtrain_events.create_index('scraped_at')
        await db.edmtrain_events.create_index([('event_id', 1), ('platform', 1)], unique=True)
        
        print('✅ EDM Train database collection and indexes created')
    except Exception as e:
        print(f'⚠️  Collection might already exist: {e}')

asyncio.run(create_collection())
"

echo.
echo 📋 5. Frontend'e EDM Train component'i ekleniyor...
cd ../frontend/src/components

echo Creating EDMTrainEvents component...
echo import { useState, useEffect } from 'react'; > EDMTrainEvents.jsx
echo import axios from 'axios'; >> EDMTrainEvents.jsx
echo. >> EDMTrainEvents.jsx
echo const API = `${process.env.REACT_APP_BACKEND_URL}/api`; >> EDMTrainEvents.jsx
echo. >> EDMTrainEvents.jsx
echo const EDMTrainEvents = ({ location = 'denver', limit = 10 }) =^> { >> EDMTrainEvents.jsx
echo   const [events, setEvents] = useState([]); >> EDMTrainEvents.jsx
echo   const [loading, setLoading] = useState(true); >> EDMTrainEvents.jsx
echo. >> EDMTrainEvents.jsx
echo   useEffect(() =^> { >> EDMTrainEvents.jsx
echo     fetchEDMEvents(); >> EDMTrainEvents.jsx
echo   }, [location]); >> EDMTrainEvents.jsx
echo. >> EDMTrainEvents.jsx
echo   const fetchEDMEvents = async () =^> { >> EDMTrainEvents.jsx
echo     try { >> EDMTrainEvents.jsx
echo       const res = await axios.get(`${API}/edmtrain/events/${location}?limit=${limit}`); >> EDMTrainEvents.jsx
echo       setEvents(res.data.events ^|^| []); >> EDMTrainEvents.jsx
echo     } catch (e) { >> EDMTrainEvents.jsx
echo       console.error('Failed to fetch EDM events'); >> EDMTrainEvents.jsx
echo     } finally { >> EDMTrainEvents.jsx
echo       setLoading(false); >> EDMTrainEvents.jsx
echo     } >> EDMTrainEvents.jsx
echo   }; >> EDMTrainEvents.jsx
echo. >> EDMTrainEvents.jsx
echo   if (loading) return ^<div^>Loading EDM events...^</div^>; >> EDMTrainEvents.jsx
echo. >> EDMTrainEvents.jsx
echo   return ( >> EDMTrainEvents.jsx
echo     ^<div className="edm-events"^> >> EDMTrainEvents.jsx
echo       ^<h3^>🎵 EDM Events in {location}^</h3^> >> EDMTrainEvents.jsx
echo       {events.map((event, i) =^> ( >> EDMTrainEvents.jsx
echo         ^<div key={i} className="event-card"^> >> EDMTrainEvents.jsx
echo           ^<h4^>{event.name}^</h4^> >> EDMTrainEvents.jsx
echo           ^<p^>📅 {event.date}^</p^> >> EDMTrainEvents.jsx
echo           ^<p^>🏢 {event.venue}^</p^> >> EDMTrainEvents.jsx
echo           ^<p^>🎤 {event.artists?.join(', ')}^</p^> >> EDMTrainEvents.jsx
echo         ^</div^> >> EDMTrainEvents.jsx
echo       ))} >> EDMTrainEvents.jsx
echo     ^</div^> >> EDMTrainEvents.jsx
echo   ); >> EDMTrainEvents.jsx
echo }; >> EDMTrainEvents.jsx
echo. >> EDMTrainEvents.jsx
echo export default EDMTrainEvents; >> EDMTrainEvents.jsx

echo ✅ EDMTrainEvents component created

echo.
echo 📋 6. Test sayfası oluşturuluyor...
cd ../../..

echo ^<!DOCTYPE html^> > EDMTRAIN_TEST_SAYFASI.html
echo ^<html^> >> EDMTRAIN_TEST_SAYFASI.html
echo ^<head^> >> EDMTRAIN_TEST_SAYFASI.html
echo     ^<title^>EDM Train Test^</title^> >> EDMTRAIN_TEST_SAYFASI.html
echo     ^<style^> >> EDMTRAIN_TEST_SAYFASI.html
echo         body { font-family: Arial, sans-serif; margin: 20px; } >> EDMTRAIN_TEST_SAYFASI.html
echo         .event { border: 1px solid #ddd; padding: 15px; margin: 10px 0; border-radius: 8px; } >> EDMTRAIN_TEST_SAYFASI.html
echo         .loading { text-align: center; padding: 20px; } >> EDMTRAIN_TEST_SAYFASI.html
echo         button { padding: 10px 20px; margin: 5px; cursor: pointer; } >> EDMTRAIN_TEST_SAYFASI.html
echo     ^</style^> >> EDMTRAIN_TEST_SAYFASI.html
echo ^</head^> >> EDMTRAIN_TEST_SAYFASI.html
echo ^<body^> >> EDMTRAIN_TEST_SAYFASI.html
echo     ^<h1^>🎵 EDM Train Events Test^</h1^> >> EDMTRAIN_TEST_SAYFASI.html
echo     ^<div^> >> EDMTRAIN_TEST_SAYFASI.html
echo         ^<button onclick="loadEvents('denver')"^>Denver^</button^> >> EDMTRAIN_TEST_SAYFASI.html
echo         ^<button onclick="loadEvents('chicago')"^>Chicago^</button^> >> EDMTRAIN_TEST_SAYFASI.html
echo         ^<button onclick="loadEvents('los-angeles')"^>Los Angeles^</button^> >> EDMTRAIN_TEST_SAYFASI.html
echo         ^<button onclick="loadEvents('new-york')"^>New York^</button^> >> EDMTRAIN_TEST_SAYFASI.html
echo     ^</div^> >> EDMTRAIN_TEST_SAYFASI.html
echo     ^<div id="events"^>^</div^> >> EDMTRAIN_TEST_SAYFASI.html
echo. >> EDMTRAIN_TEST_SAYFASI.html
echo     ^<script^> >> EDMTRAIN_TEST_SAYFASI.html
echo         async function loadEvents(location) { >> EDMTRAIN_TEST_SAYFASI.html
echo             document.getElementById('events').innerHTML = '^<div class="loading"^>Loading EDM events for ' + location + '...^</div^>'; >> EDMTRAIN_TEST_SAYFASI.html
echo             try { >> EDMTRAIN_TEST_SAYFASI.html
echo                 const response = await fetch(`http://localhost:8001/api/edmtrain/events/${location}?limit=10`); >> EDMTRAIN_TEST_SAYFASI.html
echo                 const data = await response.json(); >> EDMTRAIN_TEST_SAYFASI.html
echo                 displayEvents(data.events ^|^| [], location); >> EDMTRAIN_TEST_SAYFASI.html
echo             } catch (error) { >> EDMTRAIN_TEST_SAYFASI.html
echo                 document.getElementById('events').innerHTML = '^<p^>Error loading events: ' + error.message + '^</p^>'; >> EDMTRAIN_TEST_SAYFASI.html
echo             } >> EDMTRAIN_TEST_SAYFASI.html
echo         } >> EDMTRAIN_TEST_SAYFASI.html
echo. >> EDMTRAIN_TEST_SAYFASI.html
echo         function displayEvents(events, location) { >> EDMTRAIN_TEST_SAYFASI.html
echo             const container = document.getElementById('events'); >> EDMTRAIN_TEST_SAYFASI.html
echo             if (events.length === 0) { >> EDMTRAIN_TEST_SAYFASI.html
echo                 container.innerHTML = `^<p^>No EDM events found for ${location}^</p^>`; >> EDMTRAIN_TEST_SAYFASI.html
echo                 return; >> EDMTRAIN_TEST_SAYFASI.html
echo             } >> EDMTRAIN_TEST_SAYFASI.html
echo             container.innerHTML = `^<h2^>EDM Events in ${location} (${events.length})^</h2^>` + >> EDMTRAIN_TEST_SAYFASI.html
echo                 events.map(event =^> `^<div class="event"^>^<h3^>${event.name ^|^| 'EDM Event'}^</h3^>^<p^>📅 ${event.date ^|^| 'TBD'}^</p^>^<p^>🏢 ${event.venue ^|^| 'TBD'}^</p^>^<p^>🎤 ${event.artists?.join(', ') ^|^| 'TBD'}^</p^>^<p^>🔗 ^<a href="${event.url}" target="_blank"^>Event Link^</a^>^</p^>^</div^>`).join(''); >> EDMTRAIN_TEST_SAYFASI.html
echo         } >> EDMTRAIN_TEST_SAYFASI.html
echo. >> EDMTRAIN_TEST_SAYFASI.html
echo         // Load Denver events by default >> EDMTRAIN_TEST_SAYFASI.html
echo         loadEvents('denver'); >> EDMTRAIN_TEST_SAYFASI.html
echo     ^</script^> >> EDMTRAIN_TEST_SAYFASI.html
echo ^</body^> >> EDMTRAIN_TEST_SAYFASI.html
echo ^</html^> >> EDMTRAIN_TEST_SAYFASI.html

echo ✅ Test sayfası oluşturuldu: EDMTRAIN_TEST_SAYFASI.html

echo.
echo ========================================
echo ✅ EDM TRAIN ENTEGRASYONU TAMAMLANDI!
echo ========================================
echo.
echo 📊 Özellikler:
echo   • EDM Train event scraping (API + Web scraping)
echo   • Denver, Chicago, LA, NYC ve diğer şehirler
echo   • Elektronik müzik etkinlikleri
echo   • Event detayları ve artist bilgileri
echo   • Cache sistemi (2 saat)
echo   • Database storage
echo   • REST API endpoints
echo.
echo 🌐 API Endpoints:
echo   GET /api/edmtrain/events/{location}
echo   GET /api/edmtrain/event/{event_id}
echo   GET /api/edmtrain/locations
echo   GET /api/edmtrain/stats
echo   POST /api/edmtrain/refresh
echo.
echo 🧪 Test:
echo   1. Backend: python TEST_EDMTRAIN_SCRAPER.py
echo   2. Web: EDMTRAIN_TEST_SAYFASI.html
echo   3. API: http://localhost:8001/api/edmtrain/events/denver
echo.
echo 💡 API Key (opsiyonel):
echo   EDM Train API key için: https://edmtrain.com/developer-api
echo   export EDMTRAIN_API_KEY=your_key_here
echo.
pause