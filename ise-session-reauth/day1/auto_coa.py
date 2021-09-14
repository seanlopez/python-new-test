import requests
import urllib3
from lxml import etree
import ise_api_jinja
from jinja2 import Template
import deployment_info
import logging


class ise_auto_reauth(object):
    def __init__(self):
        self.ise_ip_address = deployment_info.ise_address
        self.username = deployment_info.username
        self.password = deployment_info.password
        self.psn_hostname_ip_mapping = deployment_info.ip_hostname_mapping_dict
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        self.logger = logging.getLogger(__name__)

    def ask_for_necessary_info(self):
        self.ise_ip_address = input("Please enter your ISE IP address:   ")
        self.username = input("Please enter the username:   ")
        self.password = input("Please enter the password:   ")

    def get_all_session_mac_isehostname_info(self):
        url_template = Template(ise_api_jinja.get_all_active_session)
        url = url_template.render(
            ise_ip_address=self.ise_ip_address
        )
        req = requests.get(url, headers={'Content-Type': 'application/json'}, auth=(self.username, self.password),
                           verify=False)
        output = req.text
        status_code = req.status_code
        if status_code != "200" or status_code != "201":
            self.logger.info("Get Success")
        else:
            self.logger.warning(f"Get Fail, status_code: {status_code}")
        par = etree.XML(output.encode('utf-8'))
        mac_isehostname_dict = {}
        for ele in par.xpath("*"):
            if ":" in ele.xpath("./calling_station_id/text()")[0]:
                mac_add = ele.xpath("./calling_station_id/text()")[0]
                mac_isehostname_dict[mac_add] = ele.xpath("./server/text()")[0]
            else:
                continue
        return mac_isehostname_dict

    def reauth_all_session(self, mac_isehostname_dict):
        print(mac_isehostname_dict)
        for mac_add in mac_isehostname_dict.keys():
            url_template = Template(ise_api_jinja.get_reauth_session)
            url = url_template.render(
                ise_ip_address=self.ise_ip_address,
                psn_hostname=self.psn_hostname_ip_mapping[mac_isehostname_dict[mac_add]],
                mac_address=mac_add
            )
            req = requests.get(url, headers={'Content-Type': 'application/json'}, auth=(self.username, self.password),
                               verify=False)
            output = req.text
            status_code = req.status_code
            if str(status_code) == "200" or str(status_code) == "201":
                self.logger.info("Get Success")
            else:
                self.logger.warning(f"Get Fail, status_code: {status_code}")


if __name__ == "__main__":
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    reauth_handler = ise_auto_reauth()
    if reauth_handler.ise_ip_address == "" or reauth_handler.username == "" or reauth_handler.password == "":
        reauth_handler.ask_for_necessary_info()
    reauth_handler.reauth_all_session(reauth_handler.get_all_session_mac_isehostname_info())
