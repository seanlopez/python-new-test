cou = int(input())

dic = {}

for i in range(cou):
    line = input()
    line_list = line.split(" ")
    dic[line_list[0]] = line_list[1]

