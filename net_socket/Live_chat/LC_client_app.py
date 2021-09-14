import socket

class client_app:
    def __init__(self):
        self.client = socket.socket()
        self.client.connect(("localhost", 6969))

    def run(self):
        while True:
            info = input(">>:   ").strip()
            if len(info) == 0:    #防止因为客户端没有输入任何消息，而断开连接
                continue
            self.client.send(info.encode())

    def rece_(self):
        while True:
            data = self.client.recv(1024)
            print("")
            print(data.decode())

    def __del__(self):
        self.client.close()
