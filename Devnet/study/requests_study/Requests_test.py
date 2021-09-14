import requests

url1 = "https://www.cisco.com"
reqs = requests.get(url1)
print(reqs.status_code)

url2 = "http://httpbin.org/post"
'''
reqs2 = requests.post(url2)
print(reqs2.json())

reqs3 = requests.options(url2)
print(reqs3.content)
'''

url3 = "http://httpbin.org/get"
data = {"name":"sean", "base":"dalian"}
reqs4 = requests.get(url3, data=data)
print(reqs4.text)

header = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"}
reqs5 = requests.get(url1, headers = header)
#print(reqs5.text)

url4 = "http://httpbin.org/cookies"
reqs6 = requests.get(url4)
print(reqs6.cookies)

url5 = "http://httpbin.org/cookies/set/"
cookies = {"username":"password"}
reqs7 = requests.get(url5, cookies=cookies)
print(reqs7.cookies)

url6 = "http://httpbin.org/basic-auth"
reqs8 = requests.get(url6, auth = ("yuan","tianqi"))
print(reqs8.status_code)