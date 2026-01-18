#!/usr/bin/env python3
"""
AI Master Kontrol - Tüm kontrol scriptlerini tek yerden çalıştırır
"""
import os
import sys
import subprocess
import time

def run_script(script_name, description):
    """Script çalıştır ve sonucu göster"""
    print(f"\n{'='*60}")
    print(f"🔍 {description}")
    print(f"Script: {script_name}")
    print('='*60)
    
    try:
        # Python script'ini çalıştır
        result = subprocess.run([sys.executable, script_name], 
                              capture_output=True, 
                              text=True, 
                              timeout=60)
        
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        return result.returncode == 0
        
    except subprocess.TimeoutExpired:
        print("❌ Script timeout - 60 saniyede tamamlanmadı")
        return False
    except Exception as e:
        print(f"❌ Script çalıştırma hatası: {e}")
        return False

def main():
    """Ana kontrol fonksiyonu"""
    print("🤖 AI MASTER KONTROL - TÜM SİSTEM ANALİZİ")
    print("=" * 60)
    print("Bu script tüm kontrol araçlarını sırayla çalıştırır")
    print("Hangi aşamada sorun olduğunu tespit eder")
    print()
    
    # Mevcut dizini kontrol et
    if not os.path.exists("esref1-main"):
        print("❌ 'esref1-main' dizini bulunamadı!")
        print("Bu script'i doğru dizinden çalıştırdığınızdan emin olun")
        return
    
    # Kontrol scriptleri listesi
    scripts = [
        ("HIZLI_BACKEND_KONTROL.py", "Hızlı Backend Kontrol - Backend çalışıyor mu?"),
        ("SORUN_TESPIT_ADIM_ADIM.py", "Adım Adım Sorun Tespiti - Detaylı analiz"),
        ("SISTEM_KONTROL_KAPSAMLI.py", "Kapsamlı Sistem Kontrol - Full diagnostic")
    ]
    
    results = []
    
    print("🚀 Kontrol scriptleri sırayla çalıştırılıyor...")
    print("Her script'in sonucunu bekleyin...")
    
    for script_name, description in scripts:
        if os.path.exists(script_name):
            success = run_script(script_name, description)
            results.append((script_name, success))
            
            if not success:
                print(f"\n⚠️ {script_name} başarısız oldu")
                user_input = input("Devam etmek istiyor musunuz? (y/n): ")
                if user_input.lower() != 'y':
                    break
            
            time.sleep(2)  # Script'ler arası kısa bekleme
        else:
            print(f"❌ {script_name} bulunamadı!")
            results.append((script_name, False))
    
    # Sonuç özeti
    print("\n" + "=" * 60)
    print("📋 MASTER KONTROL SONUÇLARI")
    print("=" * 60)
    
    for script_name, success in results:
        status = "✅ BAŞARILI" if success else "❌ BAŞARISIZ"
        print(f"{status} - {script_name}")
    
    successful_scripts = sum(1 for _, success in results if success)
    total_scripts = len(results)
    
    print(f"\n📊 Özet: {successful_scripts}/{total_scripts} script başarılı")
    
    if successful_scripts == total_scripts:
        print("\n🎉 TÜM KONTROLLER BAŞARILI!")
        print("✅ AI sistemi tamamen çalışıyor")
        print("✅ Frontend'de brain ikonu (🧠) ile test edebilirsiniz")
    else:
        print(f"\n⚠️ {total_scripts - successful_scripts} script başarısız")
        print("🔧 Sorun giderme önerileri:")
        print("1. Backend'i başlatın: cd esref1-main/backend && python real_data_backend.py")
        print("2. Dependencies'leri yükleyin: pip install -r esref1-main/backend/requirements.txt")
        print("3. Başarısız script'leri tek tek çalıştırıp detayları inceleyin")
    
    # Ek araçlar önerisi
    print(f"\n🛠️ EK ARAÇLAR:")
    print("• AI_FRONTEND_TEST.html - Tarayıcı tabanlı test")
    print("• AI_DEBUG_FULL.py - Detaylı debug analizi")
    print("• BACKEND_BASLAT_AI.bat - Backend başlatma")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️ Master kontrol kullanıcı tarafından durduruldu")
    except Exception as e:
        print(f"\n❌ Master kontrol hatası: {e}")
        import traceback
        traceback.print_exc()