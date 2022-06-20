# TO-DO LIST BOT
to-do-list chat bot (telegram)

 ## 실행 모습
1. 시작

![1](https://user-images.githubusercontent.com/100172683/174671377-daa3f46c-c577-42dd-8298-41cee67ce07a.gif)

2. 할일 입력

![Screen_Recording_20220621-015822_Telegram_3](https://user-images.githubusercontent.com/100172683/174671607-0ce4b04c-5118-41be-becf-0dbdb355abb0.gif)

3. 키보드 클릭시, 삭제

![Screen_Recording_20220621-015822_Telegram_6](https://user-images.githubusercontent.com/100172683/174671736-e8329abd-d45f-4dde-8d8b-4584c21213f2.gif)




##  프로젝트 목표
* 채팅창에서 TODOLIST 기능 사용
* 끝내지 못한 일들은 다음날 오전 9시에 자동으로 채팅방에 전송됨  



 ##  데이터 파이프 라인
*user -> telegrambot API -> WEBHOOK -> API GATEWAY -> LAMBDA FUNCTION 호출 ->  연동된 AWS RDS(Relational Database Service)*

![투두봇통신](https://user-images.githubusercontent.com/100172683/174668333-e6bae7d2-3fba-4723-b8d8-483aab847db1.png)

![투두봇 ec2222](https://user-images.githubusercontent.com/100172683/174676855-7a99591a-e9a3-436f-bb09-cebf10ea86cd.png)

![투두봇 rds](https://user-images.githubusercontent.com/100172683/174676687-bd8b297d-537c-47c0-a241-30cca0f48d13.png)




 ##  1차(test)

1. python sqlite3 모듈 사용해 데이터 베이스 구현
  -  데이터 베이스 생성 / 삽입/ 조회 및 가져오기/ 삭제하기/ 리셋하기 기능
  -  database() 클래스
  -  db.py 파일로 저장

2. main 
- 채팅창 정보(메시지, 챗아이디) get 방식으로 가져와 json파일로 저장
- 키보드 기능
- TODO 봇 기능 : 시작기능, 할일 추가, 할일삭제, 안내창, 모두보기, 삭제기능, 리셋 기능



 ##  2차

1. SQLITE -> MYSQL로 변경 (만 하면 됨)
2. RDS-데이터베이스 생성 후, 엔진 버전을 MYSQL로 지정
3. RDS - LAMBDA와 연결
4. (9시마다 알림 기능) LAMBDA 함수 따로 실행
