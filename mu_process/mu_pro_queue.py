from multiprocessing import Process,Queue

def q_oper(qq):
    qq.put("hello world!")

if __name__ == "__main__":
    q = Queue()
    p = Process(target=q_oper,args=(q,))
    p.start()
    p.join()
    print(q.get())
