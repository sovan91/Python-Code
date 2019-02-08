# How many times try except finally and else block will work
x = int(input('Enter the number:'))
def sumation():
    global x
    try:
        try:
          if x %2 == 0 :
            print('Even number')
            print('priiii')
          else:
            print('odd number')
        except IndexError:
            print('Invalid error')
        finally:
            print('This is final block')
        print('Global code')
    except ZeroDivisionError:
        print('Zero division error')
    finally:
        print('Outer global finaaly block')
    print('outer block')
sumation()

