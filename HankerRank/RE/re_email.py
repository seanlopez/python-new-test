import email.utils
import re


cou = int(input())

for i in range(cou):
    em_add = input()
    tup = email.utils.parseaddr(em_add)
    list1 = re.findall("@",tup[1])
    if len(list1) == 1:
        web_dom = re.search("(?<=\@).*", tup[1]).group()
        list2 = re.findall("\.", web_dom)
        if len(list2) == 1:
            dom = re.search("(?<=\.).*",web_dom).group()
            name = re.search(".*(?=\@)",tup[1]).group()
            website = re.search("(?<=\@).*(?=\.)",tup[1]).group()
            name_fir = re.match("^[A-Za-z]",name)   #匹配大写或者小写
            if name_fir :
                if website.isalpha():
                    if dom.isalpha():
                        if 0<len(dom) <= 3:
                            print(em_add)
