from tkinter import messagebox
from tkinter import *
import sqlite3
import re

db = sqlite3.connect("bank.db")
cur = db.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS CUSTOMER(NAME VARCHAR(30) NOT NULL, PASSWORD VARCHAR(30) NOT NULL, BALANCE INT)")

class Home(Tk):
    def __init__(self):
        super().__init__()
        self.title("Landing Page")
        self.geometry('400x300')
        self.create_widgets()
        self.config(bg='sea green')
        
    def login(self):
        self.destroy()
        Login()
    
    def register(self):
        self.destroy()
        Register()
    
    def create_widgets(self):
        self.label = Label(self,text="IDGAF BANK",font=("Calibri",30),bg="sea green").pack(pady=(10,10))    
        self.b1 = Button(self,text="Login",command=self.login,bg="dark green",width=25).pack(pady=(30,30))
        self.b2 = Button(self,text="Register",command=self.register,bg="dark green",width=25).pack(pady=(30,30))

class Login(Tk):
    def __init__(self):
        super().__init__()
        self.title("Login Page")
        self.geometry('400x300')
        self.create_widgets()
        self.config(bg='sea green')
        
    def validate(self):
        name = self.e1.get().strip(" ")
        password = self.e2.get().strip(" ")
        data = cur.execute(f"SELECT * FROM CUSTOMER WHERE NAME='{name}' AND PASSWORD='{password}'")
        count=0
        for row in data:
            count+=1
        if count==0:
            self.e1.delete("0","end")
            self.e2.delete("0","end")
            messagebox.showerror(title="Fail",message="Invalid Credentials!\n\nTry Again!")
            return
        self.destroy()
        Profile(name)
        
    def back(self):
        self.destroy()
        Home()
    
    def create_widgets(self):
        self.label = Label(self,text="IDGAF BANK",font=("Calibri",30),bg="sea green").pack(pady=(10,10))    
        self.l1 = Label(self,text="Enter Name",bg="sea green").pack(pady=(10,10))    
        self.e1 = Entry(self,text="Login",width=25)
        self.e1.pack(pady=(0,15))
        self.l2 = Label(self,text="Enter Password",bg="sea green").pack(pady=(10,10))    
        self.e2 = Entry(self,text="Register",width=25)
        self.e2.pack(pady=(0,15))
        self.b2 = Button(self,text="Login",command=self.validate,bg="dark green",width=20).pack(pady=(20,30),side=RIGHT)
        self.b3 = Button(self,text="Back",command=self.back,bg="dark green",width=20).pack(pady=(20,30),side=LEFT)
         
class Register(Tk):
    def __init__(self):
        super().__init__()
        self.title("Register Page")
        self.geometry('400x400')
        self.create_widgets()
        self.config(bg='sea green')
        
    def validate(self):
        name = self.e1.get()
        password = self.e2.get()
        balance = self.e3.get()
        p1 = r".*[^A-Za-z0-9].*$"
        p2 = r".{12,}$"
        p3 = r"[A-Za-z]{1,}.*\d{1,}|\d{1,}.*[A-Za-z]{1,}"
        if re.match(p1,password) and re.match(p2,password) and re.match(p3,password):
            cur.execute("INSERT INTO CUSTOMER VALUES(?,?,?)",(name,password,balance))
            db.commit()
            messagebox.showinfo(title="Success",message="Registered Successfully!")
            self.destroy()
            Home()
        else:
            self.e2.delete('0','end')
            messagebox.showerror(title="Error",message="Password Invalid!")            
        
    def back(self):
        self.destroy()
        Home()
    
    def create_widgets(self):
        self.label = Label(self,text="IDGAF BANK",font=("Calibri",30),bg="sea green").pack(pady=(10,10))    
        self.l1 = Label(self,text="Enter Name",bg="sea green").pack(pady=(10,10))    
        self.e1 = Entry(self,text="Login",width=25)
        self.e1.pack(pady=(0,15))
        self.l2 = Label(self,text="Enter Password",bg="sea green").pack(pady=(10,10))    
        self.e2 = Entry(self,text="Register",width=25)
        self.e2.pack(pady=(0,15))
        self.l2 = Label(self,text="Enter Balance",bg="sea green").pack(pady=(10,10))
        self.e3 = Entry(self,text="Balance",width=25)
        self.e3.pack(pady=(0,15))
        self.b2 = Button(self,text="Register",command=self.validate,bg="dark green",width=20).pack(pady=(20,30),padx=(10,0),side=RIGHT)
        self.b3 = Button(self,text="Back",command=self.back,bg="dark green",width=20).pack(pady=(20,30),padx=(0,10),side=LEFT)       
        
