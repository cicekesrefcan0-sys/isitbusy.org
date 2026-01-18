# 🚀 Google Cloud → AWS Geçiş Planı

## 📊 Mevcut Durum Analizi

### Google Cloud Servisleri:
- ✅ **Google Gemini AI** - AI tahminleri (1500/gün ücretsiz)
- ✅ **Google Places API** - Mekan verileri, fotoğraflar, yorumlar  
- ✅ **Google Maps API** - Haritalar ve geocoding
- ✅ **MongoDB** - Veritabanı (Docker container)
- ✅ **Redis** - Cache (Docker container)

### Kod Lokasyonları:
- `backend/services/gemini_ai_service.py` - AI servisi
- `backend/services/google_places.py` - Places API
- `backend/services/google_places_reviews.py` - Yorumlar
- `backend/database.py` - API anahtarları
- `backend/requirements.txt` - Google bağımlılıkları

---

## 🎯 AWS Karşılıkları ve Maliyetler

| Google Service | AWS Karşılığı | Aylık Maliyet (Tahmini) |
|---|---|---|
| **Gemini AI** | **Amazon Bedrock** (Claude-3) | $15-30 |
| **Places API** | **Amazon Location Service** + HERE/Esri | $50-100 |
| **Maps API** | **Amazon Location Service** | $20-40 |
| **MongoDB** | **Amazon DocumentDB** | $200-400 |
| **Redis** | **Amazon ElastiCache** | $50-100 |
| **Hosting** | **AWS ECS/EKS** | $100-200 |
| **TOPLAM** | | **$435-870/ay** |

---

## 📋 Geçiş Adımları (Öncelik Sırasına Göre)

### 🔥 Faz 1: AI Servisi Geçişi (2-3 gün)

#### Adım 1.1: AWS Bedrock Kurulumu
```bash
# AWS CLI kurulumu
pip install boto3 awscli

# AWS hesabı yapılandırması
aws configure
```

#### Adım 1.2: Bedrock API Entegrasyonu
- `gemini_ai_service.py` → `bedrock_ai_service.py`
- Claude-3 Sonnet modeli kullanımı
- API anahtarları güncelleme

#### Adım 1.3: Test ve Doğrulama
- AI tahmin fonksiyonlarını test et
- Performans karşılaştırması yap

### 🗺️ Faz 2: Mekan Servisleri Geçişi (3-5 gün)

#### Adım 2.1: Amazon Location Service Kurulumu
- Place Index oluşturma
- HERE veya Esri veri sağlayıcısı seçimi
- API endpoint'lerini güncelleme

#### Adım 2.2: Kod Güncellemeleri
- `google_places.py` → `aws_location_service.py`
- `google_places_reviews.py` → `aws_places_reviews.py`
- Fotoğraf URL'lerini güncelle

#### Adım 2.3: Veri Migrasyonu
- Mevcut mekan verilerini AWS'ye taşı
- Fotoğraf linklerini güncelle

### 💾 Faz 3: Veritabanı Geçişi (2-3 gün)

#### Adım 3.1: Amazon DocumentDB Kurulumu
- Cluster oluşturma
- Security group yapılandırması
- SSL sertifikası kurulumu

#### Adım 3.2: Veri Migrasyonu
```bash
# MongoDB'den DocumentDB'ye veri aktarımı
mongodump --host localhost:27017 --db isitbusy
mongorestore --host docdb-cluster.cluster-xxx.us-east-1.docdb.amazonaws.com:27017 --ssl --sslCAFile rds-combined-ca-bundle.pem --username admin --password
```

#### Adım 3.3: ElastiCache Redis Kurulumu
- Redis cluster oluşturma
- Connection string güncelleme

### 🚀 Faz 4: Deployment Geçişi (3-5 gün)

#### Adım 4.1: AWS ECS/EKS Hazırlığı
- Docker image'ları AWS ECR'ye push et
- Task definition'ları oluştur
- Load balancer yapılandırması

