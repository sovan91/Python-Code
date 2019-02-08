#inner class problem...how to call inner class and method declaration in ineer class
class Student:
    def __init__(self):
        self.name='Sovan'
        self.age=27
        self.dob=self.DOB()
    def display(self):
        print("Student name is:",self.name)
        print("Student age is:",self.age)
        self.dob.display()
    class DOB:
        def __init__(self):
            self.dd=22
            self.mm=2
            self.yyyy=1991
        def display(self):
            print('Student dob is',"{}/{}/{}".format(self.dd,self.mm,self.yyyy))
s=Student()
s.display()