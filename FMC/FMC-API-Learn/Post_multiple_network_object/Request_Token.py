import requests
from requests.auth import HTTPBasicAuth
import fmc_info
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def get_token():
    api_path = "/api/fmc_platform/v1/auth/generatetoken"
    server = fmc_info.fmc_server
    url = server + api_path
    try:
        resp = requests.post(url, auth = HTTPBasicAuth(fmc_info.admin_username, fmc_info.admin_password), verify = False)
    except Exception as e:
        print(e)

    return {'token': resp.headers["X-auth-access-token"]}

'''
if __name__ == '__main__':
    print(get_token())
'''
