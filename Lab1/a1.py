a = int(input('Enter lower limit: '))
b = int(input('Enter upper limit: '))
l1=[]
for i in range(a,b+1):
    flag=False
    for j in range(2,i):
        if i%j==0:
            flag=True
    if not flag:
        l1.append(i)
print(l1)