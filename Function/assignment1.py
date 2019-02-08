def validation():
    id = int(input('Enter user id:'))
    age = int(input('Enter user age:'))
    if id < 0 or age < 18 :
        print('Enter id and age must be required type...')
    else:
        print('enter user id  is:',id)
        print('enter user age is:',age)
validation()