#for file read operation by user input utile user put bye
# f = open('test.txt','w')
# str = ''
# while str!= 'bye':
#     str =input('Enter the string:')
#     f.write(str)
# f.close()


# file append operation

f = open('test.txt','a')
str = ''
while str != 'bye':
    str = input('Enter str:')
    f.write(str)
f.close()
