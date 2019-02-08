import os
try:
    f = open('text.txt', 'w')
    str = input('Enter the string')

except FileNotFoundError:
    if os.path.exists('text.txt'):
        os.remove('text.txt')
        print('file is deleted')
else:
    print('file doesnot exist')
finally:
   print(f.write(str))
f.close()