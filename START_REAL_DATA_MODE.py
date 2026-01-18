"""
Start Real Data Mode
Master script to switch from mock data to real data
"""
import asyncio
import subprocess
import sys
import os
import time
from datetime import datetime
import json

def print_header(title: str):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(f"🚀 {title}")
    print("=" * 60)

def print_step(step: int, title: str):
    """Print a step header"""
    print(f"\n📋 STEP {step}: {title}")
    print("-" * 40)

async def check_requirements():
    """Check if all requirements are met"""
    print_step(1, "CHECKING REQUIREMENTS")
    
    requirements = {
        'python': True,
        'mongodb': False,
        'env_file': False,
        'google_api_key': False
    }
    
    # Check Python
    try:
        python_version = sys.version
        print(f"✅ Python: {python_version.split()[0]}")
        requirements['python'] = True
    except:
        print("❌ Python not found")
        requirements['python'] = False
    
    # Check .env file
    env_path = os.path.join('backend', '.env')
    if os.path.exists(env_path):
        print("✅ Backend .env file exists")
        requirements['env_file'] = True
        
        # Check for Google API key
        try:
            with open(env_path, 'r') as f:
                env_content = f.read()
                if 'GOOGLE_PLACES_API_KEY' in env_content and len(env_content.split('GOOGLE_PLACES_API_KEY=')[1].split('\n')[0].strip()) > 10:
                    print("✅ Google Places API key configured")
                    requirements['google_api_key'] = True
                else:
                    print("⚠️ Google Places API key missing or invalid")
        except:
            print("⚠️ Could not read .env file")
    else:
        print("❌ Backend .env file not found")
    
    # Check MongoDB (try to connect)
    try:
        # Add backend to path
        sys.path.append(os.path.join(os.path.dirname(__file__), 'backend'))
        from backend.database import db
        
        # Test connection
        venue_count = await db.venues.count_documents({})
        print(f"✅ MongoDB connected - {venue_count} venues in database")
        requirements['mongodb'] = True
        
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
        requirements['mongodb'] = False
    
    # Summary
    passed = sum(requirements.values())
    total = len(requirements)
    
    print(f"\n📊 Requirements Check: {passed}/{total} passed")
    
    if passed < total:
        print("\n⚠️ REQUIREMENTS NOT MET:")
        if not requirements['mongodb']:
            print("   • Start MongoDB server")
            print("   • Check MONGO_URL in backend/.env")
        if not requirements['env_file']:
            print("   • Create backend/.env file")
        if not requirements['google_api_key']:
            print("   • Add GOOGLE_PLACES_API_KEY to backend/.env")
        
        return False
    
    print("✅ All requirements met!")
    return True

async def populate_database():
    """Populate database with real data"""
    print_step(2, "POPULATING DATABASE WITH REAL DATA")
    
    try:
        # Run population script
        print("🔄 Running data population script...")
        
        # Import and run population
        sys.path.append(os.path.dirname(__file__))
        from POPULATE_REAL_DATA import main as populate_main
        
        await populate_main()
        
        print("✅ Database population completed")
        return True
        
    except Exception as e:
        print(f"❌ Database population failed: {e}")
        return False

def start_real_data_backend():
    """Start the real data backend server"""
    print_step(3, "STARTING REAL DATA BACKEND")
    
    try:
        print("🚀 Starting real data backend on port 8003...")
        print("💡 This will replace the mock data backend")
        print("🔄 Backend will serve real data from MongoDB and scrapers")
        
        # Change to backend directory
        backend_path = os.path.join(os.path.dirname(__file__), 'backend')
        
        # Start the real data backend
        print("\n📍 Backend will be available at: http://localhost:8003")
        print("📚 API Documentation: http://localhost:8003/docs")
        print("\n🔄 Starting server...")
        
        # Run the backend
        os.chdir(backend_path)
        subprocess.run([sys.executable, 'real_data_backend.py'])
        
    except KeyboardInterrupt:
        print("\n⏹️ Backend stopped by user")
    except Exception as e:
        print(f"❌ Failed to start backend: {e}")

def update_frontend_config():
    """Update frontend to use real data backend"""
    print_step(4, "UPDATING FRONTEND CONFIGURATION")
    
    try:
        frontend_env_path = os.path.join('frontend', '.env')
        
        # Update .env file
        with open(frontend_env_path, 'w') as f:
            f.write("REACT_APP_BACKEND_URL=http://localhost:8003\n")
        
        print("✅ Frontend configured to use real data backend (port 8003)")
        print("💡 Restart frontend to apply changes: npm start")
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to update frontend config: {e}")
        return False

