import threading
import time
amount =6000
class MyThread(threading.Thread):
    def __init__(self,name,withdraw):
        self.name = name
        self.withdraw = withdraw
    def run(self):
        global amount;
        time.sleep(3)
        threadLock.acquire()
        amount = amount - self.withdraw
        time.sleep(1)
        print(self.name,self.withdraw,amount)


threadLock = threading.Lock()
t1 = MyThread('a',2000)
t1.start()