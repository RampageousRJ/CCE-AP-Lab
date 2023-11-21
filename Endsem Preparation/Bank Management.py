import tkinter as tk
import sqlite3
import re

class Login(tk.Frame):
    
    def __init__(self,conn,master=None):
        tk.Frame.__init__(self,master,height=500,width=500)
        self.conn = conn
        self.curr = conn.cursor()
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        self.uname = tk.Label(self, text="Username : ").grid(row=0, column=0)
        self.passw = tk.Label(self, text="Password : ").grid(row=1, column=0)
        
        self.enter_uname = tk.Entry(self)
        self.enter_uname.grid(row=0,column=1)
        
        self.enter_pass = tk.Entry(self)
        self.enter_pass.grid(row=1,column=1)
        
        self.login = tk.Button(self, text="Login", command=self.submit).grid(row=2,column=0,columnspan=2)
        self.signup = tk.Button(self, text="Signup", command=self.signup).grid(row=3,column=0,columnspan=2)
        
    def submit(self):
        uname = self.enter_uname.get()
        passw = self.enter_pass.get()
        self.curr.execute(f"select * from users where username='{uname}' and password='{passw}'")
        
        data_row = self.curr.fetchone()
        if data_row is not None:
            global _user,_pass,_bal
            _id,_user,_pass,_bal = data_row
            self.grid_forget()
            profile = Profile(self.conn, self.master)
            profile.grid()
        else:
            print("Not a valid user")
    
    def signup(self):
        self.grid_forget()
        signup = Signup(self.conn,self.master)
        signup.grid()
        
            
class Profile(tk.Frame):
    
    def __init__(self,conn,master=None):
        tk.Frame.__init__(self,master,height=500,width=500)
        self.conn = conn
        self.curr = conn.cursor()
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        self.uname = tk.Label(self, text="Username : ").grid(row=0, column=0)
        self.bal = tk.Label(self, text="Balance : ").grid(row=1, column=0)
        
        self.curr.execute(f"select * from users where username='{_user}' and password='{_pass}'")
        data_row = self.curr.fetchone()
        
        *notneeded,_bal = data_row
        
        self.show_uname = tk.Label(self, text=_user)
        self.show_uname.grid(row=0,column=1)
        
        self.show_bal = tk.Label(self, text=_bal)
        self.show_bal.grid(row=1,column=1)
        
        self.withdraw_butt = tk.Button(self, text="Withdraw", command=self.withdraw)
        self.withdraw_butt.grid(row=2,column=0)
        
        self.deposit_butt = tk.Button(self, text='Deposit', command=self.deposit)
        self.deposit_butt.grid(row=2,column=1)
        
        self.logout = tk.Button(self,text="Logout", command=self.logout)
        self.logout.grid(row=3,column=0,columnspan=2)
    
    def withdraw(self):
        self.grid_forget()
        withdraw = Withdraw(self.conn,self.master)
        withdraw.grid()
    
    def deposit(self):
        self.grid_forget()
        deposit = Deposit(self.conn,self.master)
        deposit.grid()
    
    def logout(self):
        self.grid_forget()
        logout = Login(self.conn,self.master)
        logout.grid()
        
class Deposit(tk.Frame):
    def __init__(self,conn,master=None):
        tk.Frame.__init__(self,master,height=500,width=500)
        self.conn = conn
        self.curr = conn.cursor()
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        self.with_amt = tk.Label(self, text="Enter amount to be Deposit : ").grid(row=0, column=0)
        
        self.enter_amt = tk.Entry(self)
        self.enter_amt.grid(row=0,column=1)
        
        self.dep_butt = tk.Button(self, text="Deposit", command=self.deposit).grid(row=2,column=0,rowspan=2)
    
    def deposit(self):
        try:
            amt = int(self.enter_amt.get())
            self.curr.execute(f"update users set balance=balance+{amt} where username='{_user}'")
            self.grid_forget()
            self.conn.commit()
            profile = Profile(self.conn,self.master)
            profile.grid()
        except:
            print('Invalid')
        
class Withdraw(tk.Frame):
    def __init__(self,conn,master=None):
        tk.Frame.__init__(self,master,height=500,width=500)
        self.conn = conn
        self.curr = conn.cursor()
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        self.with_amt = tk.Label(self, text="Enter amount to be withdrawn : ").grid(row=0, column=0)
        
        self.enter_amt = tk.Entry(self)
        self.enter_amt.grid(row=0,column=1)
        
        self.with_butt = tk.Button(self, text="Withdraw", command=self.withdraw).grid(row=2,column=0,rowspan=2)
    
    def withdraw(self):
        try:
            amt = int(self.enter_amt.get())
            self.curr.execute(f"select * from users where username='{_user}' and password='{_pass}'")
            data_row = self.curr.fetchone()
            *notneeded,_bal = data_row
            if _bal >= amt:
                self.curr.execute(f"update users set balance=balance-{amt} where username='{_user}'")
                self.grid_forget()
                self.conn.commit()
                profile = Profile(self.conn,self.master)
                profile.grid()
            else:
                print("Not enough balance in your account!")
        except:
            print("Invalid!")

class Signup(tk.Frame):
    
    def __init__(self,conn,master=None):
        tk.Frame.__init__(self,master,height=500,width=500)
        self.conn = conn
        self.curr = conn.cursor()
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        self.uname = tk.Label(self, text="Username : ").grid(row=0, column=0)
        self.passw = tk.Label(self, text="Password : ").grid(row=1, column=0)
        
        self.enter_uname = tk.Entry(self)
        self.enter_uname.grid(row=0,column=1)
        
        self.enter_pass = tk.Entry(self)
        self.enter_pass.grid(row=1,column=1)
        
        self.signup = tk.Button(self, text="Signup", command=self.submit).grid(row=2,column=0,columnspan=2)
        
    def submit(self):
        uname = self.enter_uname.get()
        passw = self.enter_pass.get()
        if re.search('[A-Z]',passw) is not None and re.search('[^A-Za-z0-9]',passw) is not None and len(passw) >= 12:
            self.curr.execute(f"insert into users values(NULL,'{uname}','{passw}',0)")
            print("Succesful Signup!")
        
            self.conn.commit()
        
            self.grid_forget()
            login = Login(self.conn,self.master)
            login.grid()
        else:
            print("Invalid Password")
        
def main():
    root = tk.Tk()
    root.title('bank Management')
    conn = sqlite3.connect('banking.db')
    app = Login(conn,root)
    
    app.mainloop()
    
if __name__ == '__main__':
    main()
    