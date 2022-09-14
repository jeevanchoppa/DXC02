
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