// static/js/sw.js

const CACHE_NAME = 'my-django-pwa-v1';
const ASSETS = [
  '/',
  '/static/css/home.css',
  '/static/css/impressora.css',
  '/static/css/tabela.css',
  '/static/icons/maskable_icon_x192 (4).png',
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => {
        return cache.addAll(ASSETS);
      })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request)
      .then((response) => {
        return response || fetch(event.request);
      })
  );
});