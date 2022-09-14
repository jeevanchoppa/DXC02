def update (RollNo, MathMarks):

    import sqlite3
    con = sqlite3.connect('StudDetails01.db')
    cur = con.cursor()
    RollNo = input("Enter RollNo which you want to update = ")
    MathMarks = input("Enter Math Marks which you want to update = ")
    data = cur.execute('''UPDATE StudDetails01 set MathMarks = ? ''' '''where RollNo = ?''', (MathMarks, RollNo,))
    con.commit()
    con.close()