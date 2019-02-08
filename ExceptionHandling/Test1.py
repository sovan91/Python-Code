arr = [1,2,3,4,5]
def square():
    intNum = 0
    try:
        intNum = int(4)
        print(arr[2])
        print(1/1)
        #based on requirement only one error message will show
    except (ValueError,IndexError,ArithmeticError) as obj :
       print('Error argument', obj)
    #except IndexError:
       # print('IndexError ....')
    #except ArithmeticError:
       # print('Arithmetic error invalid argument')
    else:
        print('No exception')
square()