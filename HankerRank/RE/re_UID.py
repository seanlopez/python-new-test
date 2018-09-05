import re


cou = int(input())

for i in range(cou):
    uid = input()
    if len(uid) == 10:
        list_upper = re.findall("[A-Z]",uid)
        list_num = re.findall("\d",uid)
        if len(list_upper) >= 2 and len(list_num)>=3:
            list_line=[]
            for i in uid:
                list_line.append(i)
            set_line = set(list_line)
            if len(set_line) == len(list_line):
                print("Valid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")

'''

line = "B128DHAH11"
list_line=[]
for i in line:
    list1.append(i)
'''

