import socket


client = socket.socket()

client.connect(("localhost",6969))

while True:
    info = input(">>:   ").strip()
    if len(info) == 0:    #防止因为客户端没有输入任何消息，而断开连接
        continue
    client.send(info.encode())
    data = client.recv(1024)
    print(data)

client.close()
