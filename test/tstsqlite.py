#encoding=utf-8

import sqlite3

db_name = "tst.db"
db_conn = sqlite3.connect(db_name)
print "conn"

cur = db_conn.cursor()
tablename = 'synthesis'
sql = '''CREATE TABLE IF NOT EXISTS %s
              (id INTEGER PRIMARY KEY NOT NULL ,
              word TEXT NOT NULL ,
              filename VARCHAR(30) NOT NULL ,
              hit INT DEFAULT 0,
              create_time date,
              update_time date);''' % (tablename)
print sql
cur.execute(sql)
print "create table"

db_conn.commit()
db_conn.close();

