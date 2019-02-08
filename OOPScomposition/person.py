class person:
    def __init__(self,pid, pan, adhar,paddr ):
        self.pid = pid
        self.pan = pan
        self.adhar = adhar
        self.paddr = paddr

    def display(self):
        print(self.pid)
        print(self.pan)
        print(self.adhar)
        print(self.paddr)
p=person('','','','')
pid = int(input('Enter the pid:'))
pan = int(input('Enter the pan no:'))
adhar = int(input('Enter the adhar no:'))
