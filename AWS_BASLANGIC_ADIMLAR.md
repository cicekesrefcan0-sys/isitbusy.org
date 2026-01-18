# 🚀 AWS Geçiş - İlk Adımlar

## 1️⃣ AWS Hesabı Hazırlığı (30 dakika)

### AWS Hesabı Açın
```bash
# 1. https://aws.amazon.com/free/ adresine gidin
# 2. "Create Free Account" tıklayın
# 3. Email, şifre, hesap adı girin
# 4. Kredi kartı bilgilerini girin (sadece doğrulama için)
# 5. Telefon doğrulaması yapın
```

### IAM User Oluşturun
```bash
# AWS Console → IAM → Users → Add User
# Username: isitbusy-developer
# Access type: Programmatic access
# Permissions: AdministratorAccess (geçici)
# Download CSV file (Access Key + Secret Key)
```

### AWS CLI Kurulumu
```bash
# Windows
curl "https://awscli.amazonaws.com/AWSCLIV2.msi" -o "AWSCLIV2.msi"
msiexec /i AWSCLIV2.msi

# Yapılandırma
aws configure
# AWS Access Key ID: [CSV'den kopyalayın]
# AWS Secret Access Key: [CSV'den kopyalayın]  
# Default region: us-east-1
# Default output format: json
```

---

## 2️⃣ Maliyet Kontrolü Kurulumu (15 dakika)

### Billing Alerts
```bash
# AWS Console → Billing → Billing preferences
# ✅ Receive PDF Invoice By Email
# ✅ Receive Free Tier Usage Alerts
# ✅ Receive Billing Alerts

# CloudWatch → Alarms → Create Alarm
# Metric: EstimatedCharges
# Threshold: $50 (aylık limit)
# Action: SNS notification
```

### Cost Budget
```bash
# AWS Console → AWS Budgets → Create budget
# Budget type: Cost budget
# Amount: $100/month
# Alert threshold: 80% ($80)
```

---

## 3️⃣ İlk Test: Bedrock AI (1 saat)

### Bedrock Servisini Aktifleştirin
```bash
# AWS Console → Amazon Bedrock → Model access
# Request access to: Claude 3 Sonnet
# Reason: AI-powered venue busyness predictions
# Wait for approval (usually 5-10 minutes)
```

### Test Scripti Oluşturun
```python
# test_bedrock.py
import boto3
import json

def test_bedrock_ai():
    client = boto3.client('bedrock-runtime', region_name='us-east-1')
    
    prompt = "Predict if a nightclub will be busy on Friday night at 10 PM"
    
    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 200,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    })
    
    response = client.invoke_model(
        modelId='anthropic.claude-3-sonnet-20240229-v1:0',
        body=body,
        contentType='application/json'
    )
    
    result = json.loads(response['body'].read())
    print("Bedrock AI Response:", result['content'][0]['text'])

if __name__ == "__main__":
    test_bedrock_ai()
```

### Testi Çalıştırın
```bash
pip install boto3
python test_bedrock.py
```

---

## 4️⃣ Mevcut Sistemi Yedekleyin (30 dakika)

### MongoDB Backup
```bash
# Mevcut veritabanını yedekleyin
cd esref1-main
mongodump --host localhost:27017 --db isitbusy --out ./backup/mongodb_backup_$(date +%Y%m%d)

# Backup dosyasını sıkıştırın
tar -czf mongodb_backup_$(date +%Y%m%d).tar.gz ./backup/mongodb_backup_$(date +%Y%m%d)
```

### Kod Backup
```bash
# Git repository'yi yedekleyin
git add .
git commit -m "Pre-AWS migration backup"
git tag -a "pre-aws-migration" -m "Backup before AWS migration"

# Alternatif: ZIP backup
7z a -r esref1_backup_$(date +%Y%m%d).zip esref1-main/
```

### Environment Variables Backup
```bash
# Mevcut .env dosyalarını yedekleyin
cp esref1-main/backend/.env esref1-main/backend/.env.backup
cp esref1-main/frontend/.env esref1-main/frontend/.env.backup
cp esref1-main/.env .env.backup
```

---

## 5️⃣ Geçiş Stratejisi Seçimi

