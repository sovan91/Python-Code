# import os
# print(os.listdir())
# os.mkdir('test4')
# os.rename('test4','test6')
# os.rmdir('test6')
# print(os.listdir('c://'))
# isFile = os.path.isfile('ex1.py')
# print(isFile)
# isDir = os.path.isdir('test')
#
# print(isDir)
#

import os
print(os.getcwd())
os.chdir('c://test')
print(os.getcwd())
for f in os.listdir():
    print(f)
    print(os.path.isfile(f))


