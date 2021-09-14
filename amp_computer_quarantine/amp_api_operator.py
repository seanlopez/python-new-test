import requests
import urllib3
import json


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class amp_api_operator(object):
    def __init__(self):
        configure_file = open("amp_info.json", "r")
        configure = json.loads(configure_file.read())

        self.address = configure["address"]
        self.api = configure["api"]
        self.uri = self.address + self.api
        self.client_id = configure["api_client_id"]
        self.key = configure["api_key"]
        self.headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }

    def get_operator(self, api=None):
        if api != None:
            uri = self.address + api
        else:
            uri = self.uri
        # print(uri)
        req = requests.get(uri, headers=self.headers,
                           auth=(self.client_id, self.key), verify=False)

        return req.text

    def get_connector_id(self, json, connector_hostname):
        connector_guid = ""
        for connector in json["data"]:
            if connector["hostname"] == connector_hostname:
                connector_guid = connector["connector_guid"]
                break

        return connector_guid

    def get_group_id(self, json, group_name):
        group_guid = ""
        for group in json["data"]:
            if group["name"] == group_name:
                group_guid = group["guid"]

        return group_guid

    def add_endpoint_2_group(self, connector_id, group_id):
        uri = self.uri + "/" + connector_id
        body = json.dumps({"group_guid": group_id})
        req = requests.patch(uri, headers=self.headers, auth=(self.client_id, self.key), verify=False, data=body)

        return req.status_code


if __name__ == "__main__":
    control_info = open("control_info.json", "r")
    control_json = json.loads(control_info.read())
    control_info.close()

    connector_name = control_json["connector_name"]
    group_name = control_json["group_name"]

    operator = amp_api_operator()

    # Get connector ID
    connects_json = json.loads(operator.get_operator("/v1/computers"))
    connector_id = operator.get_connector_id(connects_json, connector_name)

    # Get group ID
    group_json = json.loads(operator.get_operator("/v1/groups"))
    group_id = operator.get_group_id(group_json, group_name)

    # Add connector to group
    print("status_code: " + str(operator.add_endpoint_2_group(connector_id, group_id)))
