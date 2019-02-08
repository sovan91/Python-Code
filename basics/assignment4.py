'''
Created on Jan 16, 2019

@author: SOVAN
'''
bankname = input('Enter the bank name:')

if bankname == 'icici' :
    print('User enter icici bank and rate of interest is:- 10%')
elif bankname == 'hdfc':
    print('User enter hdfc bank and rate of interest is :-  11%')
elif bankname == 'sbi':
    print('User enter sbi bank and rate of interest is:- 12%')
elif bankname == 'citi':
    print('User enter citi bank and rate of interest is:- 13%')
else:
    print('User entered bank is not listed and stop')