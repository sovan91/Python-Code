class Student:
    def __init__(self,id,name):
        self.id = int(input('enter the id:'))
        self.name = input('enter the name:')
    def display(self):
            print('name of the student id  is:',self.id)
            print('name is:',self.name)
n = int(input('Enter the number of input:'))
for i in range(n):
            id = int(input('Enter the id:'))
            name = input('Enter the name:')
s = Student(id,name)
s.display()