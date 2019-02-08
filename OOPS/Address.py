class address:
    def __init__(self,hno,city, state, pin, country,street):
        self.hno  = hno
        self.city = city
        self.state = state
        self.pin = pin
        self.country  =country
        self.street = street
    def showAddress(self):
        print("House no is:",self.hno)
        print("City is:", self.city)
        print("state is:", self.state)
        print("pin no is:", self.pin)
        print("country no is:", self.country)
        print("Street no is:", self.street)

