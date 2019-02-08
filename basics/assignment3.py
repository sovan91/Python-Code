'''
Created on Jan 16, 2019

@author: SOVAN
'''
age = int(input('Enter user age:'))
user_id = int(input('Enter user id:'))
# if user_id < 0 :
#     print('User id cannot be negative and please enter positive id')
# else:
#     if age > 18 :
#         print('Entered user age is valiod and go through')
#     else:
#         print('Entered user age is below 18 and dont proceed')
#     


if user_id < 0 :
    print('User id cannot be negative and please enter positive id')
elif age < 18 :
        print('Entered user age is invalid and go through')
else:
        print('valid id and age')
    