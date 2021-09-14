name_list = ["yuan", "tian", "qi","li","yu","ke"]
sorce_list = [11,37.1,666,37.1,11,88]


num = len(name_list)
last_list = []

for i in range(num):
    last_list.append([])
    last_list[i].append(name_list[i])
    last_list[i].append(sorce_list[i])

sorce_list.sort()
sorce_min = sorce_list[0]
m = 0

for i in sorce_list:
    if i > sorce_min:
        m = i
        break

for i in last_list:
    if i[1] == m:
        print(i[0])


