from threading import *
import time
x = int(input('Enter the no thread'))
class MyThread(Thread):
    def __init__(self,amount):
        Thread.__init__(self)
        self.amount = amount
    def run(self):
        global x
        #time.sleep(3)
       # threadLock.accure()
        for input in x :
           input = input + self.amount
        #time.sleep(1)






#threadLock = threading.Lock()
t1 = MyThread(input)
t2 = MyThread(input)
t3 = MyThread(input)
t1.start()
t2.start()
t3.start()
