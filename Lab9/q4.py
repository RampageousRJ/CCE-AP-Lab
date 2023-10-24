from q3 import Bank

class ExtendedBank(Bank):
    def __init__(self):
        self.name = input("CREATE NEW USER\nEnter name: ")
        try:
            self.age = int(input("Enter Age: "))
            if self.age<18 or self.age>100:
                raise InterruptedError
        except InterruptedError:
            print("Value exceeding range")
            exit()
        try:
            self.accno = input("Enter Account Number: ")
            int(self.accno)
            if len(self.accno)>5:
                raise InterruptedError
        except InterruptedError:
            print("Should have exactly 5 digits")
            exit()
        except ValueError:
            print("Should be numeric")
            exit()
        try:
            self.acctype = input("Enter Account Type: ")
            if self.acctype!='S' or self.acctype!='C':
                raise InterruptedError
        except InterruptedError:
            print("Should be Savings(S) or Current(C)")
            exit()
        
        self.balance = 0        

if __name__=='__main__':
    emps=[]
    acc = ExtendedBank()
    emps.append(acc)
    while True:
        ch = int(input("\nOPTIONS\n1.Register\n2.Login\nEnter choice: "))
        if ch==1:
            acc=ExtendedBank()
            emps.append(acc)
        elif ch==2:
            name=input("Enter name: ")
            for emp in emps:
                if name.lower()==emp.name.lower():
                    print("\nLogged In!")
                    while True:
                        ch1=int(input("\nMENU\n1.Display\n2.Withdraw\n3.Deposit\nEnter choice: "))
                        if ch1==1:
                            emp.display()
                        elif ch1==2:
                            amount=int(input('Enter amount: '))
                            emp.withdraw(amount)
                        elif ch1==3:
                            amount=int(input('Enter amount: '))
                            emp.deposit(amount)
                        else:
                            print("Logging Out!")
                            break
        else:
            break