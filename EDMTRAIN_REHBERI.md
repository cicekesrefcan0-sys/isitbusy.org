# 🎵 EDM Train Entegrasyonu Rehberi

## 📋 Genel Bakış

EDM Train, elektronik müzik etkinlikleri için popüler bir platform. Bu entegrasyon ile uygulamanıza EDM/elektronik müzik etkinliklerini ekleyebilirsiniz.

## 🚀 Hızlı Başlangıç

### 1. Entegrasyonu Çalıştır
```bash
./EDMTRAIN_ENTEGRASYONU.bat
```

### 2. Test Et
```bash
python TEST_EDMTRAIN_SCRAPER.py
```

### 3. Web Testini Aç
```
EDMTRAIN_TEST_SAYFASI.html
```

## 🔧 Teknik Detaylar

### Backend Bileşenleri

#### `services/edmtrain_scraper.py`
- **Dual Mode**: API + Web scraping desteği
- **Locations**: Denver, Chicago, LA, NYC, Miami vb.
- **Event Data**: Name, date, venue, artists, genre
- **Caching**: Akıllı cache sistemi

#### `routes/edmtrain.py`
- **REST API**: Full CRUD endpoints
- **Cache Management**: 2-4 saat cache
- **Database Storage**: Analytics için
- **Error Handling**: Robust hata yönetimi

### Frontend Bileşenleri

#### `components/EDMTrainEvents.jsx`
- **React Component**: Modern hooks kullanımı
- **Location Support**: Şehir bazlı filtreleme
- **Loading States**: UX optimizasyonu
- **Event Display**: Güzel görünüm

## 📡 API Endpoints

### Events
```http
GET /api/edmtrain/events/{location}?limit=20&refresh=false
```
**Response:**
```json
{
  "success": true,
  "location": "denver",
  "events": [
    {
      "event_id": "12345",
      "name": "Tomorrowland Winter",
      "date": "2024-02-15",
      "venue": "Red Rocks Amphitheatre",
      "artists": ["Tiësto", "Martin Garrix"],
      "genre": "Electronic",
      "category": "EDM",
      "url": "https://edmtrain.com/events/12345",
      "source": "EDM Train"
    }
  ],
  "count": 1
}
```

### Event Details
```http
GET /api/edmtrain/event/{event_id}
```

### Locations
```http
GET /api/edmtrain/locations
```

### Statistics
```http
GET /api/edmtrain/stats
```

### Refresh Data
```http
POST /api/edmtrain/refresh
```

## 🏙️ Desteklenen Şehirler

| Şehir | Slug | Eyalet |
|-------|------|--------|
| Denver | `denver` | CO |
| Chicago | `chicago` | IL |
| Los Angeles | `los-angeles` | CA |
| New York | `new-york` | NY |
| Miami | `miami` | FL |
| Las Vegas | `las-vegas` | NV |
| Seattle | `seattle` | WA |
| Austin | `austin` | TX |
| Atlanta | `atlanta` | GA |
| Boston | `boston` | MA |

## 🔑 API Key Kurulumu (Opsiyonel)

### 1. API Key Al
1. https://edmtrain.com/developer-api adresine git
2. Formu doldur:
   - **App Name**: Uygulamanızın adı
   - **App Link**: Website URL'i
   - **Description**: Nasıl kullanacağınızı açıklayın
3. API Terms of Use'u kabul et
4. API key'i bekle (email ile gelir)

### 2. Environment Variable Ayarla
```bash
# Windows
set EDMTRAIN_API_KEY=your_api_key_here

# Linux/Mac
export EDMTRAIN_API_KEY=your_api_key_here
```

### 3. .env Dosyasına Ekle
```env
EDMTRAIN_API_KEY=your_api_key_here
```

## 🎯 Kullanım Örnekleri

### Python (Backend)
```python
from services.edmtrain_scraper import EDMTrainScraper

async def get_edm_events():
    async with EDMTrainScraper() as scraper:
        events = await scraper.get_events_by_location("denver", limit=10)
        return events
```

### JavaScript (Frontend)
```javascript
import EDMTrainEvents from './components/EDMTrainEvents';

function App() {
  return (
    <div>
      <EDMTrainEvents location="denver" limit={10} />
    </div>
  );
}
```

### cURL (API Test)
```bash
curl "http://localhost:8001/api/edmtrain/events/denver?limit=5"
```

