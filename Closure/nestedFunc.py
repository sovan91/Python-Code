# #nested function
# def f1():
#     print("hello")
#     def f2():
#         print("hello2")
#     f2()
# f1()
#closure example
num= 1
def myFun(str):
    def myFun2():
        print(str,num)
    return myFun2

obj = myFun("hello")
obj()
obj()