import socketserver


#NO.1 ：写一个class去继承BaseRequestHandler
#NO.2 : 在自己写的class中，重写handler函数，handler函数规定的如何去接受并处理客户端的请求
class MyTCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            try:
                #self.request is the TCP socket connect to the client (client instance is self.request, you dont need to accept the client)
                self.data = self.request.recv(1024).strip()
            except ConnectionResetError as e:
                print("disconnect")
                break
            else:
                print(self.data)
                self.request.send(self.data.upper())

#NO.3 : 实例化TCPserver这个类，需要将ip地址和自己创建的类传入
if __name__ == "__main__":
    HOST, PORT = "localhost",6969

    server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandler)    #开始监听地址，并且按照Handler中的规定去处理client端
    #NO.4 : 开始 持续的监听
    server.serve_forever()

