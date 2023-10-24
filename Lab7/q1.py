f = open('inp.txt','r')
lines = f.readlines()
print('Lines: ',len(lines))
words=0
char=0
for line in lines:
    line=line.strip('\n')
    word = line.split(' ')
    char+=len(line)
    words+=len(word)
print("Words: ",words)
print("Characters: ",char)