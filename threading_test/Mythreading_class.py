import threading
import time

class MyThreading(threading.Thread):
    def __init__(self,t_name,sleep_time):
        super(MyThreading,self).__init__()
        self.name = t_name
        self.time = sleep_time

    def run(self):
        print("task ",self.name," is run")
        time.sleep(self.time)


task_list = []
start_time = time.time()

for i in range(50):
    t = MyThreading("t%s"%i,2)
    task_list.append(t)
    t.start()

for tk in task_list:
    tk.join()

end_time = time.time()

print(end_time-start_time)
