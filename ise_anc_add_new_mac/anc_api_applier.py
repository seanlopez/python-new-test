import requests
import urllib3
import json


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class api_applier(object):
    def __init__(self, config_json):
        config_file = open(config_json, "r")
        config = json.loads(config_file.read())
        self.address = config["address"]
        self.api = config["api"]
        self.username = config["username"]
        self.password = config["password"]

    def upload_address(self, json_content):
        uri = self.address + self.api
        req = requests.put(uri, headers={'accept': 'application/json', 'Content-Type': 'application/json'}, auth=(self.username, self.password), verify=False, data=json_content)

        return req.status_code

    def get_info(self):
        uri = self.address + self.api
        req = requests.get(uri, headers={'accept': 'application/json', 'Content-Type': 'application/json'}, auth=(self.username, self.password), verify=False)

        return req.status_code

if __name__ == "__main__":
    api_applier = api_applier("ise_basic_info.json")
    quaratine_content = open("quaratine_mac.json", "r")
    json_content = quaratine_content.read()
    print(api_applier.upload_address(json_content))








