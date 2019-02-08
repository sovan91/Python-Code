mylist = [12,'kumar',1234.567,'hane','aaa']
print(type(mylist))
#print the list element
print(mylist)
#Iterator output
for data in mylist:
    print("item=",data)
    
    #update the data
mylist[0] = 90
print(mylist[0])

#add new element
mylist.append('bangalore')
print(mylist)
#how to add first postion
mylist.insert(0, 'java')
print(mylist)

# delete operartion
del mylist[0]
print(mylist)

# remove method
mylist.remove(mylist[0])
print(mylist)

mylist.pop(2)
print(mylist)
print(len(mylist))

# search by content
res  = 'hane' in mylist
print(res)

#clear
mylist.clear()

# merge of two list :
mylist2 =['hane','hjava','hadoop','j2ee']
mylist.extend(mylist2)
m= mylist + mylist2
print(mylist)
print(m)