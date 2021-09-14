import csv
import json
import requests
import urllib3
import pprint

def discover_group(group_name):
    url = "https://10.79.247.86:9060/ers/config/endpointgroup"

    headers = {
        'accept': "application/json",
        'content-type': "application/json",
    }

    req = requests.get(url, headers=headers, auth=("admin", "C!sc0123"), verify=False)

    group_id = []

    if req.status_code == 200:
        data = json.loads(req.text)
        pp = pprint.PrettyPrinter(indent=3)
        # pp.pprint(data.get('SearchResult'))
        resource = data.get('SearchResult').get('resources')
        for i in group_name:
            #print(i.get("id") + i.get("name"))
            for j in resource:
                if j.get("name") == i:
                    group_id.append(j.get("id"))
    return group_id

def deal_csv(csv_file_path):
    file = open(csv_file_path, "r")
    reader = csv.reader(file)
    mac_list = []
    group_list = []

    for i in reader:
        #print(i[0][:] + i[1])
        mac_list.append(i[0][:-1])
        group_list.append(i[1])
    return mac_list, group_list

def post_all_endpints(mac_list, group_list):
    url = " https://10.79.247.86:9060/ers/config/endpoint"

    headers = {
        'accept': "application/json",
        'content-type': "application/json",
    }

    json_list = []
    count = 0
    for i in mac_list:
        json_format = '''{{"ERSEndPoint" : {{"mac" : "{}","groupId" : "{}","staticGroupAssignment" : true}}}}'''.format(i,group_list[count])
        json_list.append(json_format)
        count = count+1

    print(json_list)

    for j in json_list:
        req = requests.post(url, headers=headers, auth=("admin", "C!sc0123"), verify=False, data=j)
        print(req.status_code)


if __name__ == "__main__":

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    #print(discover_group("Meralco_Printer"))
   # print(deal_csv("endpoints.csv")[0])
    mac_list = deal_csv("endpoints.csv")[0]
    group_list = deal_csv("endpoints.csv")[1]
    print(mac_list)
    print(group_list)
    print(discover_group(group_list))
    group_list_id_list = discover_group(group_list)
    post_all_endpints(mac_list, group_list_id_list)
