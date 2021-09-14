count = int(input())


for i in range(count):
    line = str(input())
    line_list = line.split(" ")
    a = line_list[0]
    b = line_list[1]
    try:
        print(int(a)//int(b))
    except (ZeroDivisionError,ValueError) as e:
        print("Error Code:", e)