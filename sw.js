const CACHE = 'optik-zada-shell-v8.9.52';
const SHELL = ['/', '/index.html', '/assets/icons/icon-192.png', '/assets/icons/icon-512.png'];

// Install: cache app shell
self.addEventListener('install', e => {
  e.waitUntil(caches.open(CACHE).then(c => c.addAll(SHELL)));
  self.skipWaiting();
});

// Activate: purge old caches
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

// Fetch: cache-first for shell, network-first for Firebase API
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;

  const url = e.request.url;
  // Always go to network for Firebase, auth, external CDN
  if (
    url.includes('firestore.googleapis.com') ||
    url.includes('identitytoolkit') ||
    url.includes('securetoken') ||
    url.includes('firebaseio.com') ||
    url.includes('firebase.googleapis.com') ||
    url.includes('cdn.jsdelivr.net') ||
    url.includes('unpkg.com')
  ) return;

  // Cache-first for app shell
  e.respondWith(
    caches.match(e.request).then(cached => {
      if (cached) return cached;
      return fetch(e.request).then(resp => {
        if (!resp || resp.status !== 200 || resp.type !== 'basic') return resp;
        const clone = resp.clone();
        caches.open(CACHE).then(c => c.put(e.request, clone));
        return resp;
      }).catch(() => {
        // Offline fallback: return cached index.html for navigation requests
        if (e.request.mode === 'navigate') return caches.match('/index.html');
      });
    })
  );
});
