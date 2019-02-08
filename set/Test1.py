mySet = {'User','sap','java','hana','sovan',1,'sovan'}
print(mySet)
#add a new element inside a set
mySet.add('java')
mySet.add('sap')
mySet.add('angular')
print(mySet)

#serach by content
res = 'sap' in mySet
print(res)
# intersection operation
mySet2= {'jquery','selinum','sap','java'}
print('mySet2=',mySet2)
mySet3 = mySet - mySet2
print(mySet3)
# reverse intersection

mySet4= mySet2- mySet
print(mySet4)

#union operation for addition
mySet5 =mySet|mySet2
print(mySet5)
#semetric difference common difference
mySet6 = mySet^mySet2
print(mySet6)
#to delete method for clear the element

#how to remove
#mySet2.remove('angular')
#print(mySet2)
#how to remove duplicate element in a list using set
list = ['user1','user2','user3','user4','user5','user2','user1','user4']
mySet7 = set(list)
print(mySet7)
