class person:
    def __init__(self,pid,name,age):
        self.pid = pid
        self.name = name
        self.age = age 
    def display(self):
        print(self.pid)
        print(self.name)
        print(self.age)
class student:
    def __init__(self,stdId,name,roll,pan,adhar):
        self.stdId = stdId
        self.name = name
        self.roll = roll
        self.pan = pan
        self.adhar = adhar
    def showStd(self):
        print(self.stdId)
        print(self.name)
        print(self.roll)
        print(self.pan)
        print(self.adhar)