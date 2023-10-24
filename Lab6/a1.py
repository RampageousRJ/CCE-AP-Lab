import sqlite3
db='appointment.db'
conn = sqlite3.connect(db)
cur = conn.cursor()
def create():
    query='''
        CREATE TABLE IF NOT EXISTS APPOINTMENT(
        ID INT PRIMARY KEY,
        DOCTOR_NAME VARCHAR(30) NOT NULL,
        PATIENT_ID VARCHAR(30) NOT NULL,
        TIME VARCHAR(30) NOT NULL);
    '''
    cur.execute(query)
    conn.commit()
    print("Table Ready")

def insert():
    id = int(input("Enter Appointment ID: "))
    name = input("Enter Doctor Name: ")
    pid = input("Enter Patient ID: ")
    time = input('Enter Time of Appointment: ')
    cur.execute(f"INSERT INTO APPOINTMENT('ID','DOCTOR_NAME','PATIENT_ID','TIME') VALUES(?,?,?,?)",(id,name,pid,time))
    conn.commit()
    print("Record Inserted Successfully")
    
def findAppointment():
    id=input("Find Appointment: ")
    cur = conn.cursor()
    data = cur.execute(f"SELECT * FROM APPOINTMENT WHERE ID={id}")
    count=0
    for row in data:
        print(row)
        count+=1
    if count==0:
        print("NO RECORDS FOUND...")
        
def update():
    id=input("Appointment to be updated: ")
    cur = conn.cursor()
    data = cur.execute(f"SELECT * FROM APPOINTMENT WHERE ID={id}")
    count=0
    for row in data:
        count+=1
    if count==0:
        print("NO RECORDS FOUND...")
        return
    field = input("Enter field to be updated: ")
    newval = input("Enter new value: ")
    data = cur.execute(f"UPDATE APPOINTMENT SET {field}='{newval}' WHERE ID={id}")
    conn.commit()
    print("Updated Successfully...")
    
def delete():
    id=input("Appointment to be deleted: ")
    cur = conn.cursor()
    data = cur.execute(f"SELECT * FROM APPOINTMENT WHERE id={id}")
    count=0
    for row in data:
        count+=1
    if count==0:
        print("NO RECORDS FOUND...")
        return
    data = cur.execute(f"DELETE FROM APPOINTMENT WHERE ID={id}")
    conn.commit()
    print("Deleted Successfully...")

def select():
    cur.execute("SELECT * FROM APPOINTMENT")
    for row in cur:
        print(row)

if __name__=='__main__':
    create()
    while(True):
        ch = int(input("\n\nMENU\n1.Insert\n2.Search Appointment\n3.Update Appointment\n4.Delete\n5.DisplayAll\n6.Exit\nEnter your choice: "))
        if ch==1:
            insert()
        elif ch==2:
            findAppointment()
        elif ch==3:
            update()
        elif ch==4:
            delete()
        elif ch==5:
            select()
        elif ch==6:
            print("\nTHANK YOU FOR USING OUR SERVICE...")
            break
        else:
            print("INVALID FEATURE...")
            break
    conn.close()