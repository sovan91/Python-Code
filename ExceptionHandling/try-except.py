''''a = [1,2,3]
try:
    print(a[1])
    print(a[3])
except IndexError:
    print('error occur')
print('bye bye')'''
# try except in division of two number
def div(a,b):
    try:
        c = a/b
    except ZeroDivisionError:
        print('zero division error')
    else:
        print(c)
    finally:
        print('Hi try-except-else block...im executing')
div(2,3) #try+else
div(3,0) # partial try + except
