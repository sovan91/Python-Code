def division(x,y):
    if y==0:
        print('we cant divide by zero')
        return x/y
num1 = int(input('enter the first number:'))
num2 = int(input('enter the second number:'))
print(division(num1, num2))