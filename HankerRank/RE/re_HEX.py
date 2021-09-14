import re


cou = int(input())

for i in range(cou):
    line = input()
    list_re6 = re.findall("(?<=.)#[0-9a-fA-F]{3,6}",line)
    for i in list_re6:
        print(i)

'''
line = "background: -webkit-linear-gradient(top, #f9f9f9, #fff);"
list_re = re.findall("#...",line)
print(list_re)
'''
