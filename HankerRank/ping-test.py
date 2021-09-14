import os,sys

while True:
    for i in range(120,254):
        os.system("ping 10.124.114.%s -n 1"%i)



