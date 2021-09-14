import Request_Token
import fmc_info
import json
import requests
import csv

token = Request_Token.get_token()['token']

def deal_csv(csv_file_path):
    file = open(csv_file_path, "r")
    reader = csv.reader(file)
    name_list = []
    subnet_list = []

    for i in reader:
        #print(i[0][:] + i[1])
        name_list.append(i[0])
        subnet_list.append(i[1])
    return name_list, subnet_list

def post_networks(token, postdata):
    api_path = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networks?bulk=true"
    server = fmc_info.fmc_server
    url = server + api_path
    postdata = json.dumps(postdata)
    print(postdata)
    try:
        req = requests.post(url, data=postdata, headers = {'Content-Type': 'application/json', 'X-auth-access-token': token}, verify=False)
        resp = req.text
        print(req.status_code)
        if req.status_code == 201 or req.status_code == 202:
            print("Post Success")
        else:
            req.raise_for_status()
            print(resp)

        req.close()
    except Exception as e:
        print(e)

def json_generator(name_list, subnet_list):
    dic_list = []
    count = 0
    for i in name_list:
        dic1 = {"name":"", "value":"", "overridable": False, "description": "Network obj 1","type": "Network"}
        dic1["name"] = i
        dic1["value"]=subnet_list[count]
        dic_list.append(dic1)
        count = count+1

    #print(dic_list)
    #print(json.dumps(dic_list))

    return dic_list


if __name__ == "__main__":
    name_list = deal_csv("networks.csv")[0]
    #print(name_list)
    subnet_list = deal_csv("networks.csv")[1]

    postdata = json_generator(name_list, subnet_list)
    post_networks(token, postdata)
    #print(postdata)
    #json_generator(name_list, subnet_list)
