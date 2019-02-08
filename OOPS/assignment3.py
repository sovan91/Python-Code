from OOPS.Address import address
from OOPS.Person import person
list= []
n = int(input('Enter the number of size:'))
for i in range(n):
    id = int(input('Enter the id:'))
    name = input('Enetr the name:')
    age = input("enter age");
    p = person(id, name, age)
    hno = int(input('Enter hno:'))
    city = input('Enter the city:')
    state = input('Enter the state:')
    pin = int(input('Enter the pin'))
    country = input('Enter the country')
    street = input('Enter the street')

    if i == 4 :
        s = person(id, name, age)
        a = address(hno, city, state, pin, country, street)
        list.append(s)
        list.append(a)
for x in list:
 x.display()
 x.showAddress()