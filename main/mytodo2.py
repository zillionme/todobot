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

# res = requests.get(url)
# # content = res.text
#   #load함수 : kakao변수 = json파일에 저장된 데이터를 읽어서 파이썬 객체로 불러오고 싶은 경우.
#   #loads함수 : JSON 문자열을 Python 객체로 변환

# with open("content.json", "r") as telebot :
#   content = json.load(telebot)  

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
#reply_markup다.
# https://api.telegram.org/bot{TOKEN}/sendmessage?text={MESSAGE}&chat_id={CHATID}&reply_markup={KEYBOARD}
#   {"keyboard": [["Done","Done 3"], ["Update"], ["Log Time"]]}
#make keyboard함수의 매개변수 items는 키보드에 들어갈 내용들
#아마 키보드에 들어갈 내용(items) 받고, item으로 리스트화 시킨다음에
#딕셔너리 reply는 키보드 속성에, item들 넣고
# reply는 json문자열로 변환 

#텔레그램 키보드 만들기
def make_keyboard(todos):
  keyboard =[]
  for todo in todos:
    keyboard.append([todo])
  reply_markup = {"one_time_keyboard": True, "keyboard": keyboard }
  return json.dumps(reply_markup) 
  #dumps함수 = Python 객체를 JSON 문자열로 변환 


#문자 전송하기. 세번째 인자는 (키보드 위한 텔레그램 봇)인자
#chat id에게 메세지message를
#keyboard에 뭔가 잇다면 reply에 새 items 추가하고
#url에 들은 내용 가져오기
def send_message (chatid, message, reply_markup=None):
  bot.sendMessage(chat_id=chatid,text=message, reply_markup=reply_markup)


#업데이트된 아이디가(채팅마다 붙는 번호) 서서히 증가한다면,
# 이미 읽은 업데이트아이디를 변수로 할당하고, 같은 메세지를 계속 프린트하는 것을 멈춘다.

def todobot():
  old_update_id = 0         #latest_update_id
  print(url)
  db = database() 
  db.create_db()  
