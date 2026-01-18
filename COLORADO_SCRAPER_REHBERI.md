# 🏔️ Colorado Kapsamlı Scraper Rehberi

## 📋 Genel Bakış

Colorado eyaleti genelinde venue ve event verilerini toplayan kapsamlı scraping sistemi. 50+ şehir, 10+ veri kaynağı ve akıllı veri zenginleştirme özellikleri.

## 🚀 Hızlı Başlangıç

### 1. Scripti Çalıştır
```bash
./COLORADO_SCRAPER_BASLAT.bat
```

### 2. Mod Seç
- **Test Modu**: 5 şehir, hızlı test
- **Öncelikli Şehirler**: 25 önemli şehir
- **Tam Colorado**: 50+ şehir
- **Sadece Venues**: Mekan scraping
- **Sadece Events**: Etkinlik scraping

### 3. Manuel Çalıştırma
```bash
# Test modu
python COLORADO_KAPSAMLI_SCRAPER.py --test --priority 1

# Öncelikli şehirler
python COLORADO_KAPSAMLI_SCRAPER.py --priority 2

# Tam scraping
python COLORADO_KAPSAMLI_SCRAPER.py --priority 3

# Sadece venues
python COLORADO_KAPSAMLI_SCRAPER.py --venues-only

# Sadece events
python COLORADO_KAPSAMLI_SCRAPER.py --events-only
```

## 🏙️ Kapsanan Şehirler

### Öncelik 1 (En Önemli - 15 şehir)
- **Denver Metro**: Denver, Aurora, Lakewood, Thornton, Arvada, Westminster
- **Üniversite Şehirleri**: Boulder, Fort Collins
- **Turizm Merkezleri**: Aspen, Vail, Breckenridge, Steamboat Springs
- **Diğer Büyük Şehirler**: Colorado Springs, Pueblo

### Öncelik 2 (Orta Önemli - 25 şehir)
- **Denver Çevresi**: Centennial, Broomfield, Castle Rock, Parker, Littleton
- **Dağ Kasabaları**: Telluride, Winter Park, Crested Butte, Durango, Estes Park
- **Diğer Şehirler**: Greeley, Longmont, Loveland, Grand Junction, Manitou Springs

### Öncelik 3 (Tümü - 50+ şehir)
- **Küçük Şehirler**: Commerce City, Northglenn, Englewood, Wheat Ridge, Golden
- **Kırsal Alanlar**: Fort Morgan, Sterling, Montrose, Grand Lake
- **Tüm Colorado**: Eyalet genelindeki tüm yerleşim yerleri

## 📊 Veri Kaynakları

### Venue Kaynakları
1. **Google Places API** ⭐
   - En kapsamlı venue verisi
   - Koordinat, rating, fotoğraf
   - 18 farklı venue tipi

2. **Yelp Web Scraping** ⭐
   - Kullanıcı yorumları
   - Rating ve kategori bilgisi
   - Güncel işletme durumu

3. **TripAdvisor Scraping**
   - Turist mekanları
   - Attraction bilgileri
   - Dağ kasabaları için önemli

4. **Yerel Dizinler**
   - Colorado.gov
   - Visit Colorado
   - Ticaret odaları

### Event Kaynakları
1. **Ticketmaster API** ⭐
   - Resmi etkinlikler
   - Konser, spor, tiyatro
   - Fiyat bilgileri

2. **Eventbrite API** ⭐
   - Yerel etkinlikler
   - Ücretsiz events
   - Küçük organizasyonlar

3. **EDMTrain API**
   - Elektronik müzik
   - Denver ve Boulder
   - Gece hayatı

4. **Web Scraping**
   - Facebook Events
   - Meetup Events
   - Yerel event siteleri

## 🔧 Teknik Özellikler

### Akıllı Veri İşleme
- **Duplicate Detection**: Aynı venue/event'i farklı kaynaklardan tespit
- **Geocoding**: Eksik koordinat bilgilerini tamamlama
- **Category Normalization**: Kategori standardizasyonu
- **Event-Venue Matching**: Etkinlikleri mekanlarla eşleştirme

