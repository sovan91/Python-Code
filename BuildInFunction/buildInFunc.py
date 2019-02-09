#any function
myCondition = [True,True,True,True]
if(any(myCondition)):
    print('procced')
else:
    print('stop')


# all function
if(all(myCondition)):
    print('procced')
else:
    print('stop')


# chr function returns for unicode
print(chr(120))

# ord function will returns convert character to unicode
print(ord('x'))


print(format(25,'%')) # input and format
print(format(25,'b'))
# formats

# len function returns length of the string
print(len(myCondition))

#isInstance will return true or false
print(isinstance(12,int))

print(type(12))
