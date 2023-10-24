class Bank():
    def __init__(self):
        self.name = input("CREATE NEW USER\nEnter name: ")
        self.age = int(input("Enter Age: "))
        self.accno = input("Enter Account Number: ")
        self.acctype = input("Enter Account Type: ")
        self.balance = 0
        
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
    acc = Bank()
    emps.append(acc)
    while True:
        ch = int(input("\nOPTIONS\n1.Register\n2.Login\n3.Exit\nEnter choice: "))
        if ch==1:
            acc=Bank()
            emps.append(acc)
        elif ch==2:
            name=input("Enter name: ")
            flag=False
            for emp in emps:
                if name.lower()==emp.name.lower():
                    print("\nLogged In!")
                    flag=True
                    while True:
                        ch1=int(input("\nMENU\n1.Display\n2.Withdraw\n3.Deposit\n4.LogoutEnter choice: "))
                        if ch1==1:
                            emp.display()
                        elif ch1==2:
                            emp.withdraw(int(input('Enter amount: ')))
                        elif ch1==3:
                            emp.deposit(int(input('Enter amount: ')))
                        elif ch1==4:
                            print("Logging Out!")
                            break
                        else:
                            print("Invalid Option...")
            if flag==False:
                print("User Not Found")
        elif ch==3:
            print("Thank you for using this service...")
            break
        else:
            print("Invalid Option...")