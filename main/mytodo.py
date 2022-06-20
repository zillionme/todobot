import requests,pprint,time
import json
from db3 import database

#pprint 모듈 : pretty josn 파일
#time 모듈 : 주기적으로 시간 다루기

#채팅창 정보 가져오기.
token = "I"
url = f"https://api.telegram.org/bot{token}/getUpdates"
# params(선택 사항)
# 튜플(tuple), 딕셔너리(dict)형식으로 매개변수에 넣으면 양식이 URL 인코딩이 되어 URL에 추가됩니다.
# URL?key=value&key1=value1

#정보가져오기 : 어떤 방식(method)의 HTTP 요청을 하느냐에따라 get, post,
# def get_url(url, params=None):
#   res = requests.get(url)
#   content = res.text #content.decode("utf8") = 바이너리 원문가져와서 utf8로 코딩
#   return content
  

res = requests.get(url)
content = res.text #content.decode("utf8") = 바이너리 원문가져와서 utf8로 코딩
  #load함수 : kakao변수 = json파일에 저장된 데이터를 읽어서 파이썬 객체로 불러오고 싶은 경우.
  #loads함수 : JSON 문자열을 Python 객체로 변환

content_json = res.json()   #정보를 json형태로 저장
#발행된 토큰 저장
with open("content.json","w") as telebot: #kakao는 현재 파일에서 쓰는 변수명 
  json.dump(content_json, telebot)  #파이썬의 token 객체를 kakao라는 json파일에 저장하기


# with open("content.json", "w") as content :
#   content_json = json.loads(content)  



