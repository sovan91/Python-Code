class Test:
    def __init__(self):
        self.a=1000
        self.b=2000
    def m1(self):
        self.c=3000
        self.d=4000
t=Test()
t.m1()
t.a=8888
t.b=9999
t.c=7777
print(t.__dict__)