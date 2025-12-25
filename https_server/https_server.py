from http.server import HTTPServer, SimpleHTTPRequestHandler
import ssl

server_address = ("0.0.0.0", 4443)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="cert.pem", keyfile="key.pem")

httpd.socket = context.wrap_socket(httpd.socket, server_side=True)

print("Serveur HTTPS en cours sur https://localhost:4443")
httpd.serve_forever()