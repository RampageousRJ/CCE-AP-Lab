f = open('inp.txt','r')
words=[]
count=0
for line in f.readlines():
    line=line.strip('\n')
    word = line.split(' ')
    for w in word:
        words.append(w)
for word in words:
    if word=='the':
        count+=1
print('Occurances: ',count)