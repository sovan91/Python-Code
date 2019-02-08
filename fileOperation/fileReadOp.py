f = open('test.txt','r')
#print(f.read())
#print(f.read(5))#it will return foirst 5 charcter
#print(f.readline())
#print(f.readlines())
for line in f.readlines():
    print(line)
f.close()
