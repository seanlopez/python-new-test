import multiprocessing


def run(name):
    print("process %s is run"%name)


if __name__ == "__main__":
    for i in range(10):
        p = multiprocessing.Process(target=run,args=("pro%s"%i,))
        p.start()
        p.join()
