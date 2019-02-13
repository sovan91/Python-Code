def welMsg(fun):
    def greet(str):
        return "hi user"+fun(str)
    return greet
@welMsg
def myFun(str2):
    return "my profile: "+str2
print(myFun("sovan"))

@welMsg
def myFun2(str2):
    return "My setting: "+str2
print(myFun2("deep"))

# calculation check both should not negative
#outer fun return innr func
#outer
