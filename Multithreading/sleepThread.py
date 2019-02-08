from  threading import Thread
import time
#default structure of thread class
class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name
        print('thread create')
    def run(self):
        print('running thread',self.name)
        time.sleep(6)
        print('running thread', self.name)
#create a thread************
th1 = MyThread('th1')
th2 = MyThread('th2')
th3 = MyThread('th3')
# ready state will create start function
th1.start()
th2.start()
th3.start()
# order by join function****************
th1.join()
th2.join()
th3.join()
print("bye bye")

