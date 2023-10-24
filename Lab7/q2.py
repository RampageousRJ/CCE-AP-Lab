f = open('inp.txt','r')
words={}
for line in f.readlines():
    line=line.strip('\n')
    word = line.split(' ')
    for w in word:
        if w in words.keys():
            words[w]+=1
        else:
            words[w]=1
print(words)