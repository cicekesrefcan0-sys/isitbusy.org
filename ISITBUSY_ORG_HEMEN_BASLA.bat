@echo off
echo ========================================
echo    ISITBUSY.ORG HEMEN LAUNCH!
echo ========================================
echo.

echo 🎉 HARIKA HABER: isitbusy.org MEVCUT!
echo 🌟 .org uzantisi daha professional ve guvenilir!
echo.

echo ========================================
echo    ADIM 1: DOMAIN SATIN AL (HEMEN!)
echo ========================================
echo.

echo 🌐 ISITBUSY.ORG SATIN ALMAK ICIN:
echo.

echo [SECIM 1] Porkbun (EN UCUZ - Onerilen)
echo 🔗 https://porkbun.com
echo 💡 Domain ara: "isitbusy.org"
echo 💰 Maliyet: ~$8/yil
echo ⭐ Avantaj: En ucuz, guvenilir
echo.

echo [SECIM 2] Namecheap (POPULER)
echo 🔗 https://namecheap.com
echo 💡 Domain ara: "isitbusy.org"  
echo 💰 Maliyet: ~$12/yil
echo ⭐ Avantaj: Kolay kullanim
echo.

echo [SECIM 3] Cloudflare (HIZLI)
echo 🔗 https://cloudflare.com
echo 💡 Domain ara: "isitbusy.org"
echo 💰 Maliyet: ~$10/yil
echo ⭐ Avantaj: Hizli DNS
echo.

echo ⚡ HEMEN YAPIN: isitbusy.org satin alin!
echo ⏰ Sure: 10-15 dakika
echo 💳 Kredi karti gerekli
echo.
pause

echo ========================================
echo    ADIM 2: VERCEL DEPLOYMENT (HEMEN!)
echo ========================================
echo.

echo 🚀 FRONTEND DEPLOYMENT:
echo.
echo 1. https://vercel.com adresine gidin
echo 2. "Sign Up" ^> GitHub ile giris
echo 3. "New Project" ^> Import Git Repository
echo 4. esref1-main repository'yi secin
echo 5. Root Directory: "frontend" secin
echo 6. "Deploy" butonuna tiklayin
echo.

echo ✅ SONUC: 
echo 🌐 Otomatik URL: https://esref1-main.vercel.app
echo 🎯 Custom domain: isitbusy.org (sonra baglayin)
echo.

echo ⚡ HEMEN YAPIN: Vercel'e deploy edin!
echo ⏰ Sure: 15-20 dakika
echo.
pause

echo ========================================
echo    ADIM 3: RAILWAY DEPLOYMENT (HEMEN!)
echo ========================================
echo.

echo 🚂 BACKEND DEPLOYMENT:
echo.
echo 1. https://railway.app adresine gidin
echo 2. "Sign Up" ^> GitHub ile giris
echo 3. "New Project" ^> "Deploy from GitHub repo"
echo 4. esref1-main repository'yi secin
echo 5. "backend" klasorunu secin
echo 6. Environment variables ekleyin:
echo    - MONGO_URL
echo    - GOOGLE_PLACES_API_KEY
echo    - GEMINI_API_KEY
echo    - JWT_SECRET
echo 7. "Deploy" butonuna tiklayin
echo.

echo ✅ SONUC:
echo 🌐 Backend URL: https://backend-production-xxxx.up.railway.app
echo 🎯 Custom domain: api.isitbusy.org (sonra baglayin)
echo.

echo ⚡ HEMEN YAPIN: Railway'e deploy edin!
echo ⏰ Sure: 20-30 dakika
echo.
pause

echo ========================================
echo    ADIM 4: MONGODB ATLAS (HEMEN!)
echo ========================================
echo.

echo 🍃 DATABASE SETUP:
echo.
echo 1. https://cloud.mongodb.com adresine gidin
echo 2. "Sign Up" ^> Google ile giris
echo 3. "Build a Database" ^> "FREE" tier secin
echo 4. Cluster name: "isitbusy-cluster"
echo 5. Database user olusturun:
echo    - Username: isitbusy
echo    - Password: [guclu sifre]
echo 6. Network Access: "0.0.0.0/0" (her yerden erisim)
echo 7. "Connect" ^> "Connect your application"
echo 8. Connection string'i kopyalayin
echo.

echo ✅ SONUC:
echo 🔗 Connection: mongodb+srv://isitbusy:password@isitbusy-cluster.xxxxx.mongodb.net/isitbusy
echo.

