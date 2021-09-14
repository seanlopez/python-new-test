import time

'''
dt = '2018-01-01 10:40:30'
ts = int(time.mktime(time.strptime(dt, "%Y-%m-%d %H:%M:%S")))

ts2 = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
print (ts)

print(ts2)

t1 = "Sun 10 May 2015 13:54:36 -0700"
t1_list = t1.split(" ")
print(t1_list)
t1_sta = str(t1_list[3])+"-"+"5"+"-"+str(t1_list[1])+" "+str(t1_list[4])
print(t1_sta)
t1_sec = int(time.mktime(time.strptime(t1_sta, "%Y-%m-%d %H:%M:%S")))
print(t1_sec)
delta = (time.timezone - int((t1_list[5])))/3600
print(delta)
'''

def time_delta(t1, t2):
    t1_list = t1.split(" ")
    t2_list = t2.split(" ")
    t1_sta = str(t1_list[3])+"-"+"5"+"-"+str(t1_list[1])+" "+str(t1_list[4])
    t2_sta = str(t2_list[3])+"-"+"5"+"-"+str(t2_list[1])+" "+str(t2_list[4])
    t1_sec = int(time.mktime(time.strptime(t1_sta, "%Y-%m-%d %H:%M:%S")))
    t2_sec = int(time.mktime(time.strptime(t2_sta, "%Y-%m-%d %H:%M:%S")))
    cha = abs(t2_sec - t1_sec)-5*3600-30*60   #时区是的正负号取反，+0530，5代表5小时，3代表30分，0代表0s
    return int(cha)

t1 = "Sat 02 May 2015 19:54:36 +0530"
t2 = "Fri 01 May 2015 13:54:36 -0000"

cha = time_delta(t1,t2)
print(cha)
