'''
Created on Jan 17, 2019

@author: SOVAN
'''
#example1
'''for i in range(10):
    print(i)'''
#example 2
# x= int(input('enter the number:'))
# for i in range(2,x+1,2):
#    
#         print(i)
#example3 take num as input and perform the sum

x = int(input('enter the number'))
sum = 0
for i in range(x):
    num = int(input('enter number:'+ str(i+1)))
    sum = sum + num
print(sum)
