def sum():
    x = int(input('enter the size of the list:'))
    list=[]
    for i in range(x):
      name = str(input('enter the name:'))
      list.insert(i,name)
    print(list)

sum()