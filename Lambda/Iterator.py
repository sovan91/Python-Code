# list = [100,200,300,400]
# # for i in list:
# #     print(i)
# #iteration method
# itr = iter(list)
# print(next(itr))
# print(next(itr))
# print(next(itr))
# print(itr.__next__())
#
#
# how to create own iterator

# create a class
# provide a constructor __init__
# provide __iter()
# priovide __next__()

class MyIterator:
    def __init__(self,num):
        self.num = num
    def __iter__(self):
        self.n = 1 # counter n
        return self
    def __next__(self):
        if self.n < self.num :
            res = self.n * self.n
            self.n = self.n + 1
            return res
        else:
            raise StopIteration
obj = MyIterator(10)

for i in iter(obj):
    print(i)