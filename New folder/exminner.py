class Person:
    def __init__(self):
        self.name="Sovandev Chakrabarty"
        self.dob=self.DOB()
    def display(self):
        print("The person name is:-",self.name)
        self.dob.display()
    class DOB:
        def __init__(self):
            self.dd=22
            self.mm=2
            self.yyyy=1991
        def display(self):
            print('DOB is :- {}/{}/{}'.format(self.dd,self.mm,self.yyyy))
p=Person()
p.display()