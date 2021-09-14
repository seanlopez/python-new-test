import socket

def server_init(ip, port):
    sock = socket.socket()
    sock2 = socket.socket()
    host = socket.gethostname()
    port = port
    ip = ip
    sock.bind((ip, port))

    sock.listen(5)
    port_dic = {"302432a15cec":"10003"}

    while True:
        try:
            c, addr = sock.accept()
            print("connected: "+ str(addr))
            client_mac_address = c.recv(1024).decode()
            port_num = port_dic[client_mac_address]
            c.send(port_num.encode())
            c.close()
        except Exception as e:
            pass
            print(e)

if __name__ == "__main__":
    server_init("10.140.232.139", 8998)