# 🕐 Otomatik Veri Toplama Sistemi Rehberi

## 📋 Genel Bakış

Artık uygulamanız **tamamen otomatik** çalışıyor! Günlük veri toplama, cache warming, event güncelleme ve haftalık tam scraping işlemleri otomatik olarak gerçekleşiyor.

## 🚀 Hızlı Başlangıç

### 1. Otomatik Scheduler'ı Kur
```bash
./OTOMATIK_SCHEDULER_BASLAT.bat
```

### 2. Backend'i Başlat
```bash
cd backend
python server.py
```

### 3. Kontrol Panelini Aç
```
SCHEDULER_KONTROL_PANELI.html
```

**🎉 Artık sistem tamamen otomatik çalışıyor!**

## 📅 Otomatik Schedule

### Günlük İşlemler
- **02:00** - Venue güncelleme (Colorado geneli)
- **03:00** - Event güncelleme (Ticketmaster, Eventbrite, EDMTrain)
- **Her 30 dk** - Cache warming (performans için)
- **Her 60 dk** - Haber güncelleme

### Haftalık İşlemler
- **Pazar 01:00** - Tam Colorado scraping (50+ şehir)

### Gerçek Zamanlı
- **Sürekli** - Cache warming
- **Sürekli** - WebSocket güncellemeleri
- **Sürekli** - Trending hesaplamaları

## 🎛️ Kontrol Paneli

### Web Arayüzü
`SCHEDULER_KONTROL_PANELI.html` dosyasını açın:

- **Scheduler Durumu**: Çalışıyor/Durmuş
- **Görev Durumları**: Her task'ın son durumu
- **Manuel Çalıştırma**: İstediğiniz task'ı hemen çalıştırın
- **Son Sonuçlar**: Task geçmişi
- **Canlı Loglar**: Gerçek zamanlı log takibi

### API Endpoints
```http
GET  /api/scheduler/status          # Durum kontrolü
POST /api/scheduler/start           # Scheduler başlat
POST /api/scheduler/stop            # Scheduler durdur
POST /api/scheduler/run/{task_name} # Manuel task çalıştır
GET  /api/scheduler/results         # Sonuç geçmişi
GET  /api/scheduler/health          # Sağlık kontrolü
```

## 🔧 Otomatik Görevler

### 1. daily_venue_update
- **Zaman**: Her gün 02:00
- **Süre**: 15-30 dakika
- **İşlem**: Colorado genelinde venue güncelleme
- **Kaynaklar**: Google Places, Yelp, TripAdvisor
- **Sonuç**: 100-500 venue güncelleme/ekleme

### 2. daily_event_update
- **Zaman**: Her gün 03:00
- **Süre**: 10-20 dakika
- **İşlem**: Yeni etkinlikleri toplama
- **Kaynaklar**: Ticketmaster, Eventbrite, EDMTrain
- **Sonuç**: 50-200 yeni event

### 3. hourly_cache_warm
- **Zaman**: Her 30 dakika
- **Süre**: 2-5 dakika
- **İşlem**: Sık kullanılan verileri cache'e yükleme
- **Sonuç**: %95 cache hit rate

### 4. weekly_full_scrape
- **Zaman**: Her Pazar 01:00
- **Süre**: 1-2 saat
- **İşlem**: Colorado genelinde kapsamlı veri toplama
- **Kaynaklar**: Tüm kaynaklar
- **Sonuç**: 1000-3000 venue, 500-1500 event

### 5. news_update
- **Zaman**: Her 60 dakika
- **Süre**: 5-10 dakika
- **İşlem**: Colorado haberleri ve duyuruları
- **Kaynaklar**: Haber siteleri, RSS feeds
- **Sonuç**: 10-50 haber

## 📊 Veri Akışı

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   API Sources   │───▶│   Auto Scheduler │───▶│    Database     │
│                 │    │                  │    │                 │
│ • Ticketmaster  │    │ • Daily Tasks    │    │ • Venues        │
│ • Eventbrite    │    │ • Cache Warming  │    │ • Events        │
│ • Google Places │    │ • Weekly Scrape  │    │ • News          │
│ • EDMTrain      │    │ • News Updates   │    │ • Cache         │
│ • Yelp          │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                │
                                ▼
                       ┌─────────────────┐
                       │   Frontend      │
                       │                 │
                       │ • Real-time     │
                       │ • Trending      │
                       │ • Events        │
                       │ • Venues        │
                       └─────────────────┘
```

## 🔍 Monitoring ve İzleme

### Gerçek Zamanlı İzleme
```bash
# Scheduler durumu
curl http://localhost:8001/api/scheduler/status

# Sağlık kontrolü
curl http://localhost:8001/api/scheduler/health

# Son sonuçlar
curl http://localhost:8001/api/scheduler/results?limit=10
```

### Log İzleme
```bash
# Backend logları
tail -f backend/backend.log | grep scheduler

# Scheduler sonuçları
curl http://localhost:8001/api/scheduler/results | jq
```

### Database İzleme
```javascript
// MongoDB'de scheduler sonuçları
db.scheduler_results.find().sort({timestamp: -1}).limit(10)

// Günlük eklenen venue sayısı
db.venues.count({created_at: {$gte: "2024-01-18"}})

// Günlük eklenen event sayısı
db.events.count({created_at: {$gte: "2024-01-18"}})
```

## ⚙️ Konfigürasyon

### Scheduler Ayarları
`scheduler_config.json` dosyasını düzenleyin:

```json
{
  "daily_venue_time": "02:00",      // Venue güncelleme saati
  "daily_event_time": "03:00",      // Event güncelleme saati
  "cache_warm_interval": 30,        // Cache warming aralığı (dakika)
  "weekly_scrape_day": "sunday",    // Haftalık scraping günü
  "weekly_scrape_time": "01:00",    // Haftalık scraping saati
  "news_update_interval": 60,       // Haber güncelleme aralığı (dakika)
  "enabled": true                   // Scheduler aktif/pasif
}
```

### API ile Konfigürasyon
```bash
# Mevcut config
curl http://localhost:8001/api/scheduler/config

