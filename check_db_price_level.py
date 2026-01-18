#!/usr/bin/env python3
"""
Check what price_level data is actually in the database
"""
import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def check_database_price_levels():
    print("🔍 CHECKING DATABASE PRICE LEVEL DATA")
    print("=" * 60)
    
    try:
        # Connect to MongoDB
        client = AsyncIOMotorClient("mongodb://localhost:27017")
        db = client.esref
        
        # Get a few sample venues
        venues = await db.venues.find({}).limit(5).to_list(length=5)
        
        if not venues:
            print("❌ No venues found in database")
            return
        
        print(f"Found {len(venues)} sample venues:")
        print()
        
        for i, venue in enumerate(venues, 1):
            print(f"Venue {i}: {venue.get('name', 'Unknown')}")
            print(f"  ID: {venue.get('id', 'No ID')}")
            print(f"  Type: {venue.get('type', 'Unknown')}")
            print(f"  Price Level: '{venue.get('price_level')}' (type: {type(venue.get('price_level'))})")
            
            # Check if price_level exists in the document
            if 'price_level' in venue:
                print(f"  ✅ price_level field exists")
            else:
                print(f"  ❌ price_level field missing")
            
            print()
        
        # Count venues with and without price_level
        total_venues = await db.venues.count_documents({})
        venues_with_price = await db.venues.count_documents({"price_level": {"$exists": True, "$ne": None}})
        venues_without_price = total_venues - venues_with_price
        
        print(f"Database Summary:")
        print(f"  Total venues: {total_venues}")
        print(f"  With price_level: {venues_with_price}")
        print(f"  Without price_level: {venues_without_price}")
        
        if venues_without_price > 0:
            print(f"  ❌ {venues_without_price} venues missing price_level data")
        else:
            print(f"  ✅ All venues have price_level data")
            
    except Exception as e:
        print(f"❌ Database error: {e}")
    finally:
        client.close()

if __name__ == '__main__':
    asyncio.run(check_database_price_levels())