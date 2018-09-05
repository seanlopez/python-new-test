import re

ti = int(input())
for i in range(ti):
    line = input()
    if re.match("#",line):
        print(line)
    elif "&&" or "||" in line:
        line = re.sub("(?<= )&&(?= )","and",line)
        line = re.sub("(?<= )\|\|(?= )", "or", line)
        print(line)
    else:
        print(line)