### Performance Optimizasyonu
- **Rate Limiting**: API limitlerini aşmama
- **Async Processing**: Paralel veri işleme
- **Caching**: Tekrarlayan istekleri önleme
- **Error Handling**: Robust hata yönetimi

### Database Schema
```javascript
// Venues Collection
{
  "id": "uuid",
  "source": "google_places|yelp|tripadvisor",
  "place_id": "google_place_id",
  "name": "Venue Name",
  "address": "Full Address",
  "city": "Denver",
  "state": "CO",
  "lat": 39.7392,
  "lng": -104.9903,
  "rating": 4.5,
  "user_ratings_total": 1250,
  "price_level": 2,
  "types": ["night_club", "bar"],
  "venue_type": "night_club",
  "category": "nightclub",
  "popularity_score": 15,
  "created_at": "2024-01-18T10:00:00Z",
  "updated_at": "2024-01-18T10:00:00Z",
  "last_scraped": "2024-01-18T10:00:00Z"
}

// Events Collection
{
  "id": "uuid",
  "source": "ticketmaster|eventbrite|edmtrain",
  "external_id": "tm_12345",
  "name": "Event Name",
  "description": "Event description",
  "url": "https://...",
  "start_date": "2024-02-15",
  "start_time": "20:00",
  "venue_name": "Venue Name",
  "venue_id": "venue_uuid",
  "venue_address": "Address",
  "city": "Denver",
  "state": "CO",
  "category": "music",
  "genre": "Rock",
  "image_url": "https://...",
  "price_min": 25.00,
  "price_max": 75.00,
  "is_free": false,
  "created_at": "2024-01-18T10:00:00Z"
}
```

## 🔑 API Key Kurulumu

### Gerekli API Keys
```bash
# Google Places API (Önemli)
export GOOGLE_PLACES_API_KEY=your_key_here

# Ticketmaster API (Önemli)
export TICKETMASTER_API_KEY=your_key_here

# Eventbrite API (Opsiyonel)
export EVENTBRITE_TOKEN=your_token_here

# EDMTrain API (Opsiyonel)
export EDMTRAIN_API_KEY=your_key_here
```

### API Key Alma Rehberi

#### 1. Google Places API
1. https://console.cloud.google.com adresine git
2. Yeni proje oluştur
3. Places API'yi etkinleştir
4. API key oluştur
5. Billing hesabı ekle (aylık $200 ücretsiz)

#### 2. Ticketmaster API
1. https://developer.ticketmaster.com adresine git
2. Hesap oluştur
3. App kaydı yap
4. API key al (ücretsiz)

#### 3. Eventbrite API
1. https://www.eventbrite.com/platform/ adresine git
2. Developer hesabı oluştur
3. App oluştur
4. OAuth token al

#### 4. EDMTrain API
1. https://edmtrain.com/developer-api adresine git
2. Form doldur
3. API key bekle (email ile gelir)

## 📈 Performans Metrikleri

### Beklenen Sonuçlar
| Mod | Şehir | Venue | Event | Süre |
|-----|-------|-------|-------|------|
| Test | 5 | 200-500 | 100-300 | 5-10 dk |
| Öncelikli | 25 | 1000-2500 | 500-1500 | 30-45 dk |
| Tam | 50+ | 3000-5000 | 1000-3000 | 1-2 saat |

### Rate Limits
- **Google Places**: 1000 request/gün (ücretsiz)
- **Ticketmaster**: 5000 request/gün
- **Eventbrite**: 1000 request/saat
- **Web Scraping**: 1 request/2 saniye

## 🧪 Test ve Debugging

### Test Modu
```bash
# Hızlı test (5 şehir)
python COLORADO_KAPSAMLI_SCRAPER.py --test

# Verbose logging
export LOG_LEVEL=DEBUG
python COLORADO_KAPSAMLI_SCRAPER.py --test
```

### Sonuç Kontrolü
```bash
# Sonuç dosyası
cat colorado_scraping_results_*.json

# Database kontrolü
mongo
use your_database
db.venues.count()
db.events.count()
```

