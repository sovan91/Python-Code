class Department:
    def __init__(self, id, name, emplist):
        self.id = id
        self.name = name
        self.emplist = emplist

    def display(self):
        print(self.id)
        print(self.name)
        for x in self.emplist:
            print(x.name)
