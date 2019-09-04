import sqlite3

con = sqlite3.connect('login.db', check_same_thread=False)
db = con.cursor()

def createTable():
    db.execute("""
    CREATE TABLE IF NOT EXISTS login(
        ID VARCHAR2(30) PRIMARY KEY,
        NAME VARCHAR2(50) NOT NULL,
        EMAIL VARCHAR2(30) NOT NULL,
        PHONE NUMBER(15) NOT NULL
    )
    """)
    #db.execute("""
    #CREATE TABLE IF NOT EXISTS loginBU AS SELECT * FROM login WHERE 1=1;
    #""")

def createUser(id,name,email,phone):
    db.execute("INSERT INTO login VALUES(?,?,?,?)",(id,name,email,phone))
    db.execute("INSERT INTO loginBU VALUES(?,?,?,?)",(id,name,email,phone))
    con.commit()


createTable()
