l1=[]
n=int(input('Enter number of elements in list1: '))
print('Enter elements: ',end='')
for i in range(n):
    num = int(input())
    l1.append(num)
l2=[]
n=int(input('\nEnter number of elements in list2: '))
print('Enter elements: ',end='')
for i in range(n):
    num = int(input())
    l2.append(num)
print('\n',l1,'\n',l2)
merged=[]
print('Merged List: ')
for i in l1:
    if i%2==1:
        merged.append(i)
for i in l2:
    if i%2==0:
        merged.append(i)
print(merged)