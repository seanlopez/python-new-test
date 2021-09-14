import re

cou = int(input())
for i in range(cou):
    num = input()
    num = str(num)
    if re.search("^[+-]?[0-9]*\.[0-9]*$",num):
        print("True")
    else:
        print("False")