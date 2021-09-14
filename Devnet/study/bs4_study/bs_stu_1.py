from bs4 import BeautifulSoup

html = '''
<html>
<title>Testing</title>
<body>
hello world
<a class="bro" href="www.baidu.com">a1</a>
<a class="bro" href="www.cisco.com">a2</a>
<a class="bro" href="www.google.com">a3</a>
</body>
</html>
'''

soup =  BeautifulSoup(html, 'html.parser')


for link in soup.find_all("a"):
    print(link.get("href"))
    print(link['class'])
