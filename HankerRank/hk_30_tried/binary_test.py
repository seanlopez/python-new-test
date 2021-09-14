n = int(input())
n_bin = bin(n)
n_bin = str(n_bin[2:])
cou = 0
cou1 = 0
cout_one_list = []
len_bin = len(n_bin)
cou_loop = 0
cou_loop = int(cou_loop)

for i in n_bin:
    cou_loop = cou_loop + 1
    if i == "1":
        cou = cou + 1
    elif i == "0":
        cout_one_list.append(cou)
        cou = 0
    if cou_loop == int(len(n_bin)):
        cout_one_list.append(cou)
        cou = 0

n = cout_one_list[0]
for j in cout_one_list:
    if j > n:
        n = j

cout_zero_list = []

cou_loop = 0
for i in n_bin:
    cou_loop = cou_loop + 1
    if i == "0":
        cou = cou + 1
    elif i == "1":
        cout_zero_list.append(cou)
        cou = 0
    if cou_loop == int(len(n_bin)):
        cout_zero_list.append(cou)
        cou = 0

t = cout_zero_list[0]
for j in cout_zero_list:
    if j > t:
        t = j

if n > t:
    print(n)
else:
    print(t)