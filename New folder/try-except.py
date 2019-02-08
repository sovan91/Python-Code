import pickle
class employeee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def display(self):
        print(self.eno,"\t",self.ename,"\t",self.esal,"\t",self.eaddr)
with open("emp.dat","wb") as f:
    e=employeee(100,'Sovan',1000,'kolkata')
    pickle.dump(e,f)
    print("pickling of employee object completed...")

with open("emp.dat","rb") as f:
    obj=pickle.load(f)
    print("Employeee information after unpickling...")
    obj.display()