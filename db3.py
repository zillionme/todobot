import sqlite3
from xml.etree.ElementTree import QName

class database:
  def __init__(self):
    self.conn = sqlite3.connect("todos.db")
    self.c = self.conn.cursor()
  
  def create_db(self):
    self.c.execute("CREATE TABLE IF NOT EXISTS table1 (chatid integer, message text)")
    

  def insert_in_db(self, chatid, message):
    tuple_value =  (chatid, message)
    self.conn.execute("INSERT INTO table1(chatid, message) VALUES(?,?)", tuple_value)

  def fetch_all_list(self, chatid):
    chatid = (chatid,)
    fetchall = self.c.execute('SELECT * FROM table1 WHERE chatid=?',chatid).fetchall()
    try:
      newlist = [todo[1] for todo in fetchall]
      return newlist
    except IndexError:
      return "The database is empty already"
  
  def delete(self, chatid, message): 
    tuple_value =(chatid, message) 
    self.c.execute("DELETE FROM table1 WHERE chatid=? and message=?", tuple_value)

  def reset(self, chatid):
    chatid = (chatid, )
    self.c.execute("DELETE FROM table1 WHERE chatid=?", chatid) 

