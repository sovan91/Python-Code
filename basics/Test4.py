'''
Created on Jan 15, 2019

@author: SOVAN
'''
class Student:
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setMarks(self, marks):
        self.marks = marks
    def getMarks(self):
        return self.marks
n = int(input('Enter number student: '))
for i in range(n):
    name = input('Enter student name : ')
    marks = int(input('Enter student marks : '))
    s=Student()
    s.setName(name)
    s.setMarks(marks)
    print('Hi', s.getName())
    print('Your marks are: ', s.getMarks())