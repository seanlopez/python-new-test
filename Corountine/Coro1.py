from greenlet import greenlet

def foo():
    print("1,2")
    g2.switch()
    print("5,6")
    g2.switch()

def doo():
    print("3,4")
    g1.switch()
    print("7,8")

g1 = greenlet(foo)
g2 = greenlet(doo)
g1.switch()
