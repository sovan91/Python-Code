def sumation():
    x = int(input('Enter the no:'))
    list = []
    sum = 0
    for i in range(x):
        num = int(input('Enter the number:'))
        list.append(num)
      #  sum = sum + num
    for n in list:
        sum = sum + n
    print(list)
    print(sum)
sumation()