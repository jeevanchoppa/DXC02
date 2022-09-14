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