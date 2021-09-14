import socket
import threading

class LC_ser_app:
    con_list = []
    def server_run(self):
        server = socket.socket()

        server.bind(("localhost",6969))

        server.listen(5)


        while True:
            print("Wait for data now!")
            con,addr = server.accept()
            self.con_list.append(con)
            print("con1 is connect")
            con1,addr1 = server.accept()
            self.con_list.append(con1)
            print("con2 is connect")
            t1 = threading.Thread(target=self.server_app, args=(self.con_list[0], self.con_list[1]))
            t2 = threading.Thread(target=self.server_app, args=(self.con_list[1], self.con_list[0]))

            t1.start()
            t2.start()


    def server_app(self,con1,con2):
        while True:
            try:
                data = con1.recv(1024)
            except ConnectionResetError as e:  # 如果有该异常，说明客户端断开，服务端可以结束这个循环，进入下一个循环,也就是可以继续等待连接
                print("disconnect...")
                self.con_list.pop()
                break
            else:
                con2.send(data)
                print(data)


ser = LC_ser_app()
ser.server_run()