#### Adım 4.2: Environment Variables
```bash
# Yeni AWS environment variables
AWS_ACCESS_KEY_ID=xxx
AWS_SECRET_ACCESS_KEY=xxx
AWS_REGION=us-east-1
BEDROCK_MODEL_ID=anthropic.claude-3-sonnet-20240229-v1:0
LOCATION_SERVICE_INDEX_NAME=isitbusy-places
DOCUMENTDB_CONNECTION_STRING=mongodb://admin:pass@docdb-cluster.cluster-xxx.us-east-1.docdb.amazonaws.com:27017/isitbusy?ssl=true&replicaSet=rs0&readPreference=secondaryPreferred&retryWrites=false
ELASTICACHE_ENDPOINT=isitbusy-redis.xxx.cache.amazonaws.com:6379
```

#### Adım 4.3: Monitoring ve Logging
- CloudWatch Logs kurulumu
- X-Ray tracing aktifleştirme
- CloudWatch Metrics dashboard'u

### 🔍 Faz 5: Test ve Optimizasyon (3-5 gün)

#### Adım 5.1: Fonksiyonel Testler
- AI tahmin doğruluğu
- Mekan arama performansı
- Veritabanı bağlantı testleri

#### Adım 5.2: Performans Testleri
- Load testing
- Latency ölçümü
- Cost optimization

#### Adım 5.3: Güvenlik Testleri
- IAM role'leri doğrulama
- VPC security group'ları
- SSL/TLS sertifikaları

---

## 💰 Maliyet Analizi

### Mevcut Google Cloud Maliyetleri:
- **Gemini AI**: Ücretsiz (1500/gün limit)
- **Places API**: $17/1000 istek
- **Maps API**: $7/1000 istek
- **Hosting**: Kendi sunucunuz

### AWS Maliyetleri (Aylık):
- **Bedrock**: $15-30 (kullanıma göre)
- **Location Service**: $50-100
- **DocumentDB**: $200-400 (instance boyutuna göre)
- **ElastiCache**: $50-100
- **ECS/EKS**: $100-200
- **Data Transfer**: $20-50

**Toplam Tahmini**: $435-870/ay

### Maliyet Optimizasyonu:
- Reserved Instances kullanımı (%30-50 tasarruf)
- Spot Instances (geliştirme ortamı için)
- Auto Scaling ile kaynak optimizasyonu

---

## ⚠️ Riskler ve Çözümler

### Risk 1: API Limitleri
- **Google**: 1500/gün ücretsiz Gemini
- **AWS**: Pay-per-use, limit yok
- **Çözüm**: Kademeli geçiş, cache kullanımı

### Risk 2: Veri Kaybı
- **Çözüm**: Tam backup alın, paralel çalıştırın
- **Test**: Staging ortamında önce test edin

### Risk 3: Downtime
- **Çözüm**: Blue-green deployment
- **Plan**: Hafta sonu geçiş yapın

### Risk 4: Performans Farkları
- **Çözüm**: Benchmark testleri yapın
- **Monitoring**: CloudWatch ile sürekli izleyin

---

## 📅 Zaman Çizelgesi

| Hafta | Faz | Aktiviteler | Durum |
|---|---|---|---|
| **Hafta 1** | Faz 1-2 | AI + Places API geçişi | 🔄 |
| **Hafta 2** | Faz 3 | Veritabanı migrasyonu | ⏳ |
| **Hafta 3** | Faz 4 | Deployment ve monitoring | ⏳ |
| **Hafta 4** | Faz 5 | Test, optimizasyon, go-live | ⏳ |

**Toplam Süre**: 3-4 hafta
**Effort**: 15-20 iş günü

---

## 🛠️ Gerekli Araçlar

### AWS Servisleri:
- ✅ **Amazon Bedrock** - AI/ML
- ✅ **Amazon Location Service** - Maps/Places
- ✅ **Amazon DocumentDB** - MongoDB uyumlu
- ✅ **Amazon ElastiCache** - Redis
- ✅ **Amazon ECS/EKS** - Container hosting
- ✅ **Amazon ECR** - Container registry
- ✅ **CloudWatch** - Monitoring
- ✅ **AWS Secrets Manager** - API key yönetimi

### Geliştirme Araçları:
- AWS CLI
- Docker
- Terraform (Infrastructure as Code)
- GitHub Actions (CI/CD)

---

## 🚦 Başlamaya Hazır mısınız?

1. **AWS hesabı açın** (eğer yoksa)
2. **Billing alerts** kurun
3. **IAM user** oluşturun (programmatic access)
4. **Bu planı onaylayın**

**Sonraki adım**: Hangi fazdan başlamak istiyorsunuz?