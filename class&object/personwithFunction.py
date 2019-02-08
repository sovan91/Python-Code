def sum(x,y):
    res = x+y
    print(res)
class person:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age =age
    def show(self):
        print(self.id)
        print(self.name)
        print(self.age)
p = person(100,"user1",27)
### a function inside a class it can be called with  a  help of object
p.show()
##
sum(10,20)