# Config güncelleme
curl -X PUT http://localhost:8001/api/scheduler/config \
  -H "Content-Type: application/json" \
  -d '{"daily_venue_time": "01:30", "enabled": true}'
```

## 🚨 Hata Yönetimi

### Otomatik Hata Düzeltme
- **API Rate Limit**: Otomatik bekleme ve yeniden deneme
- **Network Hatası**: 3 kez yeniden deneme
- **Database Hatası**: Hata logla ve devam et
- **Memory Hatası**: Batch size küçült

### Hata Bildirimleri
```python
# Email bildirimi (opsiyonel)
NOTIFICATION_EMAIL = "admin@yourapp.com"

# Slack webhook (opsiyonel)
SLACK_WEBHOOK_URL = "https://hooks.slack.com/..."
```

### Manuel Müdahale
```bash
# Hatalı task'ı manuel çalıştır
curl -X POST http://localhost:8001/api/scheduler/run/daily_venue_update

# Scheduler'ı yeniden başlat
curl -X POST http://localhost:8001/api/scheduler/stop
curl -X POST http://localhost:8001/api/scheduler/start
```

## 📈 Performans Metrikleri

### Günlük Hedefler
- **Venue Updates**: 100-500 venue
- **Event Updates**: 50-200 event
- **Cache Hit Rate**: >90%
- **API Response Time**: <500ms
- **Task Success Rate**: >95%

### Haftalık Hedefler
- **Total Venues**: 3000-5000 venue
- **Total Events**: 1000-3000 event
- **Data Freshness**: <24 saat
- **Coverage**: 50+ Colorado şehri

### Monitoring Dashboard
```javascript
// Günlük istatistikler
{
  "venues_added_today": 150,
  "events_added_today": 75,
  "cache_hit_rate": 0.94,
  "successful_tasks": 8,
  "failed_tasks": 0,
  "last_full_scrape": "2024-01-14T01:00:00Z",
  "next_full_scrape": "2024-01-21T01:00:00Z"
}
```

## 🔧 Troubleshooting

### Yaygın Sorunlar

#### 1. Scheduler Çalışmıyor
```bash
# Durum kontrol et
curl http://localhost:8001/api/scheduler/status

# Manuel başlat
curl -X POST http://localhost:8001/api/scheduler/start
```

#### 2. Task'lar Başarısız
```bash
# Hata detaylarını kontrol et
curl http://localhost:8001/api/scheduler/results?task_name=daily_venue_update

# Manuel çalıştır
curl -X POST http://localhost:8001/api/scheduler/run/daily_venue_update
```

#### 3. Veri Güncellenmiyor
```bash
# Son sonuçları kontrol et
curl http://localhost:8001/api/scheduler/results | jq '.results[0]'

# Database'i kontrol et
mongo your_database --eval "db.venues.find().sort({updated_at:-1}).limit(5)"
```

#### 4. Yüksek Memory Kullanımı
```bash
# Batch size'ı küçült
# Cache interval'ı artır
# Log level'ı azalt
```

## 🎯 Optimizasyon İpuçları

### Performance
- **API Keys**: Tüm API keylerini ayarlayın
- **Rate Limits**: API limitlerini aşmayın
- **Batch Processing**: Büyük veri setlerini bölerek işleyin
- **Caching**: Sık kullanılan verileri cache'leyin

### Reliability
- **Error Handling**: Robust hata yönetimi
- **Retry Logic**: Başarısız işlemleri yeniden deneyin
- **Health Checks**: Düzenli sağlık kontrolü
- **Monitoring**: Sürekli izleme

### Scalability
- **Database Indexing**: Uygun indexler oluşturun
- **Connection Pooling**: Bağlantı havuzu kullanın
- **Async Processing**: Paralel işleme
- **Load Balancing**: Yük dağılımı

## 📞 Destek

### Log Dosyaları
- `backend/backend.log` - Ana uygulama logları
- `scheduler_results_*.json` - Task sonuçları
- `colorado_scraping_results_*.json` - Scraping sonuçları

### Debug Komutları
```bash
# Scheduler test
python SCHEDULER_TEST.py

# Manuel task çalıştırma
python -c "
import asyncio
from backend.services.auto_scheduler import auto_scheduler
asyncio.run(auto_scheduler.run_task_manually('hourly_cache_warm'))
"
```

### Monitoring Tools
- **Web Panel**: `SCHEDULER_KONTROL_PANELI.html`
- **API Status**: `http://localhost:8001/api/scheduler/status`
- **Health Check**: `http://localhost:8001/api/scheduler/health`

---

## 🎉 Özet

**Artık uygulamanız tamamen otomatik çalışıyor!**

✅ **Günlük otomatik veri toplama**
✅ **Haftalık kapsamlı scraping**
✅ **Gerçek zamanlı cache warming**
✅ **Otomatik hata yönetimi**
✅ **Web tabanlı kontrol paneli**
✅ **API tabanlı yönetim**
✅ **Detaylı monitoring**

Sistem 7/24 çalışarak Colorado genelindeki venue ve event verilerini güncel tutuyor. Kontrol panelinden durumu izleyebilir, manuel müdahale edebilir ve konfigürasyonu değiştirebilirsiniz.

**🚀 Artık sadece uygulamanızı kullanmaya odaklanabilirsiniz!**