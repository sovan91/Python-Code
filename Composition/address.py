from Composition.person import person, student
class address:
    def __init__(self,hno,city,state,country,pin,street):
        self.hno = hno
        self.city = city
        self.state = state
        self.country = country
        self.pin = pin
        self.street = street
    def show(self):
        print(self.hno)
        print(self.city)
        print(self.state)
        print(self.country)
        print(self.pin)
        print(self.street)
presentAddr = address(hno=101,city='kolkata',state='west bengal',country='india',pin=700084,street='tentulberia anukul high school road')
permanentAddr = address(hno='11/2',city='contai',state='west bengal',country='india',pin=721425,street='madhakhgali road')
p = person(pid=1,name='sovan',age=28)
s = student(stdId=1001,name='deep chakrabarty',roll=234,pan='pand324',adhar=98708765432)
p.display()

presentAddr.show()
permanentAddr.show()
print("************End of Person details*****************")
s.showStd()
presentAddr.show()
permanentAddr.show()