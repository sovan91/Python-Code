from OOPS.Person import person
from OOPS.Address import address
id = input("enter id");
name = input("enter name");
age = input("enter age");
p= person(id,name,age)
hno = int(input('Enter hno:'))
city = input('Enter the city:')
state = input('Enter the state:')
pin = int(input('Enter the pin'))
country = input('Enter the country')
street = input('Enter the street')
addr =address(hno,city,state,pin,country,street)
p.display()
addr.showAddress()
