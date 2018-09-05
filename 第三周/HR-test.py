a = [[11,2,4],[4,5,6],[10,8,-12]]
n = 3


def diagonalDifference(arr, n):
    list1 = []
    list2 = []
    count = n - 1

    for i in range(n):
        list1.append(arr[i][i])

    for i in range(n):
        while True:
            list2.append(arr[i][count])
            count = count -1
            break

    num1 = 0
    mynum2 = 0

    for i in list1:
        num1 = num1 + i

    #print(num1)

    for i in list2:
        mynum2 = mynum2 + i

    #print(mynum2)

    x = abs(num1 - mynum2)
    return x

rel = diagonalDifference(a, n)

print(rel)