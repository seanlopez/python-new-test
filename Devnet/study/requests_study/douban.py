import requests

#https://movie.douban.com/j/search_tags?type=movie&tag=豆瓣高分&source=

#https://movie.douban.com/j/search_subjects?type=movie&tag=%E8%B1%86%E7%93%A3%E9%AB%98%E5%88%86&sort=recommend&page_limit=20&page_start=0

url = "https://movie.douban.com/j/search_subjects"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:82.0) Gecko/20100101 Firefox/82.0"
}

paramter = {
    "type" : "movie",
    "tag" : "豆瓣高分",
    "sort" : "recommend",
    "page_limit" : "2",
    "page_start" : "3"
}

req = requests.get(url, headers = header, params=paramter)
douban_data = req.json()
print(douban_data)

for dic in douban_data["subjects"]:
    #print(dic)
    name = dic["title"]
    print(name)


