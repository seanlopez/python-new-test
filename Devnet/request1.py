import json
import requests
import sys

server = "https://10.79.247.116"

username = "admin"
password = "C!sc0123"

r = None
headers = {'Content-Type': 'application/json'}
api_auth_path = "/api/fmc_platform/v1/auth/generatetoken"
auth_url = server + api_auth_path
try:
    r = requests.post(auth_url, headers=headers, auth=requests.auth.HTTPBasicAuth(username, password),verify=False)
    auth_headers = r.headers
    print(auth_headers)
    auth_token = auth_headers.get('X-auth-access-token', default=None)
    if auth_token == None:
        print("auth_token not found. Exiting...")
        sys.exit()
except Exception as err:
    print("Error in generating auth token --> " + str(err))
    sys.exit()


headers['X-auth-access-token']=auth_token
print(headers['X-auth-access-token'])
