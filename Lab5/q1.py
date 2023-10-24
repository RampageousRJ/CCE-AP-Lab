class Employee():
    def __init__(self,id,name,salary,department):
        self.details=(id,name,salary,department)
        
n=int(input("Enter number of employees: "))
k=1
emps=[]
for i in range(n):
    print("\nDETAILS FOR EMP",k)
    id=int(input("Enter ID: "))
    name=input("Enter Name: ")
    sal=int(input("Enter Salary: "))
    dept=input("Enter Department: ")
    e=Employee(id,name,sal,dept)
    emps.append(e)
    k+=1
flag=True
sid=int(input("\nSEARCH FOR EMPLOYEE :: Enter ID: "))
for emp in emps:
    if emp.details[0]==sid:
        print(f"ID: {emp.details[0]}\nName: {emp.details[1]}\nSalary: {emp.details[2]}\nDepartment: {emp.details[3]}")
        flag=False
if flag==True:
    print("Not Found...")