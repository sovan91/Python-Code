class SE:
    def __init__(self,name,age,tech):
        self.name=name
        self.age=age
        self.tech=tech
s1=SE('Sovan',27,'Python')
s2=SE('Krish',25,'Java')
s1.gf='Sunny'
s1.brand='Royal Stag'
print(s1.__dict__)
print(s2.__dict__)
del s1.brand
print(s1.__dict__)