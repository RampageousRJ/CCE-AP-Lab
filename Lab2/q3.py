import random
import string

d={}
def search(target):
    for i in d.values():
        if i==target:
            print("Found")
            return
    print('Not found')

n = int(input("Enter number of values: "))
print('Enter values: ')
sum=0
tot=0
res=""
for i in range(n):
    k=random.randint(0,99)
    d[k]=input()
    try:
        d[k]=int(d[k])
        sum+=d[k]
        tot+=1
    except:
        res+=d[k]
print('\nDictionary = ',d)
if sum>0:
    print('\nAverage of integers = ',sum/tot)
if len(res)>0:
    print('\nConcatenated string = ',res)
    
target = input('\nEnter value to find: ')
search(target)

print("\nSpecial Strings: ",end='')
for i in d.values():
    if type(i)==str:
        flag=True
        for j in i:
            if j in string.ascii_letters or j in string.hexdigits:
                flag=False
                break
        if flag:
            print(i,end='')