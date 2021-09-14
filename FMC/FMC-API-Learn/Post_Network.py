import Request_Token
import fmc_info
import json
import requests

token = Request_Token.get_token()['token']

def post_networks(token, postdata):
    api_path = "/api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/networks"
    server = fmc_info.fmc_server
    url = server + api_path
    postdata = json.dumps(postdata)
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

if __name__ == "__main__":
    postdata = {
        "name": "net100000",
        "value": "2.0.0.0/24",
        "overridable": False,
        "description": "Network obj 1",
        "type": "Network"
    }
    post_networks(token, postdata)