### Seçenek A: Kademeli Geçiş (Önerilen)
```
✅ Avantajlar:
- Düşük risk
- Sürekli çalışan sistem
- Geri dönüş kolay

❌ Dezavantajlar:
- Daha uzun süre
- İki sistem paralel çalışır
```

### Seçenek B: Tam Geçiş
```
✅ Avantajlar:
- Hızlı geçiş
- Tek seferlik iş

❌ Dezavantajlar:
- Yüksek risk
- Downtime riski
```

**Önerim**: Seçenek A (Kademeli Geçiş)

---

## 6️⃣ İlk Geçiş: AI Servisi (Bugün başlayabilirsiniz!)

### Yeni AI Servisi Oluşturun
```python
# backend/services/aws_bedrock_service.py
import boto3
import json
import logging
from typing import Optional

logger = logging.getLogger(__name__)

class AWSBedrockService:
    def __init__(self):
        self.client = boto3.client('bedrock-runtime', region_name='us-east-1')
        self.model_id = 'anthropic.claude-3-sonnet-20240229-v1:0'
    
    async def predict_busyness(self, venue_data: dict) -> dict:
        """AWS Bedrock ile mekan yoğunluğu tahmini"""
        try:
            prompt = f"""
            Venue: {venue_data.get('name', 'Unknown')}
            Type: {venue_data.get('type', 'Unknown')}
            Time: {venue_data.get('current_time', 'Now')}
            
            Predict busyness level (1-5) and explain reasoning.
            """
            
            body = json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 300,
                "messages": [{"role": "user", "content": prompt}]
            })
            
            response = self.client.invoke_model(
                modelId=self.model_id,
                body=body,
                contentType='application/json'
            )
            
            result = json.loads(response['body'].read())
            ai_response = result['content'][0]['text']
            
            return {
                "success": True,
                "prediction": ai_response,
                "source": "aws_bedrock",
                "model": "claude-3-sonnet"
            }
            
        except Exception as e:
            logger.error(f"Bedrock AI error: {e}")
            return {
                "success": False,
                "error": str(e),
                "fallback": "Unable to predict busyness"
            }

# Global instance
bedrock_service = AWSBedrockService()
```

### Mevcut Servisi Güncelleyin
```python
# backend/services/gemini_ai_service.py içine ekleyin
from .aws_bedrock_service import bedrock_service

async def predict_busyness_hybrid(venue_id: str) -> dict:
    """Hem Gemini hem Bedrock kullan (geçiş dönemi için)"""
    
    # Önce AWS Bedrock dene
    try:
        venue = await db.venues.find_one({"id": venue_id})
        if venue:
            bedrock_result = await bedrock_service.predict_busyness(venue)
            if bedrock_result.get("success"):
                return bedrock_result
    except Exception as e:
        logger.warning(f"Bedrock failed, falling back to Gemini: {e}")
    
    # Fallback: Gemini kullan
    return await predict_busyness_with_gemini(venue_id)
```

---

## 7️⃣ Test ve Doğrulama

### AI Servisi Testi
```bash
# Backend'i başlatın
cd esref1-main/backend
python server.py

# Test endpoint'ini çağırın
curl -X POST http://localhost:8001/ai/predict \
  -H "Content-Type: application/json" \
  -d '{"venue_id": "test_venue_123"}'
```

### Frontend Testi
```bash
# Frontend'i başlatın
cd esref1-main/frontend
npm start

# AI özelliklerini test edin
# - Mekan detay sayfasında AI tahminleri
# - Chat widget'ı
# - Busyness predictions
```

---

## 🎯 Sonraki Adımlar

1. **✅ AWS hesabı kurulumu** (30 dk)
2. **✅ Bedrock AI testi** (1 saat)
3. **✅ Mevcut sistem backup** (30 dk)
4. **🔄 AI servisi geçişi** (2-3 gün)
5. **⏳ Places API geçişi** (3-5 gün)
6. **⏳ Veritabanı geçişi** (2-3 gün)

**Hangi adımdan başlamak istiyorsunuz?**

### Hızlı Başlangıç Seçenekleri:

**A) Sadece AI geçişi** (düşük risk, hızlı sonuç)
**B) Tam geçiş planı** (kapsamlı, 3-4 hafta)
**C) Maliyet analizi** (önce hesaplayalım)

**Seçiminizi belirtin, size özel adımları hazırlayayım!**