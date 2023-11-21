import sqlite3
import re
from datetime import date
conn = sqlite3.connect('department.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS DEPARTMENT(EMPNO INT PRIMARY KEY, NAME VARCHAR(30), DEPT VARCHAR(30), SALARY INT)")

def insert():
    id = int(input('Enter ID: '))
    name = input('Enter Name: ')
    dept =input("Enter Department: ")
    salary = int(input("Enter Salary: "))
    cur.execute("INSERT INTO DEPARTMENT VALUES(?,?,?,?)",(id,name,dept,salary))
    conn.commit()
    print("Inserted Successfully...")

def view():
    data = cur.execute("SELECT * FROM DEPARTMENT")
    for row in data:
        if re.match(r"^[Aa]",row[1]):
            print(row)
        
if __name__=='__main__':
    # insert()
    # view()
    d1 = date(2020,2,21)
    d2 = date(2024,8,20)
    d = d2-d1
    print(d.days)