import socket

server = socket.socket()
server.bind(("127.0.0.1", 12346))
server.listen(1)

print("Le serveur attend une connexion...")

client, address = server.accept()
print("Client connecté :", address)

message = client.recv(1024).decode()
print("Message reçu :", message)

client.send("Bonjour client".encode())

client.close()
server.close()