import csv

file = open("endpoints.csv", "r")
reader = csv.reader(file)

for i in reader:
    print(i[0][:] + i[1])
