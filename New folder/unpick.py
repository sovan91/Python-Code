import emp,pickle
f=open("emp.dat","rb")
print("Employee details is.....")
while True:
    try:
        obj=pickle.load(f)
        obj.display()
        print()
    except EOFError:
        print("All employee details")
        break
f.close()