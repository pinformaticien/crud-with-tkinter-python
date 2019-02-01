import sqlite3

def connect_db():
    con=sqlite3.connect("emps.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS emp\
                 (id INTEGER PRIMARY KEY,\
                 fn TEXT, ln TEXT, dept TEXT, sal INTEGER)")
    con.commit()
    con.close()


def addrec(fn, ln, dept, sal):
    con=sqlite3.connect("emps.db")
    cur=con.cursor()
    cur.execute("INSERT INTO emp VALUES\
        (NULL, ?, ?, ?, ?)", (fn, ln, dept, sal))
    con.commit()
    con.close()


def view():
    con=sqlite3.connect("emps.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM emp")
    rows=cur.fetchall()
    con.close()
    return rows


def dele(id):
    con=sqlite3.connect("emps.db")
    cur=con.cursor()
    cur.execute\
            ("DELETE FROM emp WHERE \
            id=?", (id,))
    con.commit()
    con.close()


def findit(fn="", ln="", dept="", sal=0):
    con=sqlite3.connect("emps.db")
    cur=con.cursor()
    cur.execute("SELECT * FROM emp WHERE\
                fn=? OR ln=? OR dept=? OR sal=?",\
                (fn, ln, dept, sal))
    rows=cur.fetchall()
    con.close()
    return rows


def updt(mid, fn="", ln="", dept="", sal=0):
    con=sqlite3.connect("emps.db")
    cur=con.cursor()
    cur.execute("UPDATE emp\
         SET fn=?, ln=?, dept=?, sal=?\
             WHERE id=?", (fn,ln,dept,sal,mid))
    con.commit()
    con.close()

#Creation et connection a la base de donnees
connect_db()