import sqlite3

def connect():
    conn=sqlite3.connect("mydata.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS mydata (id INTEGER PRIMARY KEY,emaile text, passs text, types integer,note integer,datanow text)")
    conn.commit()
    conn.close()

def insert(emaile,passs,types,note,datanow):
    conn = sqlite3.connect("mydata.db")
    cur = conn.cursor()
    cur.execute("INSERT INTO mydata VALUES (NULL,?,?,?,?,?)",(emaile,passs,types,note,datanow))
    conn.commit()
    conn.close()

def View():
    conn = sqlite3.connect("mydata.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM mydata")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(emaile="",passs="",types="",note="",datanow=""):
    conn = sqlite3.connect("mydata.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM mydata WHERE emaile=? OR passs=? OR types=? OR note=?",( emaile,passs,types,note))
    rows = cur.fetchall()
    conn.close()
    return rows

def deleteitem(id):
    conn = sqlite3.connect("mydata.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM mydata WHERE id=?",(id,))
    conn.commit()
    conn.close()

def update(id, emaile,passs,types,note):
    conn = sqlite3.connect("mydata.db")
    cur = conn.cursor()
    cur.execute("UPDATE mydata SET emaile=?, passs=?, types=?, note=? WHERE id=?",( emaile,passs,types,note,id))
    conn.commit()
    conn.close()

connect()#automatically gets called when frontend file executed
