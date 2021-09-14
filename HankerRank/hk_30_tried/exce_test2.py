class myError(Exception):
    def __init__(self,msg):
        self.msg = msg

    def __str__(self):
        return "two num must greater than or equal to 0"

class calu:
    def run(self,num1,num2):
        if num1 >= 0 and num2 >= 0:
            return num1 ** num2
        else:
            raise myError("num error")

num1 = int(input())
num2 = int(input())

ca = calu()
try:
    last = ca.run(num1,num2)
    print(last)
except Exception as e:
    print(e)
