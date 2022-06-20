import requests,pprint,time
import json
import telegram
from db3 import database

#pprint 모듈 : pretty josn 파일
#time 모듈 : 주기적으로 시간 다루기

#채팅창 정보 가져오기.
token = "I"
url = f"https://api.telegram.org/bot{token}/getUpdates"
bot = telegram.Bot(token = token)

def get_updates():
  res= requests.get(url).json()
  return res


#사용자가 보낸 정보(텍스트 내용, 챗 아이디, 업데이트 아이디) 얻기
def latest_text_id():
  content= get_updates()
  if "message" in content["result"][-1]:  #key message가 있으면
    latest_text = content['result'][-1]['message']['text']  #문자내용
    latest_chat_id = content['result'][-1]['message']['from']['id'] #챗보낸 아이디
    latest_update_id = content['result'][-1]['update_id'] #문자 보낼때마다 +1 오르는 id(숫자)

  else:
    pass

  return (latest_text,latest_chat_id,latest_update_id)  

#텔레그램 키보드 만들기
def make_keyboard(todos):
  keyboard =[]
  for todo in todos:
    keyboard.append([todo])
  reply_markup = {"one_time_keyboard": True, "keyboard": keyboard }
  return json.dumps(reply_markup) 


#문자 전송하기.

def send_message (chatid, message, reply_markup=None):
  bot.sendMessage(chat_id=chatid,text=message, reply_markup=reply_markup)


#투두 봇
#첫 안내 / 시작기능, 할일 추가, 할일삭제, 안내창, 모두보기, 삭제기능, 모두삭제 기능/

def todobot():
  old_update_id = 0 #latest_update_id
  print(url)
  db = database()
  db.create_db() 

  while True:
    text,chat_id,last_update_id = latest_text_id() #latest_text_id() 함수는 최근 챗한 정보
    
    #할일 리스트 가져오기
    if last_update_id > old_update_id:
      todos_list = db.fetch_all_list(chat_id) #chat_id가 같은 데이터 베이스 가져오기

      #할일봇 시작하기
      if text == "/start":
        send_message(chat_id,"TODO봇을 시작합니다. 할 일을 입력해주세요")
      
            
      #할일 리스트 삭제하기
      elif text in todos_list:
        db.delete(chat_id, text) #데이타베이스에서 텍스트 삭제하기. 
        todos_list = db.fetch_all_list(chat_id) #데이타 베이스 다시 로드
        new_message='\n'.join(todos_list) 
        keyboard = make_keyboard(todos_list)

        #todo리스트가 빈값 아니면 키보드 보여주기
        if todos_list:
          send_message(chat_id, "<할일 목록>\n %s" %new_message ,keyboard)
        else:
          send_message(chat_id,"등록된 할일 목록이 없습니다. \n할 일을 입력해주세요")

        #todo리스트 추가하기
      else:
        print("text doesnt exist yet and its inserted")
        db.insert_in_db(chat_id,text) 
        todos_list = db.fetch_all_list(chat_id)
        new_message='\n'.join(todos_list) #할일 리스트문자열
        keyboard = make_keyboard(todos_list)
        print(todos_list)
        print(text)

        # bot.send_message(chat_id=chat_id, text="<할일 목록>\n%s"%new_message, reply_markup=keyboard)
    
        send_message(chat_id,"<할일 목록>\n%s" %new_message, keyboard)
      
      old_update_id=last_update_id

        
if __name__=="__main__": todobot()