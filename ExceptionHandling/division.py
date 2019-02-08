class Exception:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def div(self):
        if self.y == 0:
            print('second number cant zero. It will show error')
        else:
          print('Division of two number is:',self.x/self.y)
num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))

e = Exception(num1,num2)
e.div()
