import math
import os
import random
import re
import sys

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    sum_list = []
    sum_cou = 0

    numa = 0
    numb = 0
    numc = 0
    numd = 0
    nume = 0
    numf = 0
    numg = 0

    for idx in range(4):
        for fir_idx in range(4):
            numa = arr[idx][fir_idx]
            numb = arr[idx][fir_idx + 1]
            numc = arr[idx][fir_idx + 2]
            numd = arr[idx + 1][fir_idx + 1]
            nume = arr[idx + 2][fir_idx]
            numf = arr[idx + 2][fir_idx + 1]
            numg = arr[idx + 2][fir_idx + 2]
            sum_cou = numa + numb + numc + numd + nume + numf + numg
            sum_list.append(sum_cou)

    max_num = sum_list[0]
    for i in sum_list:
        if i > max_num:
            max_num = i

    print(max_num)