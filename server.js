const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const PORT = parseInt(process.argv[2] || '5500', 10);
const PUBLIC_DIR = __dirname;

const MIME_TYPES = {
  '.html': 'text/html; charset=UTF-8',
  '.css': 'text/css; charset=UTF-8',
  '.js': 'text/javascript; charset=UTF-8',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf'
};

const ROUTES = {
  '/': 'index.html',
  '/search': 'search.html',
  '/wishlist': 'wishlist.html',
  '/cart': 'cart.html',
  '/checkout': 'checkout.html',
  '/payment': 'payment.html',
  '/order-success': 'order-success.html',
  '/product': 'product.html'
};

const server = http.createServer((req, res) => {
  const parsed = url.parse(req.url);
  const cleanPath = (parsed.pathname || '/').replace(/\/$/, '') || '/';

  let filePath = '';
  if (ROUTES[cleanPath]) {
    filePath = path.join(PUBLIC_DIR, ROUTES[cleanPath]);
  } else if (cleanPath.startsWith('/product/')) {
    const relAsset = cleanPath.slice('/product/'.length);
    const diskAsset = path.join(PUBLIC_DIR, relAsset);
    if (fs.existsSync(diskAsset) && fs.statSync(diskAsset).isFile()) {
      filePath = diskAsset;
    } else {
      filePath = path.join(PUBLIC_DIR, 'product.html');
    }
  } else {
    filePath = path.join(PUBLIC_DIR, cleanPath);
  }

  // Check if file exists
  if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
    const ext = path.extname(filePath).toLowerCase();
    const contentType = MIME_TYPES[ext] || 'application/octet-stream';
    res.writeHead(200, {
      'Content-Type': contentType,
      'Access-Control-Allow-Origin': '*'
    });
    fs.createReadStream(filePath).pipe(res);
  } else {
    res.writeHead(404, { 'Content-Type': 'text/plain' });
    res.end('404 Not Found');
  }
});

server.on('error', (err) => {
  console.error('Server error:', err);
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`NOVELLE Server running on http://localhost:${PORT} with clean routing enabled.`);
});
