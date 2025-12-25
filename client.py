import socket

client = socket.socket()
client.connect(("127.0.0.1", 12346))

client.send("Bonjour serveur".encode())

response = client.recv(1024).decode()
print("Réponse du serveur :", response)

client.close()