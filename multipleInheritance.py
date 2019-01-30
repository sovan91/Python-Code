class person:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def show(self):
        print(self.id)
        print(self.name)
class student:
    def __init__(self, branch):
        self.branch = branch
    def stdInfo(self):
        print(self.branch)
class user(person,student):
    def __init__(self,id, name, branch, pan):
        person.__init__(self, id, name)
        student.__init__(self, branch)
        self.pan = pan
    def UserInfo(self):
        print(self.pan)
u = user(1,"sovan",101,876542)
u.show()
u.stdInfo()
u.UserInfo()
