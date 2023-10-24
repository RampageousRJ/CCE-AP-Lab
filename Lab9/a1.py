from q3 import Bank

class WithdrawError(Exception):
    pass

class DailyDepositError(Exception):
    pass

class DailyWithdrawError(Exception):
    pass

class ExtendedBank(Bank):
    def withdraw(self,amount):
        if self.balance-1000<amount:
            raise WithdrawError
        self.balance-=amount
    
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
                    daily_deposit=0
                    daily_withdraw=0
                    while True:
                        ch1=int(input("\nMENU\n1.Display\n2.Withdraw\n3.Deposit\n4.Logout\nEnter choice: "))
                        if ch1==1:
                            emp.display()
                        elif ch1==2:
                            try:
                                amount=int(input('Enter amount: '))
                                if amount+daily_withdraw>5000:
                                    raise DailyWithdrawError
                                daily_withdraw+=amount
                                emp.withdraw(amount)
                            except WithdrawError:
                                print("Minimum Balance Violated")
                            except DailyWithdrawError:
                                print("Daily Withdrawl Limit Exceeded")
                        elif ch1==3:
                            try:
                                amount=int(input('Enter amount: '))
                                if amount+daily_deposit>10000:
                                    raise DailyDepositError
                                daily_deposit+=amount
                                emp.deposit(amount)
                            except DailyDepositError:
                                print("Daily Deposit Limit Exceeded")
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