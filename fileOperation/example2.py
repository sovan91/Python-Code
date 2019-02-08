#how to read a data from file

f = open('test.txt','r')
f.read()
#it will read all the lines of the file()
f.read(5)
#it read first 5 character

f.readline(); # it will read the first line----by default
f.readline(); # it will read thye second line

f.readline(10); # it will read 10 characters of that line
#if 1st line contain only 5 character it will throws exception

f.readlines() # this will returns list of string

