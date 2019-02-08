from threading import Thread
import time
class MyThread(Thread):
    def __init__(self,x,y,op):
        Thread.__init__(self)
        self.x = x
        self.y = y
        self.op = op

    def sum1(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y
    def mul(self):
        return self.x * self.y
    def division(self):
        return self.x / self.y
    def run(self):
        if self.op == 1:
           print('addition of two:',self.sum1())
        if self.op == 2 :
           print('Subtraction of two:', self.sub())
        if self.op == 3 :
           print('Multiplication of two:', self.mul())
        if self.op == 4:
           print('Division of two:', self.division())


num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))

t1 = MyThread(num1,num2,1)
t2 = MyThread(num1, num2,2)
t3 = MyThread(num1, num2,3)
t4 = MyThread(num1,num2,4)

t1.start()
t2.start()
t3.start()
t4.start()
