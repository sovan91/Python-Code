def validation(id,age):
    id = int(input('enter user id:'))
    age = int(input('enter user age:'))
    if id < 0 or age < 18:
        print('id and age must be vallid')
def id(id):
    print('user id:',id)
def age(age):
    print('user age:',age)
print(validation(id,age))