def matSum():
    m1 = int(input('Enter rows for M1: '))
    n1 = int(input('Enter columns for M1: '))
    m2 = int(input('Enter rows for M2: '))
    n2 = int(input('Enter columns for M2: '))
    if m1!=m2 or n1!=n2:
        print('Not possible!')
        return
    d1={}
    d2={}
    print('Enter first matrix: ')
    for i in range(m1):
        l1=[]
        for j in range(n1):
            l1.append(int(input()))
        d1[i]=l1
    print('\nEnter second matrix: ')
    for i in range(m2):
        l1=[]
        for j in range(n2):
            l1.append(int(input()))
        d2[i]=l1
    for i in range(len(d1)):
        l1=d1[i]
        l2=d2[i]
        for j in range(len(l1)):
            l1[j]+=l2[j]
    print('\n\n')
    for i in d1.values():
        for j in i:
            print(j,end='\t')
        print('\n')

matSum()