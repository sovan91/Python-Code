def div(n1,n2):
    if n2 == 0 :
        raise ArithmeticError("num2 can't be zero")
    print(n1/n2)
div(5,0)