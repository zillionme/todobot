# 참고 : https://hleecaster.com/python-sqlite3/
#참고2 : https://www.naragara.com/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%98%88%EC%A0%9C-%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8%EB%A1%9C-%EC%95%8C%EC%95%84%EB%B3%B4%EB%8A%94-sqlite3-%EA%B8%B0%EC%B4%88-%EC%82%AC%EC%9A%A9%EB%B2%95/

import sqlite3

# print(sqlite3.version)    #라이브러리 버전 2.6.0
# print(sqlite3.sqlite_version)    #sqlite(db엔진) 버전  3.35.5

#db 연결, 커서 획득
conn = sqlite3.connect("todos.db", isolation_level= None) #엑셀에서 첫행/ 윈도우에 파일 생성가능 
#isolation_level=None이라고 명시했는데 
# 이는 (실습을 위해) 쿼리문을 실행하여 DB에 즉시 반영, 즉시 자동 커밋을 하기 위함
#commit(커밋)은 “변경사항을 DB에 반영한다”는 뜻이라 commit을 하지 않으면 
# 수정(추가/갱신/삭제 등) 작업에 대한 기록을 컴퓨터 메모리 같은 데 임시로 가지고 있을 뿐 실제로 DB에는 반영하지 않는다. 
# 최종적으로 DB를 수정을 하려면 마지막에 반드시 conn.commit()이라는 명령
#commit과 반대되는 개념으로 rollback(롤백)이 있다. 이전 이력으로 되돌린다는 뜻. conn.rollback()으로 명령

# 파이썬에서 파일을 읽고 쓰려면 커서를 가져와야 한다. 
# 그래서 conn.cursor()로 일단 커서를 생성
#DBMS에서는 보통 SQL 구문을 호출해서 데이터를 조작하게 되는데 
# SQL 구문을 호출하려면 Cursor객체가 필요
c = conn.cursor()

#테이블을 만들 때는 다음과 같이 SQL 구문을 사용합니다. 
# 'CREATE TABLE'은 테이블을 만든다는 SQL 구문이고 kakao는 테이블의 이름입니다. 
# 함수의 인자와 같은 부분은 각각 칼럼 이름과 칼럼 데이터 타입을 기술하는 부분

# 테이블 생성 (데이터 타입은 TEST, NUMERIC, INTEGER, REAL, BLOB 등)
# CREATE TABLE IF NOT EXISTS 테이블이름 
# =테이블_이름이라는 테이블이 없으면 테이블을 생성해라
# (안에 문자열로 필드(열) 이름과 데이터 타입을 작성)
c.execute("CREATE TABLE IF NOT EXISTS table1 (chatid integer, message text)")


# 테이블 삽입
#c.execute(“INSERT INTO table1 VALUES()”)라고 해서 값 직접 삽입
#정석으로 데이터를 삽입하려면 아래와 같이 튜플로
#c.execute("INSERT INTO table1(id, name, birthday) \
#    VALUES(?,?,?)", \
#    (2, 'KIM', '1990-00-00'))
#tuple_value = ((1,1),(2,2)) 튜플형태의 데이터 세트 한번에 삽입도 가능
def insert(chatid, message):
  tuple_value =  (chatid, message)
  c.execute("INSERT INTO table1(chatid, message) VALUES(?,?)", tuple_value)

#데이터 불러오기
#데이터 조회 select
#데이터를 모두 선택한 다음에 c.fetchone() 한줄씩 출력(한개의row만 출력)
#c.fetchall()이라는 걸 사용해서 
# 전체를 가져와서 출력하더라도 이미 읽은 지점 이후에 있는 것들만 출력(모든 행 다)
# 예) print(c.fetchone())
#     print(c.fetchall())
# 그래서 만약 전체 데이터를 출력하고 싶다면 이렇게 전체를 다시 읽어 놓고 해야 한다.
# c.execute("SELECT * FROM table1")
# print(c.fetchall())
#리스트 형태로 출력. 반복문을 돌 수 있다.  예) [(2, 'KIM')] 이렇게 출력됨
# c.execute("SELECT * FROM table1")
# for row in c.fetchall():
#     print(row)

#데이터 조회하기(필터링) : 원하는 데이터만 찾아서 가져오기
#포메팅하거나 딕셔너리 형식으로 가져온다 

# param1=(2,)
# c.execute('SELECT * FROM table1 WHERE chatid=?',param1)
# print("param1", c.fetchall())
# 결과 >>> param1 [(2, 'KIM'), (2, 'kim'), (2, 'kim')]

def fetch_all_list(chatid): 
  chatid = (chatid,)
  fetchall = c.execute('SELECT * FROM table1 WHERE chatid=?',chatid).fetchall()
  try:
    #new리스트 안에, message 다 넣어서 return
    newlist = [todo[1] for todo in fetchall]  #fetchall에서 todo는 튜플(1,"kim"), todo[1]은 인덱스 지칭.
    return newlist
  except IndexError:
    return "The database is empty already"

#데이터 삭제하기
#테이블에 있는 특정 데이터를 지우려면 WHERE과 DELETE를 조합
def delete(chatid, message):
  tuple_value =(chatid, message) 
  c.execute("DELETE FROM table1 WHERE chatid=? and message=?", tuple_value)

# #test
# insert(1, "김은혜")
# insert(2, "이윤서")
# insert(2, "이은혜")
# insert(2, "이상한")
# insert(3, "조정순")
# insert(3, "조정환")

# print(fetch_all_list(2))
# delete(2, 'kim')

# c.execute("SELECT * FROM table1 WHERE chatid= 2")
c.execute("DELETE FROM table1 WHERE chatid=?", (2,))
c.execute("SELECT * FROM table1")
print(c.fetchall())
# 뒤에 rowcount를 붙여주면 지운 행 개수를 돌려준다.
# print(conn.execute("DELETE FROM table1").rowcount)