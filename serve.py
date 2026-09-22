from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
import sys
import os
import urllib.parse

class RobustHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Parse query string and clean path
        parsed = urllib.parse.urlparse(path)
        clean_path = parsed.path.rstrip('/')

        # Clean routing rules
        routes = {
            '/search': 'search.html',
            '/wishlist': 'wishlist.html',
            '/cart': 'cart.html',
            '/checkout': 'checkout.html',
            '/payment': 'payment.html',
            '/order-success': 'order-success.html',
            '/product': 'product.html'
        }

        # Check exact route match
        if clean_path in routes:
            return os.path.join(os.getcwd(), routes[clean_path])

        # Check /product/:id route pattern
        if clean_path.startswith('/product/'):
            # If a static asset is requested relative to /product/, serve the asset
            rel_asset = clean_path[len('/product/'):]
            disk_asset = os.path.join(os.getcwd(), rel_asset.replace('/', os.sep))
            if os.path.isfile(disk_asset):
                return disk_asset
            return os.path.join(os.getcwd(), 'product.html')

        return super().translate_path(path)

    def log_message(self, format, *args):
        try:
            print(f"[{self.log_date_time_string()}] {self.client_address[0]} - {args[0]} {args[1]}", flush=True)
        except Exception:
            pass

if __name__ == '__main__':
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 5500
    server = ThreadingHTTPServer(('0.0.0.0', port), RobustHandler)
    server.allow_reuse_address = True
    print(f"NOVELLE Web Server listening on port {port} with clean URL routing enabled...", flush=True)
    server.serve_forever()
