deets={}
k=0
try:
    file = open('sample.txt','r')
    for line in file:
        line=line[:len(line)-1]
        l1=[]
        l1.append(len(line))
        l1.append(line)
        deets[k]=l1
        k+=1
    file.close() 
except FileNotFoundError:
    print("File does not exist")
finally:
    print(deets)
    
freq={}
k=0
for l1 in deets.values():
    for char in l1[1]:
        if char not in freq.keys():
            freq[char]=1
        else:
            freq[char]+=1
print(freq)