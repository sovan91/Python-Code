'''
Created on Jan 16, 2019

@author: SOVAN
'''
age = int(input('Enter user age:'))
if age > 18 :
    input_id = int(input('Enter user id:'))
    if input_id < 0 :
        print('Id cannot negative please entered positive id number')
    else:
        print('User id is positive and go to next step')
   # print('User age and id is matched')
else :
    print('User age is below 18....')