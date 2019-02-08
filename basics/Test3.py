'''
Created on Jan 14, 2019

@author: SOVAN
'''

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self):
        print('Hi:', self.name)
        print('Marks is:', self.marks)
    def grade(self):
        if self.marks >= 60 :
            print('First Class')
        elif self.marks >= 50 :
            print('Second class')
        elif self.marks >= 40 :
            print('Third class')
        else:
            print('You are not passed the exam:')
n=int(input('Enter number of student:-'))
for i in range(n):
    name = input('Enter the name of the student:-')
    marks = int(input('Enter the marks of the student:-'))
    s=Student(name, marks)
    s.display()
    s.grade()
    print('*'*20)
