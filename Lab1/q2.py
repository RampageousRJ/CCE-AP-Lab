k=1
n=int(input('Enter number of levels: '))
for i in range(n):
    for j in range(i+1):
        print(k,end='\t')
        k=k+1
    print('\n')