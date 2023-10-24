import sqlite3
db='appointment.db'
conn = sqlite3.connect(db)
cur = conn.cursor()
def create():
    query='''
        CREATE TABLE IF NOT EXISTS DOCTOR(
        ID INT PRIMARY KEY,
        NAME VARCHAR(30) NOT NULL,
        DEPT VARCHAR(30) NOT NULL,
        SALARY INT);
    '''
    cur.execute(query)
    conn.commit()

def insert():
    id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    dept = input("Enter Department: ")
    sal = int(input('Enter Salary: '))
    cur.execute(f"INSERT INTO DOCTOR('ID','NAME','DEPT','SALARY') VALUES(?,?,?,?)",(id,name,dept,sal))
    conn.commit()

def select():
    cur.execute("SELECT * FROM DOCTOR")
    for row in cur:
        print(row)

if __name__=='__main__':
    select()
    # print("Inserted Successfully")