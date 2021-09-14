import re

s= "__comment__"

for i in range(len(s)-1):
    reg1 = "." * i
    reg = reg1 + "(\w)(\w).?"

    first_chr = re.search(reg, s).group(1)
    sec_chr = re.search(reg, s).group(2)
    if first_chr==sec_chr:
        if first_chr != "_":
            print(first_chr)
            break
        elif i == len(s)-2:
            print("-1")
        else:
            continue
    elif i == len(s) - 2:
        print("-1")


