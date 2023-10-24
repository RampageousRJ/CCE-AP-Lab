class Bank():
    def __init__(self,name,age,accno,acctype,balance):
        self.name=name
        self.age=int(age)
        self.accno=accno
        self.acctype=acctype
        self.balance=int(balance)
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if self.balance<amount:
            print("Insufficient Balance")
            return
        self.balance-=amount
    def display(self):
        print(f"\nDETAILS\nName: {self.name}\nAge: {self.age}\nAccount Number: {self.accno}\nAccount Type: {self.acctype}\nBalance: {self.balance}\n")
    def __del__(self):
        print("Destructor Called")

if __name__=='__main__':
    emps=[]
    with open('bank.txt','r') as fp:
        for line in fp.readlines():
            details=line.split(',')
            emps.append(Bank(details[0],details[1],details[2],details[3],details[4].strip("\n")))
    name=input("Enter name: ")
    flag=False
    for emp in emps:
        if emp.name.lower()==name.lower():
            flag=True
            while True:       
                ch=int(input("\nWELCOME\n1.Display\n2.Deposit\n3.Withdraw\nEnter choice: "))
                if ch==1:
                    emp.display()
                elif ch==2:
                    amount=int(input("Enter amount: "))
                    emp.deposit(amount)
                elif ch==3:
                    amount=int(input("Enter amount: "))
                    emp.withdraw(amount)
                else:
                    break
    if flag==False:
        print("User not found...")