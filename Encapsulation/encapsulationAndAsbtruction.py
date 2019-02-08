class Person:
    def __init__(self,pId,pName,pAge,pPan):
        self.__id = pId
        self.__name = pName
        self.__age = pAge
        self.__pan = pPan

    def display(self):
        print(self.pId,"\t",self.pName,"\t",self.pAge,"\t",self.pPan)
    #def __set_name__(self, name):
















def start():
    myObj = Person(12000,"sovan",34,"mytestpan")
    print(myObj)
    myObj.setName("shyam")
    myObj.setId(2989)
    print(myObj.getName())
    print(myObj)
if__name__ = '__main__'
start()