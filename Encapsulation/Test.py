class test:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def display(self):
        print(self.id)
        print(self.name)
        print(self.age)
t = test(1000,"user1",28)
t1 = t
t1.id = 5000
t1.name = "user2"
t1.age = 43
t.display()
t1.display()