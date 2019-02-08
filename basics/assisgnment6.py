'''
Created on Jan 16, 2019

@author: SOVAN
'''
bank = ['icici','hdfc','sbi','city']
x = input('Enter required bank:')
if x == bank[0]:
    print('User enter icici bank and rate is 10%')
elif x == bank[1]:
    print('User enter nank is hdfc and rate of interest is 11%')
elif x == bank[2]:
    print('user enter bank is sbi and rate of interest is 12%')
elif x == bank[3]:
    print('User enter bank is city and rate of interest is 13%')
else:
    print('User enter bank is not listed and please try again...')