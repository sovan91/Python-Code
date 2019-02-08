from OOPScomposition.address import Address
from OOPScomposition.person import person

hno = int(input('Enter the house no:'))
city = input('Enter the city:')
state = input('Enter the state:')
pin = int(input('Enter the pin:'))
country = input('Enter the country name:')
street = input('Enter the street number:')
paddr = Address(hno, city, state, pin, country, street)

print(person.paddr.showAddress())
#   person.paddr.display()