#self is reffering to the object under execution
class person:
    def __init__(self,id,name,age,adhar):
        #__init__ is default constructor
        self.id = id
        self.name = name
        self.age = age
        self.adhar = adhar

    def __init__(self):
            # __init__ is default constructor
            self.id = 0
            self.name = ''
            self.age = 0
            self.adhar =''
p = person(1,'sovan',29,98765432)
print(p)
#class is the way to define in the entity
# self is the only current object
#as may as the object are created is available , not delete or destroy
#inside the constructor initializations are happen
#how to set the data for object
p = person()
p.id = 1
p.name = 'sovan'
p.age = 27
p.adhar = 98765432
print(p.id)
print(p.name)
print(p.age)
print(p.adhar)
p1=person(12002,'deep',34,8976567)
print(p1.id)
print(p1.name)
print(p1.age)
print(p1.adhar)
#