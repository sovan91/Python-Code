# Generator : It is a simplified version of your Iterators
#Example 1
# Generator is function and it is maintain the state.
# it will return different value for every call.
# It has no return function , it has yield function
# based on the call the value will change
#how to create: step 1 -
# step 2 create object for gen
#
def MyGen():
    x =1
    yield x
    x = 10
    yield x
    x=50
    yield x
# genObj = MyGen()
# print(next(genObj))
# print(next(genObj))
# print(next(genObj))


# Example 2
for item in MyGen():
    print(item)