import Request_Token
import fmc_info
import json
import sys
import requests
import pprint

token = Request_Token.get_token()["token"]

def get_all_accesspolicies(token):
    api_path = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies"
    server = fmc_info.fmc_server
    url = server + api_path
    token = token
    try:
        req = requests.get(url, headers = {'Content-Type': 'application/json', 'X-auth-access-token': token}, verify = False)
        if req.status_code == 200:
            return json.loads(req.text)
    except Exception as e:
        print(e)
'''
if __name__ == "__main__":
    pp = pprint.PrettyPrinter(indent=3)
    pp.pprint(get_all_accesspolicies(token))
'''
