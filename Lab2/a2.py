def union(l1,l2):
    l=list(set(l1))
    t=list(set(l2))
    for i in t:
        if i not in l:
            l.append(i)
    return l

def intersect(l1,l2):
    l=list(set(l1))
    t=list(set(l2))
    ans=[]
    for i in t:
        if i in l:
            ans.append(i)
    return ans

def diff(l1,l2):
    l=list(set(l1))
    t=list(set(l2))
    for i in t:
        if i in l:
            l.remove(i)
    return l
            

if __name__=='__main__':
    l1=[]
    n=int(input('Enter l1 length: '))
    print("Enter l1 values: ")
    for i in range(n):
        val=int(input())
        l1.append(val)
    print()
    l2=[]
    n=int(input('Enter l2 length: '))
    print("Enter l2 values: ")
    for i in range(n):
        val=int(input())
        l2.append(val)
    ch=int(input('\n\nMENU\n1.Union\n2.Intersection\n3.Difference\nEnter choice:'))
    if(ch==1):
        print('Union: ',union(l1,l2))
    elif(ch==2):
        print('Intersection: ',intersect(l1,l2))
    elif(ch==3):
        print('Difference: ',diff(l1,l2))
    else:
        print("INVALID")