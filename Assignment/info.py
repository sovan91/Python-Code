from Assignment.emp import Employee
from Assignment.dept import Department


p1= Employee(1,'sov')
p2 = Employee(2,'dep')
p3 = Employee(3,'shyam')
p4 = Employee(4,'madhu')
p5 = Employee(5,'joy')
p6 = Employee(6,'sony')
p7 =  Employee(7,'ankt')
p8 =  Employee(8,'dip')
p9 =  Employee(9,'hari')
p10 =  Employee(10,'sovan')
list1 = [p1,p2,p3]
list2 = [p4,p5,p6,p7,p8]
list3 = [p9,p10]
d1 = Department(1000,'hr',list1)
d2 = Department(2000,'it',list2)
d3 = Department(3000,'finance',list3)

d1.display()
d2.display()
d3.display()