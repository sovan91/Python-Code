# Call By Reference Example
def changeValue(obj):
    obj.id = 3000
    obj.name = "user5"
    obj.age =29

class test:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def display(self):
        print(self.id)
        print(self.name)
        print(self.age)
t = test(2000,"user1",78)
t.display()
changeValue(t)
# call by reference of changeValue function
t.display()