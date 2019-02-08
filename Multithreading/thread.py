from  threading import Thread
#default structure of thread class
class MyThread(Thread):
    def __init__(self,name):
        Thread.__init__(self)
        self.name = name
        print('thread create')
    #override the run method which is in python provided
    # every logic will write inside run function
    def run(self):
        print('running thread',self.name)
#create a thread
th1 = MyThread('th1')
th2 = MyThread('th2')
th3 = MyThread('th3')
# ready state will create start function
th1.start()
th2.start()
th3.start()

