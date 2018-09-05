import re


'''从字符串索引的第5个开始匹配'''

s = "yuan tian qi"

pattern = re.compile("tian.*",re.I)

r = pattern.match(s,5)   #限定索引为5
print(r.group())

