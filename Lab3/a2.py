def pascalTriangle(n):
    if n==1:
        l=[[1]]
        print(l)
        return
    l=[[1],[1,1]]
    for i in range(n-2):
        l1=[]
        l1.append(1)
        temp = l[len(l)-1]
        for i in range(0,len(temp)-1):
            l1.append(temp[i]+temp[i+1])
        l1.append(1)
        l.append(l1)
    for i in l:
        for j in i:
            print(j,end=" ")
        print()

a=int(input('Enter number of levels: '))
pascalTriangle(a)