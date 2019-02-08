class ComplexNumber:
    def __init__(self,r=0,i=0):
        self.real=r
        self.imag=i
    def getData(self):
        print("{0} + {1}j".format(self.real,self.imag))
c=ComplexNumber(2,3)
c.getData()
c1=ComplexNumber(5)
c1.getData()
c1.attr=10
print(c1.real+c1.imag,c1.attr)
