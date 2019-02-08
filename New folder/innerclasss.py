class Employee:
    #constructor function declaration
    def __init__(self,eno,ename,esal):
        self.eno=eno
        self.ename=ename
        self.esal=esal
    #instance method
    def display(self):
        print("Employee number is:",self.eno)
        print("Employee name is:",self.ename)
        print("Employee salary is:",self.esal)
class Test:
    #static method
    def modify(emp):
        emp.esal=emp.esal+10000
        emp.display()
#object creation for function calling
e=Employee(1001,'Sovan',70000)
Test.modify(e)
