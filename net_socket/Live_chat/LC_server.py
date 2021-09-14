import socket


server = socket.socket()

server.bind(("localhost",6969))

server.listen()

while True:
    print("Wait for data now!")
    con,addr = server.accept()
    while True:
        try:
            data = con.recv(1024)
        except ConnectionResetError as e:     #如果有该异常，说明客户端断开，服务端可以结束这个循环，进入下一个循环,也就是可以继续等待连接
            print("disconnect...")
            break
        else:
            con.send(b"ok")
            print(data)

server.close()
