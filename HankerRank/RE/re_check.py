
cou = int(input())

list1 = []
list2 = []
for i in range(cou):
    line = input()
    list1.append(line)
for j in range(cou):
    line = input()
    list2.append(line)

for z in range(cou):
    if list1[z] != list2[z]:
        print(z)