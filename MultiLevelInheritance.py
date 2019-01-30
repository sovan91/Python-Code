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
class staff(emplyoee):
    def __init__(self, id,name, age,pfno,mbenefits, contactid, contactperson):

        #person.__init__(self, id, name, age)
        emplyoee.__init__(self, id, name, age,pfno, mbenefits)
        self.contactid = contactid
        self.contactperson = contactperson
    def showStaff(self):
        print(self.contactid)
        print(self.contactperson)
        self.showEmpInfo()
        self.showPersonInfo()

p= person(1,"deep",27)
e= emplyoee(101,'sovanchakrabarty',27,'pf/2345','yes')
s = staff(1001,"Mamata Banerjee",65,'yes','yes',986543210,"Sovan")
s.showStaff()

# special thanks to murli
