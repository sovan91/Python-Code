with open('test.txt','a') as f :
    f.write('writing prograaming')

with open('test.txt','r') as f : # syntex for auto file close
    for line in f.readlines():
        print(line)