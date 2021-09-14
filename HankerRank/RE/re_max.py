import math
import os
import random
import re
import sys


nm = input().split()
# print(nm)

n = int(nm[0])

m = int(nm[1])

matrix = []

chr_ = ""
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

for j in range(m):
    for i in range(n):
        s = matrix[i]
        pattern = re.compile(".")
        char = pattern.match(s, j)
        chr_ = chr_ + char.group()
chr_ = re.sub("(?<=\w)\W+(?=\w)", " ", chr_)
print(chr_)
