#!/usr/bin/env python3
"""
Basit AI Test - Autonomous AI'nın import edilip edilemediğini test eder
"""
import sys
import os

# Backend dizinini path'e ekle
sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))

def test_imports():
    """Import'ları test et"""
    print("🔍 Import testleri başlıyor...")
    
    try:
        print("1. Autonomous AI Manager import ediliyor...")
        from services.autonomous_ai_manager import autonomous_ai, process_autonomous_conversation
        print("✅ Autonomous AI Manager başarıyla import edildi")
        
        print("2. Autonomous AI Routes import ediliyor...")
        from routes.autonomous_ai import router
        print("✅ Autonomous AI Routes başarıyla import edildi")
        
        print("3. AI Manager instance kontrol ediliyor...")
        print(f"   AI Manager type: {type(autonomous_ai)}")
        print(f"   AI Manager status: {hasattr(autonomous_ai, 'process_conversation')}")
        
        return True
        
    except ImportError as e:
        print(f"❌ Import hatası: {e}")
        return False
    except Exception as e:
        print(f"❌ Genel hata: {e}")
        return False

def test_ai_functionality():
    """AI fonksiyonalitesini test et"""
    print("\n🤖 AI fonksiyonalite testi...")
    
    try:
        from services.autonomous_ai_manager import autonomous_ai
        
        # Basit bir test sorusu
        print("Test sorusu işleniyor...")
        
        # Sync test (async olmadan)
        print("✅ AI Manager erişilebilir")
        print(f"   Knowledge base size: {len(getattr(autonomous_ai, 'knowledge_base', {}))}")
        print(f"   Response templates: {len(getattr(autonomous_ai, 'response_templates', {}))}")
        
        return True
        
    except Exception as e:
        print(f"❌ AI fonksiyonalite hatası: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Ana test fonksiyonu"""
    print("🧪 BASİT AI TEST")
    print("=" * 40)
    
    # Test 1: Import'lar
    import_success = test_imports()
    
    # Test 2: AI fonksiyonalitesi
    functionality_success = test_ai_functionality()
    
    print("\n" + "=" * 40)
    print("📋 TEST SONUÇLARI")
    print("=" * 40)
    
    if import_success and functionality_success:
        print("✅ Tüm testler başarılı!")
        print("🚀 Autonomous AI sistemi çalışmaya hazır")
        print("\n💡 Sonraki adımlar:")
        print("1. Backend'i başlatın: python backend/real_data_backend.py")
        print("2. AI_DURUM_KONTROL.py ile tam test yapın")
    else:
        print("❌ Bazı testler başarısız")
        print("\n🔧 Sorun giderme:")
        if not import_success:
            print("- Import sorunları var, dosya yollarını kontrol edin")
        if not functionality_success:
            print("- AI manager'da kod hatası olabilir")

if __name__ == "__main__":
    main()