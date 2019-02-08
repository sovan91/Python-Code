class Input():
    def __init__(self, fname, lname, password, email, phone, city ):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.phone = phone
        self.city = city
        self.password = password

    def display(self):
        print(self.fname)
        print(self.lname)
        print(self.email)
        print(self.phone)
        print(self.city)
        print(self.password)





