total = 0
while total < 100 :
    num = int(input('enter no:'))
    if (num < 0) :
        continue
    #total = total + num
#print(total)  
    if (num == 999) :
        break
    total = total + num 
print(total)