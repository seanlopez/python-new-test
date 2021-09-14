import pymongo
from master_sheet_edit.mongo_db_operation import ConnectionDBInfo


class MongoOperation():
    def __init__(self):
        self.connection = self.connect_server(ConnectionDBInfo.connect_server_ip, ConnectionDBInfo.connect_server_port)

    def connect_server(self, ip, port):
        myclient = pymongo.MongoClient(ip, port)
        return myclient

    def create_db(self, mydb_name):
        dblist = self.connection.list_database_names()
        if mydb_name in dblist:
            print(mydb_name + " was already created")
            return self.connection[mydb_name]
        else:
            mydb = self.connection[mydb_name]
            return mydb

    def create_collection(self, db_obj, mycollection_name):
        collist = db_obj.list_collection_names()
        if mycollection_name in collist:
            print(mycollection_name+" was already created")
            return db_obj[mycollection_name]
        else:
            mycollection = db_obj[mycollection_name]
            return mycollection

    def get_db(self, db_name):
        mydb = self.connection[db_name]
        return mydb

    def get_collection(self, db_obj, collection_name):
        mycollection = db_obj[collection_name]
        return mycollection

    def get_collection_1(self, db_name, collection_name):
        mydb = self.connection[db_name]
        mycol = mydb[collection_name]
        return mycol

    def insert_single_dic(self, collection_obj, dict_name):
        insert_result = collection_obj.insert_one(dict_name)
        return insert_result

    def insert_multiple_dic(self, collection_obj, dict_list):
        insert_result = collection_obj.insert_many(dict_list)
        return insert_result

    def get_hostname(self, dbname, colname, policy = None):
        mydb = self.get_db(dbname)
        mycol = self.get_collection(mydb, colname)
        hostname_list = []
        for x in mycol.find(policy):
            # print(x["hostname"])
            device_hostname = x["hostname"]
            if device_hostname.upper() in hostname_list:
                continue
            else:
                hostname_list.append(device_hostname.upper())
        return hostname_list

# if __name__ == "__main__":
#     MOO = MongoOperation()
#     hostname_list = MOO.get_hostname("tianqi_db", "l3_interface_list")
#     print(hostname_list)

