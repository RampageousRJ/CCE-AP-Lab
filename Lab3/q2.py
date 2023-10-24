def uniq(l1):
    l2=[]
    for i in l1:
        if(i not in l2):
            l2.append(i)
    return l2

n = int(input("Enter number of list elements: "))
print('Enter list elements: ')
l1=[]
for i in range(n):
    l1.append(int(input()))
    
print('Unique Values: ',uniq(l1))