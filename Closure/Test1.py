# The function we create an object


def show():
    return "hi"
f1 = show()
print(f1)

# Example 2

def show1(txt):
    return "hello" + txt
f = show1
print(f("user1"))
print(f("yuser2"))

# example 3
def fun1(x):
    def fun2(y):
        return x+y
    return fun2

# call
fobj1 = fun1(10)
print(fobj1(20))

# closure is mostly function object
# nested funcction is also a closure but when inner function call we should