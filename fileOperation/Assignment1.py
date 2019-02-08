# f = open('text.txt','w')
# str = ''
# while str !='end':
#     str = input('Enter the string:')
#     f.write(str)
# f.close()
f = open('text.txt','w')
str = input('Enter the string')
for i in str :
    f.write(i)
f.close()