#User input with the help of class , if user enter 3  then take id and name 3 time and display them.
class Student():
    def __init__(self, name,id):
          self.name = name
          self.id = id

    def display(self):
        print("Name of the student is:", self.name)
        print("Roll of the student is:", self.id)
s=Student('','')
list = []
n = int(input('Enter the number of input:'))
for i in range(n):
    id = int(input('Enter the id:'))
    name = input('Enetr the name:')
    s = Student(id,name)
    list.append(s)
for x in list:
 x.display()