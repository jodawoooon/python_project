# 1. 주제 제시

​

###  -기존 문제

442p LAB. 스톱

워치 만들기


레이블을 사용하여 간단한 스톱워치를 작성하라. 시작 버튼을 누르면 시작되고, 중지 버튼을 누르면 스톱워치가 중지된다.

​

### -확장 문제

•단순히 시작, 중지 버튼을 가진 스톱워치에서 확장하여 

  시작, 중지, 리셋, 랩 기능을 가진 스톱워치를 구현한다.

  UI도 가독성 있게 변경

​

•선정 이유 : 위 기능들은 스톱워치에 꼭 필요한 기능이라고 생각하여 기존의 스톱워치 만들기 문제에서 해당 사항들을 추가해서 구현하면 유익할 것 이라고 생각했다.

​

# 2. 기능 요구사항

1.시작 버튼을 누르면 스톱워치가 시작한다

2.중지 버튼을 누르면 스톱워치가 중지된다

3.랩 버튼을 누르면 랩 타임이 출력된다.

4.시간은 00:00:00과 같이 초와 분을 나누어 출력한다.

5.리셋 버튼을 누르면 스톱워치를 초기화한다.

​

# 3. 설계

#### 필요한 변수

- S : second 변수

- M : minute 변수

- H : hour 변수

- Laps : 랩 타임을 담을 리스트

- Listbox : 랩을 출력할 리스트 박스

- Running : running 중 인지 아닌지 판별할 변수

- Laptime : 현재 타이머 시간을 저장할 변수

#### 레이아웃

- startButton : 시작 버튼

- stopButton : 중지 버튼

- resetButton : 리셋 버튼

- lapButton : 랩 버튼

- timeTxt : 타이머 출력할 라벨

- Listbox : 랩 리스트 출력할 리스트 박스

- Scrollbar : listbox를 위한 스크롤바

#### 메소드

- Start() 

- Stop()

- Reset()

- Lap()

​

# 4. 메소드 설계

▶ start()

•S<59이면 s+=1, s=59이면 s=0하고 m+=1

•M>59이면, m=0하고 h+=1한다

•“00:00:00”형식으로 h,m,s를 timeTxt 레이블에 config한다.

•After메소드 사용하여 1000ms(1초)마다 start 함수 호출

•Running 변수에 window.after(1000, start) 저장

•시작 버튼 빨간색으로 변경

​

▶ stop()

•Window.after_cancel(running)하여 start 호출 루프 중지함

•Running = None으로 변경

•중지 버튼 빨간색으로 변경함

​

▶ reset()

•Stop()함수 호출

•timeTxt 레이블, listbox, laptime, s,m,h 등 초기화

​

▶ lap()

•Running이 None이 아닐 때에만 lap 기능 수행 (start중 일 때)

•Laps 리스트에 현재 타이머 시간(laptime)을 추가한다

•Listbox에 laps 항목 추가

​

▶ main 함수

•Window창 생성 후 Title, 배경색, font 등 UI 설정

•timeTxt, startButton, stopButton, resetButton, lapButton, listbox 등 place하기

•Mainloop() : 윈도우 창을 윈도우가 종료될 때 까지 실행

​

# 5. 구현
[![](https://postfiles.pstatic.net/MjAyMDEyMDFfMTAw/MDAxNjA2ODA5NjgwODU5.y8cVtQ-PlT2o8qLZ1eXfiRg5IbJVgrGuwsI4iAMqGRwg.jKz6QhWUI-yrKErOm0ei72Z4AKNdevFUTAg8s9XJ9lEg.PNG.jodawooooon/image.png?type=w773)](https://blog.naver.com/PostList.nhn?blogId=jodawooooon&from=postList&categoryNo=14#)
[![](https://postfiles.pstatic.net/MjAyMDEyMDFfMTc5/MDAxNjA2ODA5NjY2MDIw.HnFMl0BS0-P6Q2RG5V4y4wfZztd7pfEn0C4ZG7lUejMg.HRl6sEN66hX8NSjAiKjw7P95135Ltwd3TXDbDbqzKEYg.PNG.jodawooooon/image.png?type=w773)](https://blog.naver.com/PostList.nhn?blogId=jodawooooon&from=postList&categoryNo=14#)
[블로그 주소](https://blog.naver.com/jodawooooon/222159630984 "블로그 주소")


​

