import emp,pickle
f=open("emp.dat","wb")
n=int(input("Enter the number of employee:"))
for i in range(n):
    eno=int(input("Enter the employee number"))
    ename=input("Enter the employee name")
    esal=float(input("Enter the employee salary"))
    eaddr=input("Enter the employee address")
    e=emp.employeee(eno,ename,esal,eaddr)
    pickle.dump(e,f)