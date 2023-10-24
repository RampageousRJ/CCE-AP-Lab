n=int(input('Enter number of strings: '))
k=0
l=[]
for i in range(n):
    s=input()
    l.append(s)
    if s[0]==s[-1] and len(s)>=2:
        k=k+1
print('Number of satisfactory strings: ',k)
print()
print('Strings with odd length: ',end='')
for i in l:
    if len(i)%2==1:
        print(i,end='  ')