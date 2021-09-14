import threading,time


event = threading.Event()

counter = 0
def redlight():
    event.set()
    global counter
    while True:
        counter = counter + 1
        if counter > 5 and counter < 10:
            print("\033[41;1mredlight is on,please waiting ....\033[0m")
            event.clear()
            time.sleep(1)
        elif counter >= 10:
            print("\033[42;1mgreenlight is on, please diving now ....\033[0m")
            event.set()
            counter = 0
            time.sleep(1)
        else:
            print("\033[42;1mgreenlight is on, please diving now ....\033[0m")
            counter = counter + 1
            time.sleep(1)

def car(name):
    while True:
        if event.is_set():
            print("[%s] is running now...."%name)
            time.sleep(1)
        else:
            print("[%s] is waiting now...."%name)
            event.wait()

t1 = threading.Thread(target=redlight)
t2 = threading.Thread(target=car, args=("Auto",))
t1.start()
t2.start()
