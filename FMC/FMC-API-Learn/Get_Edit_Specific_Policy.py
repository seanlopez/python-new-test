import Request_Token
import fmc_info
import json
import sys
import requests
import pprint
from Get_All_Policies import get_all_accesspolicies

token = Request_Token.get_token()["token"]
def get_accesspolicy_url(policyname):
    policylist = get_all_accesspolicies(token).get("items")
    for i in policylist:
        if i.get("name") == policyname:
            return i.get("links").get("self")

def get_policy_detail(url, token):
    try:
        req = requests.get(url, headers = {'Content-Type': 'application/json', 'X-auth-access-token': token}, verify = False)
        if req.status_code == 200:
            return json.loads(req.text)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    #print(get_all_accesspolicies(token))
    pp = pprint.PrettyPrinter(indent=3)
    url = get_accesspolicy_url("BCS-Test")
    pp.pprint(get_policy_detail(url, token))

