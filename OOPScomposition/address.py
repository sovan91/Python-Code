class Address:
    def __init__(self,hno,city,state,pin,country,street):
        self.hno = int(input('Enter the house no:'))
        self.city = input('Enter the city:')
        self.state = input('Enter the state:')
        self.pin = int(input('Enter the pin:'))
        self.country = input('Enter the country name:')
        self.street = input('Enter the street number:')
    def showAddress(self):
        print(self.hno)
        print(self.city)
        print(self.state)
        print(self.pin)
        print(self.country)
        print(self.street)

