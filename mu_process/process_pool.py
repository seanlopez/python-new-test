from multiprocessing import Process,Pool,freeze_support
import time

def func_foo(i):
    print("this process is %s"%i)
    time.sleep(1)
    return i

def Bar(i):
    print("the %s is work over"%i)

if __name__ == "__main__":
    freeze_support()


    pool = Pool(processes=5)

    for i in range(20):
        pool.apply_async(func=func_foo,callback=Bar,args=("pro%s"%i,))

    pool.close()
    pool.join()