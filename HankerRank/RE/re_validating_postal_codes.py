import re


s = "121386"   #长度限定为6为
regex_integer_in_range = r"^[1-9][\d]{5}$"    #规定长度为6
regex_alternating_repetitive_digit_pair = r"(\d)(?=\d\1)"    #向后预查，d匹配任意一个数字，中间间隔任意一个数字，之后的数字和d匹配的数字相同

print(re.match(regex_integer_in_range,s).group())
print(re.findall(regex_alternating_repetitive_digit_pair,s))