class Profile(Tk):
    def __init__(self,name):
        super().__init__()
        self.title(f"{name} Page")
        self.geometry('400x250')
        self.config(bg='sea green')
        self.name = StringVar()
        self.name.set(name)
        self.balance = StringVar()
        self.getValues()
        self.create_widgets()
        self.grid()
    
    def getValues(self):
        data = cur.execute(f"SELECT * FROM CUSTOMER WHERE NAME='{self.name.get()}'")
        for row in data:
            self.balance.set(str(row[2]))
            
    def withdraw(self):
        self.destroy()
        Withdraw(self.name.get())
        
    def deposit(self):
        self.destroy()
        Deposit(self.name.get())
    
    def create_widgets(self):
        self.label = Label(self,text="IDGAF BANK",font=("Calibri",30),bg="sea green").grid(row=0,column=0,columnspan=2,padx=(40,20),pady=(10,10),sticky="nsew")   
        self.l1 = Label(self,text="Name: ",bg="sea green",font=('Calibri Bold',14)).grid(row=1,column=0,sticky="nsew",pady=(10,10))
        self.l2 = Label(self,text=self.name.get(),bg="sea green").grid(row=1,column=1,sticky="nsew",pady=(10,10))
        self.l3 = Label(self,text="Balance: ",bg="sea green",font=('Calibri Bold',14)).grid(row=2,column=0,sticky="nsew",pady=(10,10))
        self.l4 = Label(self,text=self.balance.get(),bg="sea green").grid(row=2,column=1,sticky="nsew",pady=(10,10))
        self.b0 = Button(self,text="Withdraw",command=self.withdraw,bg="dark green",width=20).grid(row=3,column=0,sticky="nsew",padx=(20,20),pady=(10,10))    
        self.b1 = Button(self,text="Deposit",command=self.deposit,bg="dark green",width=20).grid(row=3,column=1,sticky="nsew",padx=(20,20),pady=(10,10)) 

class Deposit(Tk):
    def __init__(self,name):
        super().__init__()
        self.title("Landing Page")
        self.geometry('400x300')
        self.create_widgets()
        self.config(bg='sea green')
        self.balance = StringVar()
        self.name = StringVar()
        self.name.set(name)
        self.getValues()
        
    def getValues(self):
        data = cur.execute(f"SELECT * FROM CUSTOMER WHERE NAME='{self.name.get()}'")
        for row in data:
            self.balance.set(str(row[2]))
    
    def deposit(self):
        new_balance = int(self.e1.get()) + int(self.balance.get())
        cur.execute(f"UPDATE CUSTOMER SET BALANCE={new_balance} WHERE NAME='{self.name.get()}'")
        db.commit()
        messagebox.showinfo(title="Success",message="Deposited Successfully!")
        self.destroy()
        Profile(self.name.get())
        
    def back(self):
        self.destroy()
        Profile(self.name.get())
    
    def create_widgets(self):
        self.label = Label(self,text="IDGAF BANK",font=("Calibri",30),bg="sea green").pack(pady=(20,10))
        self.l2 = Label(self,text="Enter Amount to Deposit",bg="sea green").pack(pady=(10,10))    
        self.e1 = Entry(self,text="Deposit",width=25)
        self.e1.pack(pady=(0,15))
        self.b1 = Button(self,text="Deposit",command=self.deposit,bg="dark green",width=25).pack(pady=(15,30),side=RIGHT)
        self.b2 = Button(self,text="Back",command=self.back,bg="dark green",width=25).pack(pady=(15,30),side=LEFT)
        
class Withdraw(Tk):
    def __init__(self,name):
        super().__init__()
        self.title("Landing Page")
        self.geometry('400x300')
        self.create_widgets()
        self.config(bg='sea green')
        self.balance = StringVar()
        self.name = StringVar()
        self.name.set(name)
        self.getValues()
        
    def getValues(self):
        data = cur.execute(f"SELECT * FROM CUSTOMER WHERE NAME='{self.name.get()}'")
        for row in data:
            self.balance.set(str(row[2]))
    
    def withdraw(self):
        new_balance = int(self.balance.get()) - int(self.e1.get())
        if new_balance<0:
            self.e1.delete('0','end')
            messagebox.showerror(title="Error",message="Insufficient Balance to Withdraw!")
            return
        cur.execute(f"UPDATE CUSTOMER SET BALANCE={new_balance} WHERE NAME='{self.name.get()}'")
        db.commit()
        messagebox.showinfo(title="Success",message="Withdrawn Successfully!")
        self.destroy()
        Profile(self.name.get())
        
    def back(self):
        self.destroy()
        Profile(self.name.get())
    
    def create_widgets(self):
        self.label = Label(self,text="IDGAF BANK",font=("Calibri",30),bg="sea green").pack(pady=(20,10))
        self.l2 = Label(self,text="Enter Amount to Withdraw",bg="sea green").pack(pady=(10,10))    
        self.e1 = Entry(self,text="Withdraw",width=25)
        self.e1.pack(pady=(0,15))
        self.b1 = Button(self,text="Withdraw",command=self.withdraw,bg="dark green",width=25).pack(pady=(15,30),side=RIGHT)
        self.b2 = Button(self,text="Back",command=self.back,bg="dark green",width=25).pack(pady=(15,30),side=LEFT)

if __name__=='__main__':
    app = Home()
    app.mainloop()