x =int(input('Enter the 1st no:'))
y = int(input('Enter the 2nd no:'))
list = []
def comaprison():
    if x > y :
        print('greaterno is:',x)
        print('smaller no is:',y)
     
    else:
        print('greater no is:',y)
        print('smaller no is:',x)
    list.append(y)
    print(list)
comaprison()