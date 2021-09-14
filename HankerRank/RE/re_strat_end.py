import re

s = input()
k = input()

pattern = re.compile(k)
r = pattern.search(s)

if k in s:
    while r:
        tup = (r.start(),r.end()-1)
        print(tup)
        r = pattern.search(s,r.start()+1)
else:
    print("(-1, -1)")
