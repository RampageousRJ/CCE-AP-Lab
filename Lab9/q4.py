from q3 import Bank

class InvalidAge(Exception):
    pass

class InvalidAccountNumber(Exception):
    pass

class InvalidAccountType(Exception):
    pass

class ExtendedBank(Bank):
    def __init__(self):
        while True:
            self.name = input("\n\nCREATE NEW USER\nEnter name: ")
            try:
                self.age = int(input("Enter Age: "))
                if self.age<18 or self.age>100:
                    raise InvalidAge
            except InvalidAge:
                print("Value exceeding range")
                continue
            try:
                self.accno = int(input("Enter Account Number: "))
                if len(str(self.accno))!=5:
                    raise InvalidAccountNumber
            except InvalidAccountNumber:
                print("Should have exactly 5 digits")
                continue
            except ValueError:
                print("Should be numeric")
                continue
            try:
                self.acctype = input("Enter Account Type: ")
                if self.acctype!='S' and self.acctype!='C':
                    raise InvalidAccountType
            except InvalidAccountType:
                print("Should be Savings(S) or Current(C)")
                continue
            self.balance = 0 
            break
        
if __name__=='__main__':
    emps=[]
    acc = ExtendedBank()
    emps.append(acc)
    while True:
        ch = int(input("\nOPTIONS\n1.Register\n2.Login\n3.Exit\nEnter choice: "))
        if ch==1:
            acc=ExtendedBank()
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