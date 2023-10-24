import sys
f=open(sys.argv[1],'r')
lines = f.readlines()
lines=lines[::-1]
f.close()

f = open(sys.argv[1],'w')
for line in lines:
    f.write(line)
f.close()
