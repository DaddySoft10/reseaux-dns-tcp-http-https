import socket

domain = "elhamri.com"

ip = socket.gethostbyname(domain)

print(f"Nom de domaine : {domain}")
print(f"Adresse IP : {ip}")