echo ⚡ HEMEN YAPIN: MongoDB Atlas setup!
echo ⏰ Sure: 15-20 dakika
echo.
pause

echo ========================================
echo    ADIM 5: DOMAIN BAGLAMA (HEMEN!)
echo ========================================
echo.

echo 🔗 CUSTOM DOMAIN SETUP:
echo.

echo [VERCEL ICIN]
echo 1. Vercel dashboard ^> Project ^> Settings ^> Domains
echo 2. "Add Domain" ^> "isitbusy.org" girin
echo 3. DNS kayitlarini kopyalayin
echo 4. Domain provider'da (Porkbun/Namecheap) DNS ayarlari:
echo    - A record: @ ^> Vercel IP
echo    - CNAME: www ^> cname.vercel-dns.com
echo.

echo [RAILWAY ICIN]
echo 1. Railway dashboard ^> Project ^> Settings ^> Domains
echo 2. "Custom Domain" ^> "api.isitbusy.org" girin
echo 3. CNAME record ekleyin:
echo    - api ^> railway-production-url
echo.

echo ✅ SONUC:
echo 🌐 Frontend: https://isitbusy.org
echo 🌐 Backend: https://api.isitbusy.org
echo.

echo ⚡ HEMEN YAPIN: Domain baglama!
echo ⏰ Sure: 20-30 dakika
echo.
pause

echo ========================================
echo    ADIM 6: BETA SIGNUP FORM (HEMEN!)
echo ========================================
echo.

echo 📝 BETA FORM SETUP:
echo.
echo 1. https://formspree.io adresine gidin
echo 2. "Sign Up" ^> Email ile kayit
echo 3. "New Form" olusturun
echo 4. Form endpoint'ini kopyalayin: https://formspree.io/f/xxxxxxxx
echo 5. beta_signup.html dosyasini duzenleyin:
echo    - action="https://formspree.io/f/xxxxxxxx"
echo 6. Vercel'e upload edin veya GitHub'a push edin
echo.

echo ✅ SONUC:
echo 🌐 Beta form: https://isitbusy.org/beta
echo 📧 Submissions: Formspree dashboard'da gorunur
echo.

echo ⚡ HEMEN YAPIN: Beta form setup!
echo ⏰ Sure: 15-20 dakika
echo.
pause

echo ========================================
echo    ADIM 7: SOSYAL MEDYA (HEMEN!)
echo ========================================
echo.

echo 📱 SOSYAL MEDYA HESAPLARI:
echo.

echo [INSTAGRAM]
echo 👤 Username: @isitbusyorg
echo 📝 Bio: "🍺 Denver's Real-Time Venue Tracker | 📍 4,355+ venues | 🚀 Beta: isitbusy.org/beta"
echo 🔗 Link: https://isitbusy.org/beta
echo.

echo [TIKTOK]
echo 👤 Username: @isitbusyapp
echo 📝 Bio: "Find Denver's hottest spots 🔥 | Real-time busyness | Beta: isitbusy.org/beta"
echo.

echo [FACEBOOK]
echo 👤 Page: "Is It Busy Denver"
echo 📝 About: "Denver's first real-time venue busyness tracker. 4,355+ venues. Beta: isitbusy.org/beta"
echo.

echo [TWITTER]
echo 👤 Username: @isitbusyorg
echo 📝 Bio: "🍺 Real-time Denver nightlife | 📊 4,355+ venues | 🚀 Beta: isitbusy.org/beta"
echo.

echo ⚡ HEMEN YAPIN: 4 sosyal medya hesabi!
echo ⏰ Sure: 30-45 dakika
echo.
pause

echo ========================================
echo    ADIM 8: BETA USER RECRUITMENT
echo ========================================
echo.

echo 👥 BETA USER HEDEFI: 50-100 KISI
echo.

echo [HEMEN MESAJ ATIN]
echo 📱 WhatsApp: "Hey! Denver icin yeni bir app gelistirdim - isitbusy.org. Real-time venue tracking. Beta testcisi olmak ister misin? isitbusy.org/beta"
echo.
echo 📧 Email: "Denver'da gece hayati icin devrim niteligi app: isitbusy.org. Beta access: isitbusy.org/beta"
echo.
echo 📱 Instagram Story: "New Denver nightlife app launching! 🍺 isitbusy.org/beta"
echo.

