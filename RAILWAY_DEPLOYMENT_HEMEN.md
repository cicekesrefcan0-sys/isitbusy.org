# 🚂 RAILWAY BACKEND DEPLOYMENT - HEMEN BAŞLA

## ✅ HAZIR OLAN BİLGİLER

**MongoDB Connection:** `mongodb+srv://cicekesrefcan0_db_user:<db_password>@cluster0.e6qgkhr.mongodb.net/isitbusy?appName=Cluster0`
**Google Places API:** `AIzaSyDRoQx4vJlTEioqyO7oQYdjSIJUeCb3Drs`
**Gemini AI API:** `AIzaSyAxFCNANlrUWD5VspWGWLM6i4VB4H7exoE`

---

## 🎯 RAILWAY DEPLOYMENT ADIM ADIM

### 1️⃣ RAILWAY'E GİT
**Link:** https://railway.app

### 2️⃣ GİRİŞ YAP
- **"Login with GitHub"** tıkla
- **cicekesrefcan0@gmail.com** hesabıyla giriş yap

### 3️⃣ YENİ PROJE OLUŞTUR
1. **"New Project"** butonuna tıkla
2. **"Deploy from GitHub repo"** seç
3. **"esref1-main"** repository'sini seç
4. **"Deploy Now"** tıkla

### 4️⃣ ROOT DIRECTORY AYARLA
1. Deployment başladıktan sonra **"Settings"** sekmesine git
2. **"Service"** altında **"Root Directory"** bul
3. **"backend"** yaz (çünkü backend kodu esref1-main/backend klasöründe)
4. **"Save"** tıkla

### 5️⃣ ENVIRONMENT VARIABLES EKLE
**"Variables"** sekmesine git ve şu değişkenleri ekle:

```
MONGO_URL=mongodb+srv://cicekesrefcan0_db_user:GERÇEK_ŞİFRE@cluster0.e6qgkhr.mongodb.net/isitbusy?appName=Cluster0
GOOGLE_PLACES_API_KEY=AIzaSyDRoQx4vJlTEioqyO7oQYdjSIJUeCb3Drs
GEMINI_API_KEY=AIzaSyAxFCNANlrUWD5VspWGWLM6i4VB4H7exoE
JWT_SECRET=isitbusy_super_secret_jwt_key_2024_production_ready_32_chars
CORS_ORIGINS=https://isitbusy.org,https://www.isitbusy.org
PORT=8000
ENVIRONMENT=production
```

**ÖNEMLİ:** `GERÇEK_ŞİFRE` yerine MongoDB Atlas'ta oluşturduğun şifreyi yaz!

### 6️⃣ DEPLOYMENT BEKLE
- Railway otomatik olarak backend'i deploy edecek
- **"Deployments"** sekmesinden durumu takip et
- Yeşil ✅ görene kadar bekle

### 7️⃣ DOMAIN AYARLA
1. **"Settings"** → **"Domains"** git
2. **"Custom Domain"** tıkla
3. **"api.isitbusy.org"** yaz
4. **"Add"** tıkla

---

## 🧪 TEST ETME

**Deployment tamamlandıktan sonra:**

1. **Railway URL'ini test et:** https://[railway-url]/health
2. **Custom domain'i test et:** https://api.isitbusy.org/health

**Beklenen sonuç:**
```json
{"status": "healthy", "timestamp": "2024-01-18T..."}
```

---

## ⚡ SONRAKI ADIM: DNS AYARLARI

**Railway deployment tamamlandıktan sonra:**
1. Domain provider'a git (isitbusy.org'u aldığın yer)
2. DNS kayıtlarını ayarla
3. Full-stack test et

**HEMEN BAŞLAYALIM!** 🚀

---

## 🆘 SORUN ÇÖZME

**Deployment başarısız olursa:**
1. **"Logs"** sekmesini kontrol et
2. Environment variables'ları kontrol et
3. Root directory'nin "backend" olduğunu kontrol et

**MongoDB bağlantı hatası:**
- MongoDB Atlas'ta şifreyi kontrol et
- Network access'in 0.0.0.0/0 olduğunu kontrol et