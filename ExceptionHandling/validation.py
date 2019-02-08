from ExceptionHandling.Input import Input
class valid:
    def __init__(self):
      Input.__init__()
        #self.display()
    def validate(self,fname,lname,email, phone, city, password):

        if self.fname < 0 :
            print("first name can't be null")

        elif self.lname < 0 :
            print("last name can't be null")
        #example = "sovan.pbc@gmail.com"
        elif self.phone < 10 :
            print('phone number must 10 digit')
        elif self.password >8 and self.password < 15 and self.password != '' :
            print('password is validate')
        elif self.city == ['chennai','hyderabad','bangalore']:
            print('valid city')
        else:
            print('invalid city')
fname = input('Enter the first name:')
lname = input('Enter the second name:')
email = input('Enter the email:')
password = input('Enter the password:')
phone = int(input('enter the phone number:'))
city = input('Enter the city:')
i = Input(fname,lname,city,password,phone,email)
i.display()
#i.valid()