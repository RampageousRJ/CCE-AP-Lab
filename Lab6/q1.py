import sqlite3
db="student.db"
conn = sqlite3.connect(db)

def create():
    cur = conn.cursor()
    table = """ CREATE TABLE IF NOT EXISTS STUDENT(
                reg varchar(9) primary key,
                name varchar(30) not null, 
                phone varchar(10) not null,
                marks int not null
    );
    """
    cur.execute(table)
    print("Table is ready")
    

def insert():
    print("\n\nINSERT DETAILS:\n")
    regno=input("Enter regno: ")
    name=input("Enter name: ")
    phone=input("Enter phone: ")
    marks=input("Enter marks: ")
    cur = conn.cursor()
    cur.execute("INSERT INTO STUDENT('REG','NAME','PHONE','MARKS') VALUES(?,?,?,?)",(regno,name,phone,marks))
    print("Inserted Student")
    conn.commit()
    
def read():
    regno=input("Find Regno: ")
    cur = conn.cursor()
    data = cur.execute(f"SELECT * FROM STUDENT WHERE REG={regno}")
    count=0
    for row in data:
        print(row)
        count+=1
    if count==0:
        print("NO RECORDS FOUND...")
        
def display():
    cur = conn.cursor()
    data = cur.execute(" SELECT * FROM STUDENT")
    for row in data:
        print(row)
        
def update():
    regno=input("Regno to be updated: ")
    cur = conn.cursor()
    data = cur.execute(f"SELECT * FROM STUDENT WHERE REG={regno}")
    count=0
    for row in data:
        count+=1
    if count==0:
        print("NO RECORDS FOUND...")
        return
    field = input("Enter field to be updated: ")
    newval = input("Enter New Value: ")
    data = cur.execute(f"UPDATE STUDENT SET {field}={newval}")
    conn.commit()
    print("Updated Successfully...")
    
def deleteRec():
    regno=input("Regno to be deleted: ")
    cur = conn.cursor()
    data = cur.execute(f"SELECT * FROM STUDENT WHERE REG={regno}")
    count=0
    for row in data:
        count+=1
    if count==0:
        print("NO RECORDS FOUND...")
        return
    data = cur.execute(f"DELETE FROM STUDENT WHERE REG={regno}")
    conn.commit()
    print("Deleted Successfully...")
    
if __name__=='__main__':
    create()
    while(True):
        ch = int(input("\n\nMENU\n1.Insert\n2.Read\n3.Update\n4.Delete\n5.DisplayAll\n6.Exit\nEnter your choice: "))
        if ch==1:
            insert()
        elif ch==2:
            read()
        elif ch==3:
            update()
        elif ch==4:
            deleteRec()
        elif ch==5:
            display()
        elif ch==6:
            print("\nTHANK YOU FOR USING OUR SERVICE...")
            break
        else:
            print("INVALID FEATURE...")
            break
    conn.close()