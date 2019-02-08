class Test:
    a=10
    def __init__(self):
        self.b=20
        Test.c=30
    def m1(self):
        self.e=40
        Test.f=50
    @classmethod
    def m2(cls):
        cls.g=60
        Test.h=70
    @staticmethod
    def m3():
        Test.i=80
t=Test()
t.m1()
Test.m2()
Test.m3()
Test.j=90
print(t.a,t.b)
print(Test.a,t.b)
print(Test.__dict__)