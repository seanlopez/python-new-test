import re


s = "yuantianqi"

pattern = re.compile(".")
for i in range(len(s)):
    print(pattern.match(s,i).group())
