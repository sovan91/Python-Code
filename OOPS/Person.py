class person:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def display(self):
        print('Person id is:',self.id)
        print('Person name is:',self.name)
        print('Person age is:',self.age)
