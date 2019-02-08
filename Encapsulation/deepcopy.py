import copy
class Person:
    def __init__(self, id, name, age):  # instance varibales
        self.id = id
        self.name = name
        self.age = age

    def show(self):
        print(self.id)
        print(self.name)
        print(self.age)


p = Person(2000, "user2", 78)
p.show()
print('******p******')
p1 = copy.deepcopy(p)
p1.show()
print('******p1 data******')
p1.id=3000
p1.name="user5"
p1.age=654
p.show()
p1.show()