### Hata Ayıklama
```python
# Python console'da
import asyncio
from COLORADO_KAPSAMLI_SCRAPER import ColoradoKapsamliScraper

async def debug_test():
    async with ColoradoKapsamliScraper() as scraper:
        # Tek şehir test
        venues = await scraper._scrape_google_places("Denver", {"lat": 39.7392, "lng": -104.9903})
        print(f"Found {len(venues)} venues")

asyncio.run(debug_test())
```

## 📊 Veri Analizi

### Venue İstatistikleri
```javascript
// MongoDB queries
// Şehir bazlı venue sayısı
db.venues.aggregate([
  {$group: {_id: "$city", count: {$sum: 1}}},
  {$sort: {count: -1}}
])

// Kategori dağılımı
db.venues.aggregate([
  {$group: {_id: "$category", count: {$sum: 1}}},
  {$sort: {count: -1}}
])

// Rating ortalaması
db.venues.aggregate([
  {$group: {_id: "$city", avg_rating: {$avg: "$rating"}}}
])
```

### Event İstatistikleri
```javascript
// Aylık event dağılımı
db.events.aggregate([
  {$group: {
    _id: {$substr: ["$start_date", 0, 7]},
    count: {$sum: 1}
  }},
  {$sort: {_id: 1}}
])

// Kategori bazlı event sayısı
db.events.aggregate([
  {$group: {_id: "$category", count: {$sum: 1}}},
  {$sort: {count: -1}}
])
```

## 🔄 Otomatik Güncelleme

### Cron Job Kurulumu
```bash
# Günlük güncelleme (sadece öncelikli şehirler)
0 2 * * * cd /path/to/project && python COLORADO_KAPSAMLI_SCRAPER.py --priority 1

# Haftalık tam güncelleme
0 1 * * 0 cd /path/to/project && python COLORADO_KAPSAMLI_SCRAPER.py --priority 2

# Aylık kapsamlı güncelleme
0 0 1 * * cd /path/to/project && python COLORADO_KAPSAMLI_SCRAPER.py --priority 3
```

### Monitoring
```bash
# Log dosyası takibi
tail -f colorado_scraper.log

# Email bildirimi (başarı/hata)
python COLORADO_KAPSAMLI_SCRAPER.py --priority 1 --notify-email your@email.com
```

## 🚨 Troubleshooting

### Yaygın Sorunlar

#### 1. API Key Hatası
```
Error: Google Places API key not configured
```
**Çözüm**: Environment variable'ı set edin
```bash
export GOOGLE_PLACES_API_KEY=your_key_here
```

#### 2. Rate Limit Aşımı
```
Error: API rate limit exceeded
```
**Çözüm**: Bekleme sürelerini artırın veya API key upgrade yapın

#### 3. Database Bağlantı Hatası
```
Error: MongoDB connection failed
```
**Çözüm**: MongoDB servisinin çalıştığını kontrol edin

#### 4. Memory Hatası
```
Error: Out of memory
```
**Çözüm**: Batch size'ı küçültün veya test modunu kullanın

### Debug Komutları
```bash
# Verbose logging
python COLORADO_KAPSAMLI_SCRAPER.py --test --verbose

# Sadece bir şehir test
python -c "
import asyncio
from COLORADO_KAPSAMLI_SCRAPER import ColoradoKapsamliScraper
async def test():
    async with ColoradoKapsamliScraper() as s:
        venues = await s._scrape_google_places('Denver', {'lat': 39.7392, 'lng': -104.9903})
        print(f'Found {len(venues)} venues')
asyncio.run(test())
"
```

## 📞 Destek

### Log Dosyaları
- `colorado_scraper.log` - Ana log dosyası
- `colorado_scraping_results_*.json` - Sonuç dosyaları
- `backend/backend.log` - Backend logları

### Performans İzleme
```python
# Scraping istatistikleri
results = await scraper.run_full_scraping()
print(f"Venues: {results['venues']['added']} added")
print(f"Events: {results['events']['added']} added")
print(f"Time: {results['processing_time']} seconds")
```

---

**🏔️ Colorado'nun tüm venue ve event verilerini tek bir script ile toplayın!**