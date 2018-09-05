
N = int(input())

list1 = []
for i in range(N):
    com = input()
    if "insert" in com:
        com = com.split(" ")
        num1 = com[1]
        num2 = com[2]
        com.remove(num1)
        com.remove(num2)
        com.append(int(num1))
        com.append(int(num2))
        print(com)
        list1.insert(com[1],com[2])
    if com == "print":
        print(list1)
    if "remove" in com:
        com = com.split(" ")
        num1 = int(com[1])
        list1.remove(num1)
    if "append" in com:
        com = com.split(" ")
        num1 = int(com[1])
        list1.append(num1)
    if com == "sort":
        list1.sort()
    if com == "pop":
        list1.pop()
    if com == "reverse":
        list1.reverse()

