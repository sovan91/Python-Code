# upper case using generator
def changeUpper(str):
    length = len(str)
    for i in str:
        yield i.upper()
for ch in changeUpper("India"):
    print(ch)
for ch in changeUpper("bangalore karnataka india"):
    print(ch)
