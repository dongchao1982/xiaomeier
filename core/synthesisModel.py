#encoding=utf-8

import sqlite3

class synthesisModel(object):

    table_name = "synthesis"

    def __init__(self):
        self.db_name = "../data/voice.db"
        self.db_conn = sqlite3.connect(self.db_name)
        self.db_conn.text_factory = str
        cur = self.db_conn.cursor()
        sql = '''CREATE TABLE IF NOT EXISTS %s
                (id INTEGER PRIMARY KEY NOT NULL ,
                word TEXT NOT NULL ,
                filename VARCHAR(30) NOT NULL ,
                hit INT DEFAULT 0,
                create_time date,
                update_time date);''' % (synthesisModel.table_name)
        cur.execute(sql)
        self.db_conn.commit()

    def find(self,word):
        sql = '''SELECT filename FROM %s WHERE word = '%s';''' % (synthesisModel.table_name,word)
        cur = self.db_conn.cursor()
        cur.execute(sql)
        filename = cur.fetchone()
        self.db_conn.commit()
        if filename!=None:
            return filename[0]
        return None

    def insert(self,word,filename):
        sql = '''insert into %s (word, filename,create_time,update_time)
                  values (?,?,datetime('now'),datetime('now'))''' % (synthesisModel.table_name)
        para = (word,filename)
        cur = self.db_conn.cursor()
        cur.execute(sql,para)
        self.db_conn.commit()

    def updateHit(self,word):
        sql = '''UPDATE %s SET hit=hit+1,update_time=datetime('now') where word='%s';''' % (synthesisModel.table_name,word)
        cur = self.db_conn.cursor()
        cur.execute(sql)
        self.db_conn.commit()