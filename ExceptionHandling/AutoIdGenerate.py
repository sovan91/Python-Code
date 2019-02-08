class person:
    id = 0
    def __init__(self, id, name, age):
        self.id = person.id
        self.name = name
        self.age = age
    def display(self):
        print(self.id)
        print(self.name)
        print(self.age)
x= int(input('Enter the no of persons are there'))
for i in range(x):
    person.id = person.id + 1
    name = input('Enter the name:')
    age = int(input('Enter the person age:'))
    p = person(id,name,age)
    p.display()

