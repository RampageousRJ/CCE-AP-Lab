f = open('inp.txt','r')
lines = f.readlines()
print('Lines: ',len(lines))
words=[]
characters=0
for line in lines:
    line=line.strip('\n')
    for char in line:
        if char=='\n':
            break
        characters+=1
    word = line.split(' ')
    for w in word:
        words.append(w)
print("Words: ",len(words))
print("Characters: ",characters)