
def create():
    import sqlite3
    con = sqlite3.connect('StudDetails01.db')
    cur = con.cursor()
    table = """CREATE TABLE StudDetails01 (RollNo int, StudName VARCHAR(30), PhyMarks int, CheMarks int, MathMarks)"""
    cur.execute(table)
    con.commit()
    print("Table successfully created")

def insert(RollNo, StudName, PhyMarks, CheMarks, MathMarks)

    RollNo = input("Enter RollNo = ")
    StudName = input("Enter Student Name = ")
    PhyMarks = input("Enter Phy Marks = ")
    CheMarks = input("Enter Che Marks = ")
    MathMarks = input("Enter Math Marks = ")
    cur.execute('''INSERT INTO StudDetails01 (RollNo, StudName, PhyMarks, CheMarks, MathMarks) VALUES(?,?,?,?,?)''', (RollNo, StudName, PhyMarks, CheMarks, MathMarks))
    con.commit()
    con.close()

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
    con.close()

