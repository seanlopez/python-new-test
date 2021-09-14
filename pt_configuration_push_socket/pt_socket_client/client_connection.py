import socket
import threading, time
import uuid

def get_mac_address():
    uuid_str = str(uuid.UUID(int=uuid.getnode()))
    uuid_list = uuid_str.split("-")
    mac_address = uuid_list[-1]
    return mac_address

def client_connect_to_server(ip, port, mac_address):
    sock = socket.socket()
    host = socket.gethostname()
    mac_address = mac_address

    sock.connect((ip, port))
    sock.send(mac_address.encode())
    print(sock.recv(1024).decode())
    sock.close()

if __name__ == "__main__":
    mac_addres = get_mac_address()
    client_connect_to_server("10.140.232.139", 8998, mac_addres)