class Employee():
    def __init__(self,id,name,sal,dept):
        self.id=id
        self.name=name
        self.sal=sal
        self.dept=dept
    
    def __del__(self):
        print("Destructor Called")
        
    def display(self):
        print(f"\nDETAILS\nID: {self.id}\nName: {self.name}\nSalary: {self.sal}\nDepartment: {self.dept}")

def computeSal(emps):
    sum=0
    for emp in emps:
        sum+=emp.sal
    return sum

if __name__=='__main__':
    emps=[]
    n=int(input("Enter total employees: "))
    for i in range(n):
        print("\nENTER EMPLOYEE",i+1)
        if i==0:
            id=2912
        else:
            id = emps[i-1].id + 1
        name = input("Enter name: ")
        salary = int(input("Enter salary: "))
        dept = input("Enter department: ")
        emps.append(Employee(id,name,salary,dept))
    while True:
        ch = int(input("\n\nOPTIONS\n1.Compute Salary\n2.Search Employee\n3.Exit\nEnter Choice: "))
        if ch==1:
            print("Total Employees Salary: ",computeSal(emps))
        elif ch==2:
            id = int(input("Enter ID to search: "))
            for emp in emps:
                if emp.id==id:
                    emp.display()
        elif ch==3:
            print("Thanks for choosing our service...")
            break
        else:
            print("Invalid Option...")
        