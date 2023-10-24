s=input('Enter sentence: ')
d={}
sum=0
words=s.split()
for i in words:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1    
for i in d.values():
    sum+=i
print('Number of words: ',sum)
# Hello there I am a python programmer