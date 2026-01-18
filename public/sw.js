// Service Worker for Push Notifications & Performance Caching
// Is it Busy? App

const CACHE_NAME = 'isitbusy-v2';
const API_CACHE_NAME = 'isitbusy-api-v1';
const API_CACHE_DURATION = 30 * 1000; // 30 seconds for API responses

// Static assets to cache
const STATIC_ASSETS = [
  '/',
  '/index.html',
  '/logo192.png'
];

// API endpoints to cache
const CACHEABLE_API_PATTERNS = [
  '/api/venues',
  '/api/news',
  '/api/events'
];

// Install event - cache static assets
self.addEventListener('install', function(event) {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then(function(cache) {
        console.log('[SW] Caching static assets');
        return cache.addAll(STATIC_ASSETS);
      })
      .then(() => self.skipWaiting())
  );
});

// Activate event - clean up old caches
self.addEventListener('activate', function(event) {
  event.waitUntil(
    caches.keys().then(function(cacheNames) {
      return Promise.all(
        cacheNames
          .filter(name => name !== CACHE_NAME && name !== API_CACHE_NAME)
          .map(name => caches.delete(name))
      );
    }).then(() => self.clients.claim())
  );
});

// Fetch event - smart caching strategy
self.addEventListener('fetch', function(event) {
  const url = new URL(event.request.url);
  
  // Check if this is an API request we should cache
  const isApiRequest = CACHEABLE_API_PATTERNS.some(pattern => 
    url.pathname.includes(pattern)
  );
  
  if (isApiRequest && event.request.method === 'GET') {
    // Stale-while-revalidate strategy for API requests
    event.respondWith(
      caches.open(API_CACHE_NAME).then(async function(cache) {
        const cachedResponse = await cache.match(event.request);
        
        // Fetch fresh data in background
        const fetchPromise = fetch(event.request).then(function(networkResponse) {
          if (networkResponse.ok) {
            // Clone and cache the response with timestamp
            const responseToCache = networkResponse.clone();
            cache.put(event.request, responseToCache);
          }
          return networkResponse;
        }).catch(() => cachedResponse); // Fallback to cache on network error
        
        // Return cached response immediately if available, otherwise wait for network
        return cachedResponse || fetchPromise;
      })
    );
  } else {
    // Default: cache-first for static assets
    event.respondWith(
      caches.match(event.request).then(function(response) {
        return response || fetch(event.request);
      })
    );
  }
});

// Push notification handlers
self.addEventListener('push', function(event) {
  console.log('[SW] Push Received.');
  
  let data = {};
  if (event.data) {
    try {
      data = event.data.json();
    } catch (e) {
      data = {
        title: 'Is it Busy?',
        body: event.data.text()
      };
    }
  }

  const title = data.title || 'Is it Busy?';
  const options = {
    body: data.body || 'You have a new notification',
    icon: '/logo192.png',
    badge: '/logo192.png',
    vibrate: [100, 50, 100],
    data: {
      dateOfArrival: Date.now(),
      url: data.url || '/'
    },
    actions: [
      { action: 'view', title: 'View' },
      { action: 'close', title: 'Close' }
    ]
  };

  event.waitUntil(
    self.registration.showNotification(title, options)
  );
});

self.addEventListener('notificationclick', function(event) {
  console.log('[SW] Notification click received.');
  
  event.notification.close();
  
  if (event.action === 'close') return;
  
  const url = event.notification.data?.url || '/';
  
  event.waitUntil(
    clients.matchAll({ type: 'window', includeUncontrolled: true })
      .then(function(clientList) {
        for (let client of clientList) {
          if (client.url.includes(self.location.origin) && 'focus' in client) {
            client.navigate(url);
            return client.focus();
          }
        }
        if (clients.openWindow) {
          return clients.openWindow(url);
        }
      })
  );
});

self.addEventListener('pushsubscriptionchange', function(event) {
  console.log('[SW] Push subscription changed.');
});
