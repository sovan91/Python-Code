class myData:
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
#to perform addtion , we have to create a function __add__(self, other).It is in build function
    def __add__(self, other):
        return myData(self.n1 + other.n1, self.n2 + other.n2)
# for subtraction operation
    def __sub__(self, other):
        return myData(self.n1 - other.n1, self.n2 - other.n2)
# str for string.


    def __str__(self):
        return "{0} {1}".format(self.n1,self.n2)

obj1 = myData(10,20)
obj2 = myData(20,40)
obj3 = obj1 + obj2
obj4 = obj1 - obj2
obj5 = 'sovan','deep'
print(obj3.n1)
print(obj3.n2)
print(obj4.n1)
print(obj4.n2)
print(obj5)