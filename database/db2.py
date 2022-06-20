import sqlite3

conn = sqlite3.connect("todos.db", isolation_level= None) 
c = conn.cursor()

#테이블생성
c.execute("CREATE TABLE IF NOT EXISTS table1 (chatid integer, message text)")

#테이블 열 삽입
def insert(chatid, message):
  tuple_value =  (chatid, message)
  c.execute("INSERT INTO table1(chatid, message) VALUES(?,?)", tuple_value)

#테이블에 있는 데이터 조회(select) 및 불러오기
def fetch_all_list(chatid): 
  chatid = (chatid,)
  fetchall = c.execute('SELECT * FROM table1 WHERE chatid=?',chatid).fetchall()
  try:
    newlist = [todo[1] for todo in fetchall]
    return newlist
  except IndexError:
      return "The database is empty already"


#데이터 삭제하기
#테이블에 있는 특정 데이터를 지우려면 WHERE과 DELETE를 조합
def delete(chatid, message):
  tuple_value =(chatid, message) 
  c.execute("DELETE FROM table1 WHERE chatid=? and message=?", tuple_value)

#chat id에 딸린 데이터 전부 삭제하기
def reset(chatid):
  chatid = (chatid, )
  c.execute("DELETE FROM table1 WHERE chatid=?", chatid) #보완필요?????


