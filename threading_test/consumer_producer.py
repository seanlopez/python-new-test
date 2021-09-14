import queue
import threading
import time

qu = queue.Queue(maxsize=10)
def producer():
    count = 1
    while True:
        qu.put("NO.%s data"%count)
        print("produce has produce a data")
        count = count + 1
        time.sleep(0.5)

def comsumer(name):
    while True:
        print("%s has comsume the data [%s]"%(name,qu.get()))
        time.sleep(1)

t1 = threading.Thread(target=producer)
com1 = threading.Thread(target=comsumer,args=("comsumer1",))
com2 = threading.Thread(target=comsumer,args=("comsumer2",))

t1.start()
com1.start()
com2.start()
