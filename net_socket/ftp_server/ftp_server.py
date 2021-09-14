import socket


server = socket.socket()

server.bind(("localhost",6969))

server.listen()


while True:
    print("Wait for data now!")
    con, addr = server.accept()
    while True:
        print("Wait for data now!")
        try:
            data = con.recv(1024)
        except ConnectionResetError as e:
            print("disconnect...")
            break
        else:
            print(data)

server.close()