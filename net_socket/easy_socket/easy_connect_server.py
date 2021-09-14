import socket


server = socket.socket()

server.bind(("localhost",6969))

server.listen()

con,addr = server.accept()

data = con.recv(1024)

print(data)

con.send(b"nice to meet you")

server.close()
