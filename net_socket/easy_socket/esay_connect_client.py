import socket


client = socket.socket()

client.connect(("localhost",6969))

client.send(b"hello socket!")

data = client.recv(1024)

print(data)

client.close()
