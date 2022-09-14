
def delete (RollNo):

    import sqlite3
    con = sqlite3.connect('StudDetails01.db')
    cur = con.cursor()
    RollNo = input("Enter RollNo which you want to delete = ")
    data = cur.execute('''delete from StudDetails01 where RollNo = ?''', (RollNo, ))
    con.commit()
    con.close()