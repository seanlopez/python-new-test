
class com:
    intro = ""
    def __init__(self,name,desc):
        self.name = name
        self.desc = desc

    def getintro(self):
        print(self.intro)

    def setintro(self):
        self.intro = input()
