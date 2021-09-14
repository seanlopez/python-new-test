import requests
from bs4 import BeautifulSoup

url = "https://mp.weixin.qq.com/s/7qgz2PNaUxcf-WxUzzbf5A"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
}
req = requests.get(url, headers=header)
#print(req.status_code)

html = req.text

soup = BeautifulSoup(html, 'html.parser')
img_list = soup.find_all("img")

for img_link in img_list:
    filename = str(img_list.index(img_link)) + '.jpeg'
    img_url = img_link.get("data-src")
    if img_url:
        img_req = requests.get(img_url)
        image = img_req.content
        with open(filename, "wb+") as f:
            f.write(image)
            f.close()
        print("the {} image was stored".format(img_list.index(img_link)))



