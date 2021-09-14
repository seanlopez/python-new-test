import re


cou = int(input())

for i in range(cou):
    line = input()
    if line.isnumeric() and len(line) == 10:
        if re.match("^[789]",line):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
