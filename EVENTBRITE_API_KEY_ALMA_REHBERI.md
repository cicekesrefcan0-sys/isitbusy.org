# 🔑 EVENTBRITE API KEY ALMA REHBERİ

## 1. Eventbrite Developer Hesabı Oluşturma

### Adım 1: Eventbrite'a Kayıt Olun
1. https://www.eventbrite.com adresine gidin
2. "Sign Up" ile hesap oluşturun
3. Email doğrulaması yapın

### Adım 2: Developer Portal'a Erişim
1. https://www.eventbrite.com/platform/api adresine gidin
2. "Get Started" butonuna tıklayın
3. Developer hesabınızla giriş yapın

### Adım 3: Uygulama Oluşturma
1. "Create App" butonuna tıklayın
2. Uygulama bilgilerini doldurun:
   - **App Name**: "Colorado Events Scraper"
   - **Description**: "Colorado etkinliklerini çeken uygulama"
   - **Website URL**: "http://localhost:3000"
   - **OAuth Redirect URI**: "http://localhost:3000/callback"

### Adım 4: API Key'i Alma
1. Uygulama oluşturulduktan sonra "API Keys" sekmesine gidin
2. **Private Token**'ı kopyalayın (bu bizim API key'imiz)

## 2. API Key'i Projeye Ekleme

### Backend .env Dosyası
```bash
# esref1-main/backend/.env dosyasına ekleyin
EVENTBRITE_API_KEY=YOUR_PRIVATE_TOKEN_HERE
```

### Test Etme
```bash
# Test scripti ile kontrol edin
py TEST_EVENTBRITE_COLORADO.py
```

## 3. API Limitleri

### Ücretsiz Plan
- **5,000 API calls/hour**
- **50,000 API calls/day**
- Temel etkinlik bilgileri

### Ücretli Plan
- Daha yüksek limitler
- Gelişmiş özellikler
- Premium support

## 4. Güvenlik Notları

⚠️ **ÖNEMLİ**: API key'inizi asla public repository'lerde paylaşmayın!

- `.env` dosyasını `.gitignore`'a ekleyin
- Environment variables kullanın
- Production'da güvenli key management kullanın

## 5. Hızlı Test

API key'inizi aldıktan sonra:

```bash
# 1. API key'i .env dosyasına ekleyin
echo "EVENTBRITE_API_KEY=your_key_here" >> backend/.env

# 2. Test scripti çalıştırın
py TEST_EVENTBRITE_COLORADO.py

# 3. Gerçek veri çekin
curl -X POST http://localhost:8000/api/eventbrite/scrape
```

## 6. Sorun Giderme

### API Key Çalışmıyor
- Key'in doğru kopyalandığından emin olun
- Boşluk karakteri olmadığını kontrol edin
- Eventbrite hesabınızın aktif olduğunu doğrulayın

### Rate Limit Hatası
- API çağrı limitinizi aştınız
- 1 saat bekleyin veya ücretli plana geçin

### 401 Unauthorized
- API key yanlış veya geçersiz
- Yeni key oluşturmayı deneyin

---

**Not**: API key almak ücretsizdir, sadece Eventbrite hesabı gerekir.