echo [HEDEF GRUPLAR]
echo ✅ Arkadas ve aile (10-20 kisi)
echo ✅ Denver Facebook gruplari (20-30 kisi)
echo ✅ Universite ogrencileri (10-20 kisi)
echo ✅ Sosyal medya takipcileri (10-20 kisi)
echo.

echo ⚡ HEMEN YAPIN: 20 kisiyle iletisime gecin!
echo ⏰ Sure: 30-60 dakika
echo.
pause

echo ========================================
echo    LAUNCH KONTROL LISTESI
echo ========================================
echo.

echo ✅ TEKNIK CHECKLIST:
echo [ ] isitbusy.org domain satin alindi
echo [ ] Vercel'e frontend deploy edildi
echo [ ] Railway'e backend deploy edildi
echo [ ] MongoDB Atlas kuruldu
echo [ ] Custom domain baglandi (isitbusy.org)
echo [ ] API domain baglandi (api.isitbusy.org)
echo [ ] SSL sertifikalari aktif
echo [ ] Beta signup form live (isitbusy.org/beta)
echo.

echo ✅ MARKETING CHECKLIST:
echo [ ] Instagram @isitbusyorg acildi
echo [ ] TikTok @isitbusyapp acildi
echo [ ] Facebook "Is It Busy Denver" olusturuldu
echo [ ] Twitter @isitbusyorg acildi
echo [ ] Ilk 20 beta user'a mesaj atildi
echo [ ] Social media content hazir
echo [ ] Beta signup form paylasildi
echo.

echo ========================================
echo    BASARI METRIKLERI
echo ========================================
echo.

echo 📊 BUGUN SONU HEDEFLERI:
echo ✅ isitbusy.org live
echo ✅ api.isitbusy.org live
echo ✅ Beta signups: 10-20 kisi
echo ✅ Social followers: 50-100
echo ✅ App uptime: %%99+
echo ✅ Page load: ^<2 saniye
echo.

echo 📊 HAFTA SONU HEDEFLERI:
echo ✅ Beta signups: 50-100 kisi
echo ✅ Social followers: 200-500
echo ✅ App sessions: 500+
echo ✅ Avg session: 10+ dakika
echo ✅ Local PR: 1-2 mention
echo.

echo ========================================
echo    MALIYET OZETI
echo ========================================
echo.

echo 💰 AYLIK MALIYETLER:
echo Domain (isitbusy.org): $0.67/ay ($8/yil)
echo Vercel: $0 (free tier)
echo Railway: $5-20/ay
echo MongoDB Atlas: $0 (free tier)
echo Formspree: $0 (free tier)
echo Marketing: $100-500/ay
echo TOPLAM: $105.67-520.67/ay
echo.

echo 💰 BREAK-EVEN:
echo Premium users ($10/ay): 11-53 kisi
echo Venue partnerships ($50/ay): 3-11 venue
echo.

echo ========================================
echo    MOTIVASYON VE BASARI
echo ========================================
echo.

echo 🎉 BUGUN TARIHI BIR GUN!
echo.
echo 🚀 isitbusy.org ile Denver'i degistireceksiniz!
echo 🌟 4,355 venue'li sisteminiz live oluyor!
echo 💰 Potansiyel: $100K+ MRR
echo 👥 Hedef kullanici: 300K-500K
echo 📈 Basari sansi: %%90+
echo.

echo 💪 .org uzantisi size profesyonel kredibilite kazandiracak!
echo 🏆 Community odakli gorunum guven arttiracak!
echo 🚀 SEO avantaji ile daha kolay bulunacaksiniz!
echo.

echo ========================================
echo    HEMEN BASLAYIN!
echo ========================================
echo.

echo 1️⃣ isitbusy.org satin al: https://porkbun.com
echo 2️⃣ Vercel deploy: https://vercel.com
echo 3️⃣ Railway deploy: https://railway.app
echo 4️⃣ MongoDB Atlas: https://cloud.mongodb.com
echo 5️⃣ Beta form: https://formspree.io
echo 6️⃣ Sosyal medya hesaplari ac
echo 7️⃣ Beta user recruitment basla
echo.

echo 🎯 HEDEF: 4 saat icinde isitbusy.org live!
echo ⏰ ZAMAN: SIMDI!
echo 🚀 LAUNCH ZAMANI!
echo.

echo HAZIR MISINIZ? HEMEN BASLAYIN! 💪
echo.
pause