import pymongo
import ConnectionDBInfo

def connection():
    myclient = pymongo.MongoClient(ConnectionDBInfo.connect_server_ip, ConnectionDBInfo.connect_server_port)
    return myclient
