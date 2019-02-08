def div(n1,n2):
    if n2 == 0 :
        raise ArithmeticError("num2 can't be zero")
    print(n1/n2)
try:
  div(5,0)
except ArithmeticError as obj :
    print('Invalid input due to', obj)
print('bye bye')