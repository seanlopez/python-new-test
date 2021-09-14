import threading,time



def run(n):
    sm.acquire()
    print("task: ",n)
    time.sleep(2)
    sm.release()

sm = threading.BoundedSemaphore(2)
for i in range(22):
    t = threading.Thread(target=run,args=("t%s"%i,))
    t.start()




