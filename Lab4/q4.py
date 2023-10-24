import datetime
def greet(name):
    print('Welcome',name,"the time is",datetime.datetime.now())
    
s=input("Enter name: ")
greet(s)