## 📊 Database Schema

### `edmtrain_events` Collection
```javascript
{
  "_id": ObjectId,
  "event_id": "12345",
  "name": "Event Name",
  "date": "2024-02-15",
  "time": "20:00",
  "venue": "Venue Name",
  "venue_address": "Address",
  "artists": ["Artist 1", "Artist 2"],
  "genre": "Electronic",
  "category": "EDM",
  "age_restriction": "18+",
  "ticket_url": "https://...",
  "url": "https://edmtrain.com/events/12345",
  "location": "denver",
  "platform": "edmtrain",
  "source": "EDM Train",
  "scraped_at": "2024-01-18T10:00:00Z",
  "stored_at": "2024-01-18T10:00:00Z"
}
```

### Indexes
```javascript
// Performance için indexler
db.edmtrain_events.createIndex({ "event_id": 1 })
db.edmtrain_events.createIndex({ "location": 1 })
db.edmtrain_events.createIndex({ "platform": 1 })
db.edmtrain_events.createIndex({ "scraped_at": 1 })
db.edmtrain_events.createIndex({ "event_id": 1, "platform": 1 }, { unique: true })
```

## 🔄 Cache Stratejisi

### Cache Keys
```
edmtrain_events:{location}:{limit}     # 2 saat
edmtrain_event_details:{event_id}      # 4 saat
```

### Cache Warming
```python
# Popüler şehirler için otomatik cache warming
popular_locations = ["denver", "chicago", "los-angeles", "new-york", "miami"]
```

## 🧪 Test Senaryoları

### 1. Basic Scraping Test
```bash
python TEST_EDMTRAIN_SCRAPER.py
```

### 2. API Integration Test
```bash
# API key ile
export EDMTRAIN_API_KEY=your_key
python TEST_EDMTRAIN_SCRAPER.py
```

### 3. Web Interface Test
```
# Browser'da aç
EDMTRAIN_TEST_SAYFASI.html
```

### 4. Performance Test
```bash
# Concurrent requests
curl -s "http://localhost:8001/api/edmtrain/events/denver" &
curl -s "http://localhost:8001/api/edmtrain/events/chicago" &
curl -s "http://localhost:8001/api/edmtrain/events/los-angeles" &
wait
```

## 🚨 Troubleshooting

### Problem: No events found
**Çözüm:**
1. Internet bağlantısını kontrol et
2. EDM Train sitesinin erişilebilir olduğunu kontrol et
3. Şehir adının doğru olduğunu kontrol et

### Problem: API key not working
**Çözüm:**
1. API key'in doğru set edildiğini kontrol et
2. API Terms of Use'u kabul ettiğinizi kontrol et
3. Rate limit'e takılmadığınızı kontrol et

### Problem: Slow performance
**Çözüm:**
1. Cache'in çalıştığını kontrol et
2. Database indexlerinin oluşturulduğunu kontrol et
3. Concurrent request sayısını azalt

## 📈 Analytics ve Monitoring

### Event Statistics
```python
# Total events
total = await db.edmtrain_events.count_documents({})

# Events by location
pipeline = [
    {"$group": {"_id": "$location", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
]
```

### Performance Metrics
- **Scraping Time**: ~2-5 saniye per location
- **API Response**: ~200-500ms (cached)
- **Database Storage**: ~1KB per event
- **Cache Hit Rate**: %80-90

## 🔮 Gelecek Geliştirmeler

### Planned Features
1. **Real-time Updates**: WebSocket ile canlı güncellemeler
2. **Artist Following**: Favori artist takibi
3. **Event Recommendations**: AI tabanlı öneriler
4. **Social Integration**: Event sharing
5. **Mobile App**: React Native component

### API Enhancements
1. **Filtering**: Genre, date range, price filters
2. **Sorting**: Date, popularity, distance
3. **Pagination**: Large result sets için
4. **Webhooks**: Event updates için

## 📞 Destek

### Loglar
```bash
# Backend logs
tail -f backend/backend.log | grep edmtrain

# Database queries
db.edmtrain_events.find().limit(5)
```

### Debug Mode
```python
import logging
logging.getLogger('services.edmtrain_scraper').setLevel(logging.DEBUG)
```

---

**🎉 EDM Train entegrasyonu ile elektronik müzik etkinliklerini uygulamanıza başarıyla entegre ettiniz!**