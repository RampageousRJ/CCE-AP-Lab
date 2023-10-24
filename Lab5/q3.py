class Subset():
    def generateSubset(l1):
        n = len(l1)
        temp_list = []
        for start in range(n):
            for end in range(start + 1, n + 1):
                temp_list.append(l1[start:end])
        return temp_list

n=int(input('Enter number of elements: '))
l1=[]
print("Enter list values: ")
for i in range(n):
    num=int(input())
    l1.append(num)
ans = Subset.generateSubset(l1)
ans.append([])
print(ans)