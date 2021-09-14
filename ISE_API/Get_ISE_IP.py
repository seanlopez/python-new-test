import requests
import urllib3
from lxml import etree

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://10.79.247.85/admin/API/mnt/Session/ActiveList"

try:
    req = requests.get(url, headers = {'Content-Type': 'application/json'}, auth = ("admin", "C!sc0123"), verify = False)
    req_code = req.status_code
    if req_code != (200 or 201):
        print("Test Fail")
        print(req_code)
    else:
        print("Status checking success")
except Exception as e:
    print("No Response")

'''
data = req.text
par = etree.XML(data.encode('utf-8'))
#print(par.xpath("//framed_ip_address/text()")[0])

NAD_Floor_Mapping = {"10.79.247.45": "Floor_1", "10.79.247.18": "Floor_2"}
for ele in par.xpath("*"):
    #print(par.xpath("*"))
    #print(ele)
    #print(ele.xpath("./framed_ip_address/text()"))
    if len(ele.xpath("./framed_ip_address/text()")) != 0:
        if len(ele.xpath("./nas_ip_address/text()")) != 0:
            #print(ele.xpath("./framed_ip_address/text()")[0])
            Endpoint_IP = ele.xpath("./framed_ip_address/text()")[0]
            #print(ele.xpath("./nas_ip_address/text()")[0])
            NAD_IP = ele.xpath("./nas_ip_address/text()")[0]
            Floor = NAD_Floor_Mapping[NAD_IP]
            print("Endpoint_IP:{}    NAD_IP:{}    NAD_Floor:{}".format(Endpoint_IP, NAD_IP, Floor))
        else:
            pass
    else:
        pass
'''
