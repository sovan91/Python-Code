#write from the list
# f = open('test2.txt','w')
# list = ['hi','python','programming']
# f.writelines(list)
# f.close()


#logic for delete a file

import os
if os.path.exists('test2.txt'):
    os.remove('test2.txt')
    print('file is deleted')
else:
    print('file doesnot exist')
