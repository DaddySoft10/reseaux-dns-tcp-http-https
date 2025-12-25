from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Bonjour depuis mon serveur HTTP")

server = HTTPServer(("0.0.0.0", 8080), SimpleHandler)

print("Serveur HTTP en cours sur le port 8080")
server.serve_forever()