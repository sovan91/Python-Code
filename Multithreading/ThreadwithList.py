from threading import Thread
import time
class MyThread(Thread):
    def __init__(self, name, list):
        Thread.__init__(self)
        self.name = name
        self.list = list
    def run(self):
        time.sleep(4)
        for i in self.list:
            i.join()
        print(self.name)

t2 = MyThread('t2', [])
t3 = MyThread('t3', [])
t1 = MyThread('t1',[t2,t3])


t1.start()
t3.start()
t2.start()