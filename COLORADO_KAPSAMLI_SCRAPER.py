#!/usr/bin/env python3
"""
Colorado Kapsamlı Event & Venue Scraper
Colorado eyaleti genelinde etkinlik ve mekan verilerini toplar
"""
import asyncio
import aiohttp
import json
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Optional
import sys
import os
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin, quote
import uuid

# Backend modüllerini import et
sys.path.append('backend')
from backend.database import db
from backend.cache_manager import cache

# Logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class ColoradoKapsamliScraper:
    def __init__(self):
        # API Keys
        self.google_api_key = os.getenv('GOOGLE_PLACES_API_KEY')
        self.ticketmaster_key = os.getenv('TICKETMASTER_API_KEY')
        self.eventbrite_token = os.getenv('EVENTBRITE_TOKEN')
        self.edmtrain_key = os.getenv('EDMTRAIN_API_KEY')
        
        # Headers for web scraping
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
        }
        
        # Colorado şehirleri ve koordinatları
        self.colorado_cities = {
            # Front Range (Ana Nüfus Merkezi)
            "Denver": {"lat": 39.7392, "lng": -104.9903, "population": 715522, "priority": 1},
            "Colorado Springs": {"lat": 38.8339, "lng": -104.8214, "population": 478961, "priority": 1},
            "Aurora": {"lat": 39.7294, "lng": -104.8319, "population": 386261, "priority": 1},
            "Fort Collins": {"lat": 40.5853, "lng": -105.0844, "population": 169810, "priority": 1},
            "Lakewood": {"lat": 39.7047, "lng": -105.0814, "population": 155984, "priority": 1},
            "Thornton": {"lat": 39.8681, "lng": -104.9719, "population": 141867, "priority": 1},
            "Arvada": {"lat": 39.8028, "lng": -105.0875, "population": 124402, "priority": 1},
            "Westminster": {"lat": 39.8367, "lng": -105.0372, "population": 116317, "priority": 1},
            "Pueblo": {"lat": 38.2544, "lng": -104.6091, "population": 111876, "priority": 2},
            "Centennial": {"lat": 39.5794, "lng": -104.8769, "population": 108418, "priority": 2},
            "Boulder": {"lat": 40.0150, "lng": -105.2705, "population": 108090, "priority": 1},
            "Greeley": {"lat": 40.4233, "lng": -104.7092, "population": 108795, "priority": 2},
            "Longmont": {"lat": 40.1672, "lng": -105.1019, "population": 98885, "priority": 2},
            "Loveland": {"lat": 40.3978, "lng": -105.0750, "population": 76378, "priority": 2},
            "Grand Junction": {"lat": 39.0639, "lng": -108.5506, "population": 65560, "priority": 2},
            "Broomfield": {"lat": 39.9205, "lng": -105.0867, "population": 74112, "priority": 2},
            "Castle Rock": {"lat": 39.3722, "lng": -104.8561, "population": 73158, "priority": 2},
            "Commerce City": {"lat": 39.8083, "lng": -104.9342, "population": 62418, "priority": 3},
            "Parker": {"lat": 39.5186, "lng": -104.7614, "population": 58512, "priority": 2},
            "Littleton": {"lat": 39.6133, "lng": -105.0167, "population": 46729, "priority": 2},
            "Northglenn": {"lat": 39.8961, "lng": -104.9811, "population": 38879, "priority": 3},
            "Englewood": {"lat": 39.6478, "lng": -104.9878, "population": 33659, "priority": 3},
            "Wheat Ridge": {"lat": 39.7661, "lng": -105.0772, "population": 31889, "priority": 3},
            "Golden": {"lat": 39.7555, "lng": -105.2211, "population": 21254, "priority": 2},
            
            # Dağ Kasabaları (Turizm Merkezleri)
            "Aspen": {"lat": 39.1911, "lng": -106.8175, "population": 7431, "priority": 1},
            "Vail": {"lat": 39.6403, "lng": -106.3742, "population": 5584, "priority": 1},
            "Breckenridge": {"lat": 39.4817, "lng": -106.0384, "population": 5078, "priority": 1},
            "Steamboat Springs": {"lat": 40.4850, "lng": -106.8317, "population": 13224, "priority": 1},
            "Telluride": {"lat": 37.9375, "lng": -107.8123, "population": 2607, "priority": 2},
            "Winter Park": {"lat": 39.8917, "lng": -105.7631, "population": 708, "priority": 2},
            "Keystone": {"lat": 39.6042, "lng": -105.9347, "population": 1079, "priority": 3},
            "Copper Mountain": {"lat": 39.5022, "lng": -106.1506, "population": 387, "priority": 3},
            "Crested Butte": {"lat": 38.8697, "lng": -106.9878, "population": 1639, "priority": 2},
            "Durango": {"lat": 37.2753, "lng": -107.8801, "population": 19071, "priority": 2},
            "Estes Park": {"lat": 40.3772, "lng": -105.5217, "population": 6467, "priority": 2},
            
            # Diğer Önemli Şehirler
            "Fort Morgan": {"lat": 40.2536, "lng": -103.7991, "population": 11570, "priority": 3},
            "Sterling": {"lat": 40.6256, "lng": -103.2077, "population": 14421, "priority": 3},
            "Montrose": {"lat": 38.4783, "lng": -107.8762, "population": 20291, "priority": 3},
            "Grand Lake": {"lat": 40.2517, "lng": -105.8231, "population": 471, "priority": 3},
            "Manitou Springs": {"lat": 38.8581, "lng": -104.9192, "population": 5341, "priority": 2},
        }
        
        # Event kaynakları
        self.event_sources = [
            "ticketmaster",
            "eventbrite", 
            "edmtrain",
            "denver_gov",
            "colorado_tourism",
            "local_venues",
            "facebook_events",
            "meetup"
        ]
        
        # Venue tipleri
        self.venue_types = [
            "night_club", "bar", "restaurant", "cafe", "music_venue",
            "dance_club", "lounge", "brewery", "winery", "casino",
            "theater", "concert_hall", "sports_bar", "rooftop_bar",
            "comedy_club", "karaoke_bar", "pool_hall", "bowling_alley"
        ]
        
        self.session = None
        self.results = {
            "venues": {"added": 0, "updated": 0, "errors": 0},
            "events": {"added": 0, "updated": 0, "errors": 0},
            "cities_processed": 0,
            "sources_used": [],
            "processing_time": 0,
            "errors": []
        }
    
    async def __aenter__(self):
        self.session = aiohttp.ClientSession(headers=self.headers)
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()
    
    async def run_full_scraping(self, priority_filter: int = 3, test_mode: bool = False):
        """
        Colorado genelinde tam scraping işlemi
        priority_filter: 1=Sadece en önemli şehirler, 2=Orta+önemli, 3=Tümü
        test_mode: True ise sadece birkaç şehir test edilir
        """
        start_time = datetime.now()
        print("🏔️  COLORADO KAPSAMLI SCRAPER BAŞLADI")
        print("=" * 60)
        
        try:
            # Test mode için şehir listesini sınırla
            cities_to_process = self._filter_cities(priority_filter, test_mode)
            
            print(f"📍 İşlenecek şehir sayısı: {len(cities_to_process)}")
            print(f"🔧 Test modu: {'Açık' if test_mode else 'Kapalı'}")
            print(f"⭐ Öncelik filtresi: {priority_filter}")
            print()
            
            # 1. Venue scraping
            print("🏢 VENUE SCRAPING BAŞLADI")
            print("-" * 40)
            await self._scrape_all_venues(cities_to_process)
            
            # 2. Event scraping
            print("\n🎉 EVENT SCRAPING BAŞLADI")
            print("-" * 40)
            await self._scrape_all_events(cities_to_process)
            
            # 3. Data enrichment
            print("\n📊 DATA ENRICHMENT BAŞLADI")
            print("-" * 40)
            await self._enrich_data()
            
            # 4. Results
            self.results["processing_time"] = (datetime.now() - start_time).total_seconds()
            self.results["cities_processed"] = len(cities_to_process)
            
            await self._save_results()
            self._print_summary()
            
        except Exception as e:
            logger.error(f"Scraping hatası: {e}")
            self.results["errors"].append(f"Genel hata: {str(e)}")
        
        return self.results
    
    def _filter_cities(self, priority_filter: int, test_mode: bool) -> Dict:
        """Şehirleri filtrele"""
        filtered = {}
        
        for city, data in self.colorado_cities.items():
            if data["priority"] <= priority_filter:
                filtered[city] = data
        
        if test_mode:
            # Test için sadece 5 şehir
            test_cities = ["Denver", "Boulder", "Colorado Springs", "Aspen", "Fort Collins"]
            filtered = {k: v for k, v in filtered.items() if k in test_cities}
        
        return filtered
    
    async def _scrape_all_venues(self, cities: Dict):
        """Tüm şehirler için venue scraping"""
        for city_name, city_data in cities.items():
            print(f"  📍 {city_name} venue'ları işleniyor...")
            
            try:
                # Google Places API
                if self.google_api_key:
                    venues = await self._scrape_google_places(city_name, city_data)
                    await self._save_venues(venues, city_name, "google_places")
                
                # Yelp scraping (web)
                venues = await self._scrape_yelp_venues(city_name, city_data)
                await self._save_venues(venues, city_name, "yelp")
                
                # TripAdvisor scraping (web)
                venues = await self._scrape_tripadvisor_venues(city_name, city_data)
                await self._save_venues(venues, city_name, "tripadvisor")
                
                # Local directory scraping
                venues = await self._scrape_local_directories(city_name, city_data)
                await self._save_venues(venues, city_name, "local_directories")
                
                # Rate limiting
                await asyncio.sleep(1)
                
            except Exception as e:
                logger.error(f"{city_name} venue scraping hatası: {e}")
                self.results["venues"]["errors"] += 1
                self.results["errors"].append(f"{city_name} venues: {str(e)}")
    
    async def _scrape_google_places(self, city_name: str, city_data: Dict) -> List[Dict]:
        """Google Places API ile venue scraping"""
        venues = []
        
        if not self.google_api_key:
            return venues
        
        try:
            for venue_type in self.venue_types:
                url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
                params = {
                    "location": f"{city_data['lat']},{city_data['lng']}",
                    "radius": 10000,  # 10km
                    "type": venue_type,
                    "key": self.google_api_key
                }
                
                async with self.session.get(url, params=params) as response:
                    if response.status == 200:
                        data = await response.json()
                        
                        for place in data.get("results", []):
                            venue = {
                                "source": "google_places",
                                "place_id": place.get("place_id"),
                                "name": place.get("name"),
                                "address": place.get("vicinity"),
                                "city": city_name,
                                "state": "CO",
                                "lat": place.get("geometry", {}).get("location", {}).get("lat"),
                                "lng": place.get("geometry", {}).get("location", {}).get("lng"),
                                "rating": place.get("rating"),
                                "user_ratings_total": place.get("user_ratings_total"),
                                "price_level": place.get("price_level"),
                                "types": place.get("types", []),
                                "venue_type": venue_type,
                                "photo_reference": place.get("photos", [{}])[0].get("photo_reference") if place.get("photos") else None,
                                "business_status": place.get("business_status"),
                                "scraped_at": datetime.now().isoformat()
                            }
                            venues.append(venue)
                
                # Rate limiting
                await asyncio.sleep(0.2)
                
        except Exception as e:
            logger.error(f"Google Places API hatası ({city_name}): {e}")
        
        return venues
    
    async def _scrape_yelp_venues(self, city_name: str, city_data: Dict) -> List[Dict]:
        """Yelp web scraping"""
        venues = []
        
        try:
            # Yelp search URL
            search_terms = ["bars", "nightlife", "restaurants", "clubs", "breweries"]
            
            for term in search_terms:
                url = f"https://www.yelp.com/search"
                params = {
                    "find_desc": term,
                    "find_loc": f"{city_name}, CO",
                    "start": 0
                }
                
                async with self.session.get(url, params=params) as response:
                    if response.status == 200:
                        html = await response.text()
                        soup = BeautifulSoup(html, 'html.parser')
                        
                        # Yelp business cards
                        business_cards = soup.find_all('div', {'data-testid': 'serp-ia-card'})
                        
                        for card in business_cards:
                            try:
                                name_elem = card.find('a', class_=re.compile(r'businessname'))
                                if not name_elem:
                                    name_elem = card.find('h3')
                                
                                if name_elem:
                                    venue = {
                                        "source": "yelp",
                                        "name": name_elem.get_text(strip=True),
                                        "city": city_name,
                                        "state": "CO",
                                        "category": term,
                                        "scraped_at": datetime.now().isoformat()
                                    }
                                    
                                    # Rating
                                    rating_elem = card.find('div', {'aria-label': re.compile(r'star rating')})
                                    if rating_elem:
                                        rating_text = rating_elem.get('aria-label', '')
                                        rating_match = re.search(r'(\d+\.?\d*)', rating_text)
                                        if rating_match:
                                            venue["rating"] = float(rating_match.group(1))
                                    
                                    # Address
                                    address_elem = card.find('p', string=re.compile(r'\d+.*'))
                                    if address_elem:
                                        venue["address"] = address_elem.get_text(strip=True)
                                    
                                    venues.append(venue)
                            except Exception as e:
                                logger.debug(f"Yelp card parsing hatası: {e}")
                
                # Rate limiting
                await asyncio.sleep(2)
                
        except Exception as e:
            logger.error(f"Yelp scraping hatası ({city_name}): {e}")
        
        return venues
    
    async def _scrape_tripadvisor_venues(self, city_name: str, city_data: Dict) -> List[Dict]:
        """TripAdvisor web scraping"""
        venues = []
        
        try:
            # TripAdvisor nightlife search
            city_slug = city_name.lower().replace(' ', '_')
            url = f"https://www.tripadvisor.com/Attractions-g{city_slug}-Activities-c20-Colorado.html"
            
            async with self.session.get(url) as response:
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    
                    # TripAdvisor attraction cards
                    attraction_cards = soup.find_all('div', class_=re.compile(r'attraction'))
                    
                    for card in attraction_cards:
                        try:
                            name_elem = card.find('h3') or card.find('h2')
                            if name_elem:
                                venue = {
                                    "source": "tripadvisor",
                                    "name": name_elem.get_text(strip=True),
                                    "city": city_name,
                                    "state": "CO",
                                    "category": "attraction",
                                    "scraped_at": datetime.now().isoformat()
                                }
                                venues.append(venue)
                        except Exception as e:
                            logger.debug(f"TripAdvisor card parsing hatası: {e}")
                            
        except Exception as e:
            logger.error(f"TripAdvisor scraping hatası ({city_name}): {e}")
        
        return venues
    
    async def _scrape_local_directories(self, city_name: str, city_data: Dict) -> List[Dict]:
        """Yerel dizinlerden venue scraping"""
        venues = []
        
        try:
            # Colorado.gov events and venues
            if city_name.lower() in ["denver", "boulder", "colorado springs"]:
                venues.extend(await self._scrape_colorado_gov(city_name))
            
            # Visit Colorado
            venues.extend(await self._scrape_visit_colorado(city_name))
            
            # Local chamber of commerce
            venues.extend(await self._scrape_chamber_commerce(city_name))
            
        except Exception as e:
            logger.error(f"Local directories scraping hatası ({city_name}): {e}")
        
        return venues
    
    async def _scrape_colorado_gov(self, city_name: str) -> List[Dict]:
        """Colorado.gov'dan venue bilgileri"""
        venues = []
        
        try:
            url = "https://www.colorado.gov/pacific/dola/local-government-directory"
            
            async with self.session.get(url) as response:
                if response.status == 200:
                    html = await response.text()
                    # Colorado.gov parsing logic burada olacak
                    
        except Exception as e:
            logger.debug(f"Colorado.gov scraping hatası: {e}")
        
        return venues
    
    async def _scrape_visit_colorado(self, city_name: str) -> List[Dict]:
        """Visit Colorado'dan venue bilgileri"""
        venues = []
        
        try:
            url = f"https://www.colorado.com/cities/{city_name.lower().replace(' ', '-')}"
            
            async with self.session.get(url) as response:
                if response.status == 200:
                    html = await response.text()
                    # Visit Colorado parsing logic burada olacak
                    
        except Exception as e:
            logger.debug(f"Visit Colorado scraping hatası: {e}")
        
        return venues
    
    async def _scrape_chamber_commerce(self, city_name: str) -> List[Dict]:
        """Ticaret odalarından venue bilgileri"""
        venues = []
        
        # Her şehrin ticaret odası farklı olduğu için genel bir yaklaşım
        chamber_urls = {
            "Denver": "https://www.denverchamber.org",
            "Boulder": "https://boulderchamber.com",
            "Colorado Springs": "https://coloradospringschamberedc.com"
        }
        
        if city_name in chamber_urls:
            try:
                url = chamber_urls[city_name]
                async with self.session.get(url) as response:
                    if response.status == 200:
                        html = await response.text()
                        # Chamber parsing logic burada olacak
                        
            except Exception as e:
                logger.debug(f"Chamber scraping hatası ({city_name}): {e}")
        
        return venues
    
    async def _save_venues(self, venues: List[Dict], city_name: str, source: str):
        """Venue'ları veritabanına kaydet"""
        if not venues:
            return
        
        try:
            for venue_data in venues:
                # Unique identifier oluştur
                unique_key = f"{venue_data.get('name', '')}-{city_name}-{source}"
                venue_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, unique_key))
                
                # Mevcut venue kontrolü
                existing = await db.venues.find_one({"id": venue_id})
                
                if existing:
                    # Update existing
                    await db.venues.update_one(
                        {"id": venue_id},
                        {"$set": {
                            "updated_at": datetime.now().isoformat(),
                            "last_scraped": datetime.now().isoformat(),
                            **venue_data
                        }}
                    )
                    self.results["venues"]["updated"] += 1
                else:
                    # Insert new
                    venue_doc = {
                        "id": venue_id,
                        "created_at": datetime.now().isoformat(),
                        "updated_at": datetime.now().isoformat(),
                        "last_scraped": datetime.now().isoformat(),
                        "current_busyness": 0,
                        "busyness_label": "Unknown",
                        "report_count": 0,
                        "is_active": True,
                        **venue_data
                    }
                    
                    await db.venues.insert_one(venue_doc)
                    self.results["venues"]["added"] += 1
                    
        except Exception as e:
            logger.error(f"Venue kaydetme hatası ({city_name}, {source}): {e}")
            self.results["venues"]["errors"] += 1
    
    async def _scrape_all_events(self, cities: Dict):
        """Tüm şehirler için event scraping"""
        for city_name, city_data in cities.items():
            print(f"  🎉 {city_name} etkinlikleri işleniyor...")
            
            try:
                # Ticketmaster API
                if self.ticketmaster_key:
                    events = await self._scrape_ticketmaster_events(city_name)
                    await self._save_events(events, city_name, "ticketmaster")
                
                # Eventbrite API
                if self.eventbrite_token:
                    events = await self._scrape_eventbrite_events(city_name, city_data)
                    await self._save_events(events, city_name, "eventbrite")
                
                # EDMTrain API
                if self.edmtrain_key and city_name.lower() in ["denver", "boulder"]:
                    events = await self._scrape_edmtrain_events(city_name)
                    await self._save_events(events, city_name, "edmtrain")
                
                # Facebook Events (web scraping)
                events = await self._scrape_facebook_events(city_name)
                await self._save_events(events, city_name, "facebook")
                
                # Meetup Events (web scraping)
                events = await self._scrape_meetup_events(city_name)
                await self._save_events(events, city_name, "meetup")
                
                # Local event websites
                events = await self._scrape_local_events(city_name)
                await self._save_events(events, city_name, "local")
                
                # Rate limiting
                await asyncio.sleep(1)
                
            except Exception as e:
                logger.error(f"{city_name} event scraping hatası: {e}")
                self.results["events"]["errors"] += 1
                self.results["errors"].append(f"{city_name} events: {str(e)}")
    
    async def _scrape_ticketmaster_events(self, city_name: str) -> List[Dict]:
        """Ticketmaster API ile event scraping"""
        events = []
        
        if not self.ticketmaster_key:
            return events
        
        try:
            url = "https://app.ticketmaster.com/discovery/v2/events.json"
            params = {
                "apikey": self.ticketmaster_key,
                "city": city_name,
                "stateCode": "CO",
                "size": 100,
                "sort": "date,asc"
            }
            
            async with self.session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    for event in data.get("_embedded", {}).get("events", []):
                        venue_info = event.get("_embedded", {}).get("venues", [{}])[0]
                        
                        event_data = {
                            "source": "ticketmaster",
                            "external_id": event.get("id"),
                            "name": event.get("name"),
                            "description": event.get("info", ""),
                            "url": event.get("url"),
                            "start_date": event.get("dates", {}).get("start", {}).get("localDate"),
                            "start_time": event.get("dates", {}).get("start", {}).get("localTime"),
                            "venue_name": venue_info.get("name"),
                            "venue_address": venue_info.get("address", {}).get("line1"),
                            "city": city_name,
                            "state": "CO",
                            "category": event.get("classifications", [{}])[0].get("segment", {}).get("name", "events"),
                            "genre": event.get("classifications", [{}])[0].get("genre", {}).get("name"),
                            "image_url": event.get("images", [{}])[0].get("url") if event.get("images") else None,
                            "price_min": event.get("priceRanges", [{}])[0].get("min") if event.get("priceRanges") else None,
                            "price_max": event.get("priceRanges", [{}])[0].get("max") if event.get("priceRanges") else None,
                            "scraped_at": datetime.now().isoformat()
                        }
                        events.append(event_data)
                        
        except Exception as e:
            logger.error(f"Ticketmaster API hatası ({city_name}): {e}")
        
        return events
    
    async def _scrape_eventbrite_events(self, city_name: str, city_data: Dict) -> List[Dict]:
        """Eventbrite API ile event scraping"""
        events = []
        
        if not self.eventbrite_token:
            return events
        
        try:
            url = "https://www.eventbriteapi.com/v3/events/search/"
            headers = {"Authorization": f"Bearer {self.eventbrite_token}"}
            params = {
                "location.address": f"{city_name}, CO",
                "location.within": "25km",
                "expand": "venue,organizer",
                "sort_by": "date"
            }
            
            async with self.session.get(url, headers=headers, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    for event in data.get("events", []):
                        venue = event.get("venue", {})
                        
                        event_data = {
                            "source": "eventbrite",
                            "external_id": event.get("id"),
                            "name": event.get("name", {}).get("text"),
                            "description": event.get("description", {}).get("text", ""),
                            "url": event.get("url"),
                            "start_date": event.get("start", {}).get("local", "").split("T")[0],
                            "start_time": event.get("start", {}).get("local", "").split("T")[1] if "T" in event.get("start", {}).get("local", "") else None,
                            "venue_name": venue.get("name"),
                            "venue_address": venue.get("address", {}).get("localized_address_display"),
                            "city": city_name,
                            "state": "CO",
                            "category": event.get("category", {}).get("name", "events"),
                            "is_free": event.get("is_free", False),
                            "image_url": event.get("logo", {}).get("url") if event.get("logo") else None,
                            "scraped_at": datetime.now().isoformat()
                        }
                        events.append(event_data)
                        
        except Exception as e:
            logger.error(f"Eventbrite API hatası ({city_name}): {e}")
        
        return events
    
    async def _scrape_edmtrain_events(self, city_name: str) -> List[Dict]:
        """EDMTrain API ile event scraping"""
        events = []
        
        if not self.edmtrain_key:
            return events
        
        try:
            url = "https://edmtrain.com/api/events"
            params = {
                "client": self.edmtrain_key,
                "city": city_name,
                "state": "Colorado"
            }
            
            async with self.session.get(url, params=params) as response:
                if response.status == 200:
                    data = await response.json()
                    
                    for event in data.get("data", []):
                        event_data = {
                            "source": "edmtrain",
                            "external_id": str(event.get("id")),
                            "name": event.get("name"),
                            "url": event.get("link"),
                            "start_date": event.get("date"),
                            "venue_name": event.get("venue", {}).get("name"),
                            "venue_address": event.get("venue", {}).get("address"),
                            "city": city_name,
                            "state": "CO",
                            "category": "EDM",
                            "genre": "Electronic",
                            "image_url": event.get("imageUrl"),
                            "scraped_at": datetime.now().isoformat()
                        }
                        events.append(event_data)
                        
        except Exception as e:
            logger.error(f"EDMTrain API hatası ({city_name}): {e}")
        
        return events
    
    async def _scrape_facebook_events(self, city_name: str) -> List[Dict]:
        """Facebook Events web scraping"""
        events = []
        
        try:
            # Facebook events search (public events only)
            search_url = f"https://www.facebook.com/events/search/?q={quote(city_name + ' Colorado events')}"
            
            async with self.session.get(search_url) as response:
                if response.status == 200:
                    html = await response.text()
                    # Facebook parsing logic burada olacak
                    # Not: Facebook'un anti-scraping önlemleri nedeniyle sınırlı
                    
        except Exception as e:
            logger.debug(f"Facebook scraping hatası ({city_name}): {e}")
        
        return events
    
    async def _scrape_meetup_events(self, city_name: str) -> List[Dict]:
        """Meetup Events web scraping"""
        events = []
        
        try:
            # Meetup events search
            search_url = f"https://www.meetup.com/find/events/?allMeetups=false&keywords=&radius=25&userFreeform={quote(city_name + ', CO')}"
            
            async with self.session.get(search_url) as response:
                if response.status == 200:
                    html = await response.text()
                    # Meetup parsing logic burada olacak
                    
        except Exception as e:
            logger.debug(f"Meetup scraping hatası ({city_name}): {e}")
        
        return events
    
    async def _scrape_local_events(self, city_name: str) -> List[Dict]:
        """Yerel event websitelerinden scraping"""
        events = []
        
        # Şehir bazlı yerel event kaynakları
        local_sources = {
            "Denver": [
                "https://www.denver.org/events/",
                "https://www.westword.com/events",
                "https://303magazine.com/events"
            ],
            "Boulder": [
                "https://www.bouldercoloradousa.com/events/",
                "https://www.dailycamera.com/events/"
            ],
            "Colorado Springs": [
                "https://www.visitcos.com/events/",
                "https://www.coloradospringsindependent.com/events/"
            ],
            "Aspen": [
                "https://www.aspenchamber.org/events/",
                "https://www.aspensnowmass.com/events"
            ]
        }
        
        if city_name in local_sources:
            for url in local_sources[city_name]:
                try:
                    async with self.session.get(url) as response:
                        if response.status == 200:
                            html = await response.text()
                            # Local event parsing logic burada olacak
                            
                except Exception as e:
                    logger.debug(f"Local event scraping hatası ({url}): {e}")
        
        return events
    
    async def _save_events(self, events: List[Dict], city_name: str, source: str):
        """Event'leri veritabanına kaydet"""
        if not events:
            return
        
        try:
            for event_data in events:
                # Unique identifier oluştur
                unique_key = f"{event_data.get('external_id', '')}-{event_data.get('name', '')}-{source}"
                event_id = str(uuid.uuid5(uuid.NAMESPACE_DNS, unique_key))
                
                # Mevcut event kontrolü
                existing = await db.events.find_one({"id": event_id})
                
                if existing:
                    # Update existing
                    await db.events.update_one(
                        {"id": event_id},
                        {"$set": {
                            "updated_at": datetime.now().isoformat(),
                            "last_scraped": datetime.now().isoformat(),
                            **event_data
                        }}
                    )
                    self.results["events"]["updated"] += 1
                else:
                    # Insert new
                    event_doc = {
                        "id": event_id,
                        "created_at": datetime.now().isoformat(),
                        "updated_at": datetime.now().isoformat(),
                        "last_scraped": datetime.now().isoformat(),
                        "is_active": True,
                        **event_data
                    }
                    
                    await db.events.insert_one(event_doc)
                    self.results["events"]["added"] += 1
                    
        except Exception as e:
            logger.error(f"Event kaydetme hatası ({city_name}, {source}): {e}")
            self.results["events"]["errors"] += 1
    
    async def _enrich_data(self):
        """Veri zenginleştirme işlemleri"""
        print("  📊 Venue popularity skorları hesaplanıyor...")
        await self._calculate_venue_scores()
        
        print("  🔗 Event-venue eşleştirmeleri yapılıyor...")
        await self._match_events_to_venues()
        
        print("  📍 Koordinat bilgileri tamamlanıyor...")
        await self._geocode_missing_locations()
        
        print("  🏷️  Kategori normalizasyonu yapılıyor...")
        await self._normalize_categories()
    
    async def _calculate_venue_scores(self):
        """Venue popularity skorlarını hesapla"""
        try:
            venues = await db.venues.find({}, {"_id": 0, "id": 1}).to_list(10000)
            
            for venue in venues:
                venue_id = venue["id"]
                
                # Skor hesaplama
                report_count = await db.busyness_reports.count_documents({"venue_id": venue_id})
                comment_count = await db.comments.count_documents({"venue_id": venue_id})
                
                score = (report_count * 3) + (comment_count * 2)
                
                await db.venues.update_one(
                    {"id": venue_id},
                    {"$set": {"popularity_score": score}}
                )
                
        except Exception as e:
            logger.error(f"Venue score hesaplama hatası: {e}")
    
    async def _match_events_to_venues(self):
        """Event'leri venue'larla eşleştir"""
        try:
            events = await db.events.find({"venue_id": {"$exists": False}}).to_list(1000)
            
            for event in events:
                venue_name = event.get("venue_name", "").lower()
                city = event.get("city", "")
                
                if venue_name and city:
                    # Venue arama
                    venue = await db.venues.find_one({
                        "name": {"$regex": venue_name, "$options": "i"},
                        "city": city
                    })
                    
                    if venue:
                        await db.events.update_one(
                            {"id": event["id"]},
                            {"$set": {"venue_id": venue["id"]}}
                        )
                        
        except Exception as e:
            logger.error(f"Event-venue eşleştirme hatası: {e}")
    
    async def _geocode_missing_locations(self):
        """Eksik koordinat bilgilerini tamamla"""
        try:
            if not self.google_api_key:
                return
            
            venues = await db.venues.find({
                "$or": [
                    {"lat": {"$exists": False}},
                    {"lng": {"$exists": False}},
                    {"lat": None},
                    {"lng": None}
                ]
            }).to_list(100)
            
            for venue in venues:
                address = f"{venue.get('address', '')}, {venue.get('city', '')}, CO"
                
                url = "https://maps.googleapis.com/maps/api/geocode/json"
                params = {
                    "address": address,
                    "key": self.google_api_key
                }
                
                async with self.session.get(url, params=params) as response:
                    if response.status == 200:
                        data = await response.json()
                        
                        if data.get("results"):
                            location = data["results"][0]["geometry"]["location"]
                            
                            await db.venues.update_one(
                                {"id": venue["id"]},
                                {"$set": {
                                    "lat": location["lat"],
                                    "lng": location["lng"]
                                }}
                            )
                
                # Rate limiting
                await asyncio.sleep(0.1)
                
        except Exception as e:
            logger.error(f"Geocoding hatası: {e}")
    
    async def _normalize_categories(self):
        """Kategori normalizasyonu"""
        try:
            # Venue kategorileri
            venue_category_mapping = {
                "night_club": "nightclub",
                "dance_club": "nightclub", 
                "music_venue": "music",
                "sports_bar": "bar",
                "rooftop_bar": "bar"
            }
            
            for old_cat, new_cat in venue_category_mapping.items():
                await db.venues.update_many(
                    {"venue_type": old_cat},
                    {"$set": {"category": new_cat}}
                )
            
            # Event kategorileri
            event_category_mapping = {
                "Music": "music",
                "Sports": "sports",
                "Arts & Theatre": "arts",
                "Film": "entertainment"
            }
            
            for old_cat, new_cat in event_category_mapping.items():
                await db.events.update_many(
                    {"category": old_cat},
                    {"$set": {"category": new_cat}}
                )
                
        except Exception as e:
            logger.error(f"Kategori normalizasyon hatası: {e}")
    
    async def _save_results(self):
        """Sonuçları dosyaya kaydet"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"colorado_scraping_results_{timestamp}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.results, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 Sonuçlar kaydedildi: {filename}")
    
    def _print_summary(self):
        """Özet raporu yazdır"""
        print("\n" + "=" * 60)
        print("📊 COLORADO SCRAPING ÖZET RAPORU")
        print("=" * 60)
        
        print(f"⏱️  İşlem süresi: {self.results['processing_time']:.1f} saniye")
        print(f"📍 İşlenen şehir: {self.results['cities_processed']}")
        print()
        
        print("🏢 VENUE SONUÇLARI:")
        print(f"   ✅ Eklenen: {self.results['venues']['added']}")
        print(f"   🔄 Güncellenen: {self.results['venues']['updated']}")
        print(f"   ❌ Hata: {self.results['venues']['errors']}")
        print()
        
        print("🎉 EVENT SONUÇLARI:")
        print(f"   ✅ Eklenen: {self.results['events']['added']}")
        print(f"   🔄 Güncellenen: {self.results['events']['updated']}")
        print(f"   ❌ Hata: {self.results['events']['errors']}")
        print()
        
        if self.results['errors']:
            print("⚠️  HATALAR:")
            for error in self.results['errors'][:5]:  # İlk 5 hatayı göster
                print(f"   • {error}")
            if len(self.results['errors']) > 5:
                print(f"   ... ve {len(self.results['errors']) - 5} hata daha")
        
        print("\n✅ Colorado scraping tamamlandı!")

async def main():
    """Ana fonksiyon"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Colorado Kapsamlı Scraper')
    parser.add_argument('--priority', type=int, default=2, choices=[1, 2, 3],
                       help='Öncelik filtresi (1=En önemli, 2=Orta+önemli, 3=Tümü)')
    parser.add_argument('--test', action='store_true',
                       help='Test modu (sadece birkaç şehir)')
    parser.add_argument('--venues-only', action='store_true',
                       help='Sadece venue scraping')
    parser.add_argument('--events-only', action='store_true',
                       help='Sadece event scraping')
    
    args = parser.parse_args()
    
    async with ColoradoKapsamliScraper() as scraper:
        if args.venues_only:
            print("🏢 Sadece venue scraping modu")
            # Venue-only logic burada olacak
        elif args.events_only:
            print("🎉 Sadece event scraping modu")
            # Event-only logic burada olacak
        else:
            # Full scraping
            results = await scraper.run_full_scraping(
                priority_filter=args.priority,
                test_mode=args.test
            )
            
            return results

if __name__ == "__main__":
    try:
        results = asyncio.run(main())
        print(f"\n🎉 Scraping başarıyla tamamlandı!")
        
    except KeyboardInterrupt:
        print(f"\n⚠️  Scraping kullanıcı tarafından durduruldu")
    except Exception as e:
        print(f"\n❌ Scraping hatası: {e}")
        import traceback
        traceback.print_exc()