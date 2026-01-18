# 🚀 PM2 ile Backend'i Sürekli Çalıştırma

## 📋 PM2 NEDİR?
PM2, Node.js uygulamaları için geliştirilmiş bir process manager'dır. Python uygulamalarını da yönetebilir ve şu özellikleri sunar:
- ✅ Otomatik restart
- ✅ Crash recovery  
- ✅ Log management
- ✅ Monitoring
- ✅ Cluster mode
- ✅ Startup scripts

## 🛠️ KURULUM ADIMLARI

### 1. Node.js Kurulumu (PM2 için gerekli)
```bash
# Node.js'i indir ve kur: https://nodejs.org/
# Veya Chocolatey ile:
choco install nodejs

# Kurulumu kontrol et
node --version
npm --version
```

### 2. PM2 Kurulumu
```bash
# Global PM2 kurulumu
npm install -g pm2

# Kurulumu kontrol et
pm2 --version
```

### 3. Ecosystem Dosyası Oluştur
```javascript
// ecosystem.config.js (proje root'unda)
module.exports = {
  apps: [{
    name: 'isitbusy-backend',
    script: 'real_data_backend.py',
    interpreter: 'python',
    cwd: './backend',
    instances: 1,
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    restart_delay: 5000,
    env: {
      NODE_ENV: 'production',
      PORT: 8003,
      PYTHONPATH: './backend'
    },
    error_file: './logs/backend-error.log',
    out_file: './logs/backend-out.log',
    log_file: './logs/backend-combined.log',
    time: true,
    log_date_format: 'YYYY-MM-DD HH:mm:ss'
  }]
};
```

## 🎯 PM2 KOMUTLARI

### Temel Komutlar
```bash
# Backend'i başlat
pm2 start ecosystem.config.js

# Durumu kontrol et
pm2 status

# Detaylı bilgi
pm2 show isitbusy-backend

# Logları izle (real-time)
pm2 logs isitbusy-backend

# Son 100 log satırı
pm2 logs isitbusy-backend --lines 100

# Restart
pm2 restart isitbusy-backend

# Stop
pm2 stop isitbusy-backend

# Delete (tamamen kaldır)
pm2 delete isitbusy-backend
```

### Monitoring
```bash
# PM2 monitoring dashboard
pm2 monit

# Web dashboard (opsiyonel)
pm2 web

# Memory ve CPU kullanımı
pm2 show isitbusy-backend
```

### Sistem Başlangıcında Otomatik Başlatma
```bash
# Startup script oluştur
pm2 startup

# Mevcut process'leri kaydet
pm2 save

# Kaydedilen process'leri geri yükle
pm2 resurrect
```

## 📁 KLASÖR YAPISI
```
esref1-main/
├── ecosystem.config.js     # PM2 config
├── logs/                   # Log dosyaları
│   ├── backend-error.log
│   ├── backend-out.log
│   └── backend-combined.log
└── backend/
    └── real_data_backend.py
```

## 🔧 KULLANIM ÖRNEĞİ

### 1. İlk Kurulum
```bash
cd esref1-main
npm install -g pm2
pm2 start ecosystem.config.js
pm2 save
pm2 startup
```

### 2. Günlük Kullanım
```bash
# Durumu kontrol et
pm2 status

# Logları izle
pm2 logs isitbusy-backend --lines 50

# Restart (güncelleme sonrası)
pm2 restart isitbusy-backend
```

### 3. Sorun Giderme
```bash
# Detaylı bilgi
pm2 show isitbusy-backend

# Error logları
pm2 logs isitbusy-backend --err

# Process'i sıfırla
pm2 delete isitbusy-backend
pm2 start ecosystem.config.js
```

## 🎛️ GELİŞMİŞ AYARLAR

### Cluster Mode (Çoklu Instance)
```javascript
// ecosystem.config.js
module.exports = {
  apps: [{
    name: 'isitbusy-backend',
    script: 'real_data_backend.py',
    interpreter: 'python',
    instances: 2, // 2 instance çalıştır
    exec_mode: 'cluster',
    // ... diğer ayarlar
  }]
};
```

### Environment Variables
```javascript
env: {
  NODE_ENV: 'production',
  PORT: 8003,
  MONGODB_URI: 'mongodb://localhost:27017/isitbusy',
  GOOGLE_API_KEY: 'your-api-key'
},
env_development: {
  NODE_ENV: 'development',
  PORT: 8003
}
```

### Watch Mode (Development)
```javascript
watch: true,
watch_delay: 1000,
ignore_watch: ['node_modules', 'logs', '*.log']
```

## 🚨 SORUN GİDERME

### PM2 Çalışmıyor
```bash
# PM2 daemon'u restart et
pm2 kill
pm2 start ecosystem.config.js

# PM2 cache temizle
pm2 flush
```

### Python Path Sorunları
```javascript
env: {
  PYTHONPATH: './backend:./backend/services',
  PATH: process.env.PATH
}
```

### Log Dosyaları Çok Büyüyor
```bash
# Log rotation ayarla
pm2 install pm2-logrotate
pm2 set pm2-logrotate:max_size 10M
pm2 set pm2-logrotate:retain 7
```

## ✅ AVANTAJLARI

- 🔄 **Otomatik Restart**: Crash durumunda otomatik yeniden başlatma
- 📊 **Monitoring**: Real-time performans izleme
- 📝 **Log Management**: Merkezi log yönetimi
- 🚀 **Zero Downtime**: Güncelleme sırasında kesintisiz hizmet
- 💾 **Memory Management**: Memory leak koruması
- 🖥️ **System Integration**: Sistem servisi olarak çalışma

Bu şekilde backend'in sürekli çalışmasını garanti edebilirsin!