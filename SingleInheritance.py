# Single Inheritance Example
class person:
    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
    def showPersonInfo(self):
        print(self.id)
        print(self.name)
        print(self.age)
#child class declarartion
class emplyoee(person):
    def __init__(self, id, name, age, pfno, mbenefits):
        person.__init__(self, id, name, age)
        self.pfno = pfno
        self.mbenefits = mbenefits
    def showEmpInfo(self):
        print(self.pfno)
        print(self.mbenefits)
#Multi level example
class staff(emplyoee):
    def __init__(self, id,name, age,pfno,mbenefits, contactid, contactperson):

        #person.__init__(self, id, name, age)
        emplyoee.__init__(self, id, name, age,pfno, mbenefits)
        self.contactid = contactid
        self.contactperson = contactperson
    def showStaff(self):
        print(self.contactid)
        print(self.contactperson)

p1 = person(1,"sovan",27)
e1 = emplyoee(101,"Sovan Chakrabarty",28, 'yes','yes')
s1 = staff(1001,"Mamata Banerjee",65,'yes','yes',986543210,"Sovan")
#single inheritance method call
p1.showPersonInfo()
e1.showPersonInfo()
e1.showEmpInfo()
#multi-level inheritance method call
s1.showPersonInfo()
s1.showEmpInfo()
s1.showStaff()

