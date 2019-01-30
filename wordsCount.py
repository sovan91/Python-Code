list = ['sap','java','mac','windows','c','c++','java','sap']
d ={}
for words in list:
    d[words] = d.get(words,0) + 1
sorted(d.items(), key=lambda x : x[1], reverse=True )
print(d)
