import Request_Token
import fmc_info
import json
import sys
import requests
import pprint

token = Request_Token.get_token()['token']

def get_networks(token):
    token = token
    api_path = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networks"
    #print(token)
    headers = {'Content-Type': 'application/json', 'X-auth-access-token': token}
    url = fmc_info.fmc_server + api_path
    try:
        req = requests.get(url, headers=headers, verify = False)
        status_code = req.status_code
        resp = req.text
        if status_code == 200:
            print("Get success")
            json_resp = json.loads(resp)
            return json_resp
        else:
            req.raise_for_status()
            print("Error in Get" + resp)
    except requests.exceptions.HTTPError as err:
        print("Error in connection --> " + str(err))

def get_obj_url(objectname):
    for i in get_networks(token).get('items'):
        #print(i)
        if i.get("name") == objectname:
            return i.get("links").get("self")

def get_obj_detail(objecturl, token):
    objecturl = objecturl
    try:
        object_detail = requests.get(objecturl, headers = {'Content-Type': 'application/json', 'X-auth-access-token': token}, verify = False)
        return object_detail.json()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=3)
    pp.pprint(get_networks(token))
    #object_url = get_obj_url("10.0.0.1")
    #pp.pprint(get_obj_detail(object_url, token))

