class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display(self):
        print("Student name is:",self.name)
        print("Student roll is:",self.roll)
        print("Student marks:",self.marks)

std=Student('sovan',1,100)
std.x=1000
std.display()
print(std.__dict__)