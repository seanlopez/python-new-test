import gevent
from gevent import monkey

monkey.patch_all()


def foo():
    print("this is func foo")
    gevent.sleep(2)
    print("switch to func foo")


def doo():
    print("switch to func doo")
    gevent.sleep(1)
    print("switch to func doo again")

def coo():
    print("switch to func coo")
    gevent.sleep(0)
    print("switch to func coo again")

gevent.joinall(
    [gevent.spawn(foo), gevent.spawn(doo), gevent.spawn(coo)]
)

