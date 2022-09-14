def create():

    import sqlite3
    con = sqlite3.connect('StudDetails01.db')
    cur = con.cursor()
    table = """CREATE TABLE StudDetails01 (RollNo int, StudName VARCHAR(30), PhyMarks int, CheMarks int, MathMarks)"""
    cur.execute(table)
    con.commit()
    print("Table successfully created")
    con.close()