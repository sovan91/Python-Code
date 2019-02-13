# Example 3
def myGen(size):
    n = 1
    while n<=size :
        yield n
        n+=1
for item in myGen(5):
    print(item)
for item in myGen(7):
    print(item)