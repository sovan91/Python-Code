id = 0
class person:
    count = 6000
    def __init__(self,name,age):
        self.id = person.count
        person.count= person.count+1
        self.name = name
        self.age = age

    def display(self):
        print(self.id)
        print(self.name)
        print(self.age)

p = person("usre2",67)
p.display()

p = person("usre1",89)
p.display()