async def run_integration_test():
    """Run integration test to verify everything works"""
    print_step(5, "RUNNING INTEGRATION TEST")
    
    try:
        print("🧪 Testing real data integration...")
        
        # Import and run test
        from TEST_REAL_DATA_INTEGRATION import compare_backends
        
        results = await compare_backends()
        
        real_backend = results['real_backend']
        success_rate = (real_backend['total_score'] / real_backend['max_score']) * 100
        
        if success_rate >= 80:
            print("✅ Integration test passed!")
            return True
        else:
            print("⚠️ Integration test found issues")
            return False
            
    except Exception as e:
        print(f"❌ Integration test failed: {e}")
        return False

def create_startup_scripts():
    """Create convenient startup scripts"""
    print_step(6, "CREATING STARTUP SCRIPTS")
    
    try:
        # Create Windows batch file
        batch_content = """@echo off
echo 🚀 Starting Real Data Mode
echo.
echo 📍 Backend: http://localhost:8003
echo 📍 Frontend: http://localhost:3000
echo.
echo Starting backend...
cd backend
python real_data_backend.py
"""
        
        with open('START_REAL_DATA_BACKEND.bat', 'w') as f:
            f.write(batch_content)
        
        # Create shell script
        shell_content = """#!/bin/bash
echo "🚀 Starting Real Data Mode"
echo ""
echo "📍 Backend: http://localhost:8003"
echo "📍 Frontend: http://localhost:3000"
echo ""
echo "Starting backend..."
cd backend
python real_data_backend.py
"""
        
        with open('start_real_data_backend.sh', 'w') as f:
            f.write(shell_content)
        
        # Make shell script executable
        try:
            os.chmod('start_real_data_backend.sh', 0o755)
        except:
            pass
        
        print("✅ Created startup scripts:")
        print("   • START_REAL_DATA_BACKEND.bat (Windows)")
        print("   • start_real_data_backend.sh (Linux/Mac)")
        
        return True
        
    except Exception as e:
        print(f"❌ Failed to create startup scripts: {e}")
        return False

async def main():
    """Main function to switch to real data mode"""
    print_header("REAL DATA MODE ACTIVATION")
    print(f"🕐 Started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    try:
        # Step 1: Check requirements
        if not await check_requirements():
            print("\n❌ ACTIVATION FAILED - Requirements not met")
            print("💡 Fix the issues above and try again")
            return
        
        # Step 2: Populate database
        if not await populate_database():
            print("\n❌ ACTIVATION FAILED - Database population failed")
            return
        
        # Step 3: Update frontend config
        if not update_frontend_config():
            print("\n❌ ACTIVATION FAILED - Frontend config update failed")
            return
        
        # Step 4: Create startup scripts
        if not create_startup_scripts():
            print("\n⚠️ WARNING - Startup scripts creation failed")
        
        # Step 5: Final summary
        print_header("REAL DATA MODE ACTIVATED SUCCESSFULLY!")
        
        print("🎉 CONGRATULATIONS!")
        print("✅ Mock data has been replaced with real data")
        print("✅ Database populated with real venues and events")
        print("✅ Frontend configured for real data backend")
        print("✅ Startup scripts created")
        
        print("\n🚀 NEXT STEPS:")
        print("1. Start the real data backend:")
        print("   python backend/real_data_backend.py")
        print("   OR double-click: START_REAL_DATA_BACKEND.bat")
        
        print("\n2. Start the frontend (in another terminal):")
        print("   cd frontend && npm start")
        
        print("\n3. Test the application:")
        print("   • Backend: http://localhost:8003")
        print("   • Frontend: http://localhost:3000")
        print("   • API Docs: http://localhost:8003/docs")
        
        print("\n📊 DATA SOURCES NOW ACTIVE:")
        print("   • Google Places API (1700+ venues)")
        print("   • Denver event scrapers")
        print("   • Eventbrite real data")
        print("   • Generated after parties")
        print("   • Real-time busyness simulation")
        
        print("\n💡 BENEFITS:")
        print("   ✅ Real venue data with authentic websites")
        print("   ✅ Dynamic event data from multiple sources")
        print("   ✅ Realistic after party generation")
        print("   ✅ Performance optimized with caching")
        print("   ✅ Scalable database architecture")
        
        # Ask if user wants to start backend now
        print("\n" + "=" * 60)
        response = input("🚀 Start real data backend now? (y/n): ").lower().strip()
        
        if response in ['y', 'yes']:
            print("\n🔄 Starting real data backend...")
            start_real_data_backend()
        else:
            print("\n✅ Real data mode ready!")
            print("💡 Start backend when ready: python backend/real_data_backend.py")
        
    except KeyboardInterrupt:
        print("\n⏹️ Activation cancelled by user")
    except Exception as e:
        print(f"\n❌ ACTIVATION FAILED: {e}")
        print("💡 Check the error above and try again")

if __name__ == "__main__":
    asyncio.run(main())