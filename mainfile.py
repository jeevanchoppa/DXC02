
def create():
    import sqlite3
    con = sqlite3.connect('StudDetails01.db')
    cur = con.cursor()
    table = """CREATE TABLE StudDetails01 (RollNo int, StudName VARCHAR(30), PhyMarks int, CheMarks int, MathMarks)"""
    cur.execute(table)
    con.commit()
    print("Table successfully created")

def insert(RollNo, StudName, PhyMarks, CheMarks, MathMarks):

    RollNo = input("Enter RollNo = ")
    StudName = input("Enter Student Name = ")
    PhyMarks = input("Enter Phy Marks = ")
    CheMarks = input("Enter Che Marks = ")
    MathMarks = input("Enter Math Marks = ")
    data = cur.execute('''INSERT INTO StudDetails01 (RollNo, StudName, PhyMarks, CheMarks, MathMarks) VALUES(?,?,?,?,?)''', (RollNo, StudName, PhyMarks, CheMarks, MathMarks))
    con.commit()    

def fetch ():
    import sqlite3
    con = sqlite3.connect('StudDetails01.db')
    cur = con.cursor()
    data = cur.execute('''select * from StudDetails01''')
    for row in data:
        RollNo = row[0]
        StudName = row[1]
        PhyMarks = row[2]
        CheMarks = row[3]
        MathMarks = row[4]

        print(str(RollNo) + "  ,  " + StudName + "  ,  " + str(PhyMarks) + "  ,  " + str(CheMarks) + "  ,  " + str(MathMarks))

def update (RollNo, MathMarks):
    import sqlite3
    con = sqlite3.connect('StudDetails01.db')
    cur = con.cursor()

    RollNo = input("Enter RollNo which you want to update = ")
    MathMarks = input("Enter Math Marks which you want to update = ")
    data = cur.execute('''UPDATE StudDetails01 set MathMarks = ? ''' '''where RollNo = ?''', (MathMarks, RollNo,))
    con.commit()

def delete (RollNo):
    RollNo = input("Enter RollNo which you want to delete = ")
    data = cur.execute('''delete from StudDetails01 where RollNo = ?''', (RollNo, ))
    con.commit() 
    con.close()

choice = 9
while (choice != 0):
    print("Enter 1 to Create Table :")
    print("Enter 2 for INSERT :")
    print("Enter 3 for FETCH : ")
    print("Enter 4 for UPDATE :")
    print("Enter 5 for DELETE :")
    print(" ")
    print("Enter 0 to EXIT ")
    print(" ")
    choice = int(input('Enter your Choice : '))
    if choice == 1:
        print(create())
    if choice == 2:
        print(insert('val1', 'val2', 'val3', 'val4', 'val5'))
    elif choice == 3:
        print(fetch ())
    elif choice == 4:
        print(update('RollNo', 'MathMarks'))
    elif choice == 5:
        print(delete('RollNo'))
