class Employee():
    def __init__(self,id,name,sal,dept):
        self.id=id
        self.name=name
        self.sal=sal
        self.dept=dept

def computeSal(emp):
    sum=0
    for i in emp:
        sum+=i.sal
    return sum

if __name__=='__main__':
    n=int(input("Enter total employees: "))
    for i in range(n):
        print("ENTER EMPLOYEE",i+1,": ")
        id=int(input("Enter ID:"))
        