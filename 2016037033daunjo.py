# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 16:28:23 2020

@author: DaunJO


정보통신공학부 2016037033 조다운
2020-1 충북대학교 파이썬프로그래밍 프로젝트
"""


from tkinter import *
import time
import tkinter.font

s = 0 #second 변수
m = 0 #minute 변수
h = 0 #hour 변수
laps = [] #lap 타임을 담을 리스트 
listbox = 0 #lap 타임을 출력할 리스트박스
running = None

    
def start(): #start함수
    global s,m,h,running,laptime #변수 선언
    if s < 59: #s<59이면
        s += 1 #s를 하나 증가시킨다
        timeTxt.config(text=('%02d:%02d:%02d')%(h,m,s))
    else: #1분이 되면
        s = 0 #s를 0으로 바꾸고
        if m < 59:
            m += 1 #m를 하나 증가 시킨다
            timeTxt.config(text=('%02d:%02d:%02d')%(h,m,s))
        else: #60분이 되면
            m = 0 #m을 0으로 바꾸고
            h += 1 #h를 하나 증가 시킨다
            timeTxt.config(text=('%02d:%02d:%02d')%(h,m,s)) #"00:00:00"의 형식으로 h,m,s를 라벨에 출력한다
   # 시작 버튼 색상 변경, 중지 버튼 변경 원래대로 변경
    startButton = Button(window, text="Start   시작", bg="red", fg="white", font=font, command = start)# 시작 버튼 색상 빨간색으로 변경
    startButton.place(x = 0, y = 150, width=200, height=30)       
    stopButton = Button(window, text="Stop   중지", bg="#FBED6C", font=font, command = stop) # 중지 버튼 원래대로 변경
    stopButton.place(x = 200, y = 150, width=200, height=30)
    laptime = ('%02d:%02d:%02d')%(h,m,s) #랩 타임 출력을 위해 현재 타이머를 저장한다
    running = window.after(1000,start) #1000ms 후, 즉 1초 마다 after함수 호출하고 running 변수에 저장
    

def stop(): #stop함수
    global running 
    window.after_cancel(running) #start 호출 루프 중지
    running = None # running 비우기
    # 시작 버튼 색상 원래대로 변경, 중지 버튼 색상 변경
    startButton = Button(window, text="Start   시작", bg="#F19090", font=font, command = start)  # 시작 버튼 색상 원래대로 변경
    startButton.place(x = 0, y = 150, width=200, height=30)
    stopButton = Button(window, text="Stop   중지", bg="red", fg="white", font=font, command = stop) # 중지 버튼 빨간색으로 변경
    stopButton.place(x = 200, y = 150, width=200, height=30)
    
def reset(): #reset 함수
    global s,m,h,time1,running,time2,laptime, label
    try:
        stop() #stop함수 호출
    except: #예외처리
        start()
        stop()
    timeTxt.config(text='00:00:00') #스톱워치 초기화 하기
    s = 0
    m = 0
    h = 0
    laps = []   
    laptime= '00:00:00'
    listbox.delete(0, END) #리스트 박스 비우기
    #버튼 색상 원래대로 변경하기
    startButton = Button(window, text="Start   시작", bg="#F19090", font=font, command = start) # 시작 버튼 , start 함수 
    startButton.place(x = 0, y = 150, width=200, height=30)

    stopButton = Button(window, text="Stop   중지", bg="#FBED6C", font=font, command = stop) # 중지 버튼, stop함수 호출
    stopButton.place(x = 200, y = 150, width=200, height=30)
    
def lap(): #lap 함수
    global laptime
    if running is not None: #running이 None 이 아닐 때, 스톱워치가 start중 일 때
        laps.append(laptime)#현재 타이머 시간 lap 리스트에 추가
        listbox.insert(END, laps[-1]) # 리스트박스 END 위치에 항목 추가
        listbox.yview_moveto(1)  #세로 스크롤 이동하기



window = Tk() #Tk 클래스 객체 widdow 생성
window.title("2016037033조다운") #title 설정
window.configure(background=("#FAD6DB")) #배경색 설정
window.geometry("810x600") #window 사이즈 설정


font = tkinter.font.Font(family = "빙그레체Ⅱ", size=20, weight="bold") #기본 폰트 설정

timeTxt = Label(window, text="00:00:00", fg='#DAE8FC', bg = '#7DA5DE', font=("에스코어 드림 8 Heavy", 80))
#타이머 출력할 라벨 timeTxt 
timeTxt.place(x = 150, y = 20, width=500, height=120) #timeTxt place



startButton = Button(window, text="Start   시작", bg="#F19090", font=font, command = start) # 시작 버튼 , start 함수 
startButton.place(x = 0, y = 150, width=200, height=30) #startButton place

stopButton = Button(window, text="Stop   중지", bg="#FBED6C", font=font, command = stop) # 중지 버튼, stop함수 호출
stopButton.place(x = 200, y = 150, width=200, height=30) #stopButton place

resetButton = Button(window, text="Reset   초기화", bg="#82D896", font=font, command = reset) # 리셋 버튼, reset 함수 호출
resetButton.place(x = 400, y = 150, width=200, height=30) #resetButton place

lapButton = Button(window, text="Lap   랩", bg="#DB9AFC", font=font, command = lap) #랩 버튼, lap함수 호출
lapButton.place(x = 600, y = 150, width=200, height=30) #lapButton place

l = Label(window, text="Lap Time", fg='#DAE8FC', bg = '#7DA5DE', font=font) # lap time 라벨
l.place(x=320,y=200, width=150) #라벨 place

scrollbar = Scrollbar(window, orient="vertical") #listbox를 위한 스크롤바
listbox = Listbox(window, width=50, height=20, yscrollcommand=scrollbar.set) #listbox 세로 스크롤 위젯 적용
listbox.place(x=220,y=250) #listbox place
scrollbar.pack(side=RIGHT, fill="y") #스크롤바 pack
scrollbar.config(command=listbox.yview) #스크롤바 세로 스크롤 연결

window.mainloop() 

