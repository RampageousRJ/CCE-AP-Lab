num=int(input(('Enter number: ')))
sum,temp=0,num
while(num>0):
    dig=num%10
    sum=sum+(dig**3)
    num=num//10
if sum==temp:
    print('Armstrong')
else:
    print('Not armstrong')