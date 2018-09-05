nl = []
sc_list = []
for i in range(int(input())):
    name = input()
    score = float(input())
    sc_list.append(score)
    nl.append([])
    nl[i].append(name)
    nl[i].append(score)

sc_list.sort()
lowest = sc_list[0]
cou = 0
for i in sc_list:
    if i == lowest:
        cou = cou + 1

for i in range(cou):
    sc_list.remove(lowest)

lower = sc_list[0]
nl.sort()
for i in nl:
    if i[1] == lower:
        print(i[0])
