from  threading import Thread
import time
class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name
       # print("Thread created...")
    def run(self):
        #print("Thread is runnning:", self.name)
        time.sleep(4)
        #print("Thread is running", self.name)
        if self.name == 't1':
            time.sleep(4)
        print("thread close", self.name)
t1 = MyThread('t1')
t2 = MyThread('t2')
t3 = MyThread('t3')
t1.start()
t3.start()
t2.start()


