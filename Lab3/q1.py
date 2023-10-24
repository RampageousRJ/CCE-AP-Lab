def multList(l1):
    prod=1
    for i in l1:
        prod*=i
    return prod
    
n = int(input("Enter number of list elements: "))
print('Enter list elements: ')
l1=[]
for i in range(n):
    l1.append(int(input()))

print("Product: ",multList(l1))