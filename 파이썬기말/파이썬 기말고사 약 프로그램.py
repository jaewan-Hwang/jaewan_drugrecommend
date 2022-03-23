##질환별 약 목록 프로그램
from tkinter import*
import tkinter.messagebox             ##메세지박스
import webbrowser                     ##링크걸기 라이브러리
import tkinter.ttk
import table

url1 = 'https://www.druginfo.co.kr/'  #druginfo링크
url2 = 'https://www.health.kr/'       #약학정보원 링크


window=Tk()


##함수정의                      
def b6():
    webbrowser.open(url1)    ##링크1실행 
def b7():
    webbrowser.open(url2)    ##링크2실행



##화면구성

window.title("증상별 약 추천 프로그램")
window.geometry("500x500")

P1 = PhotoImage(file = "mark.gif")
P2 = PhotoImage(file = "그림2.gif")
P3 = PhotoImage(file = "그림3.gif")
P4 = PhotoImage(file = "그림4.gif")
P5 = PhotoImage(file = "그림5.gif")


label0=Label(window, text="아픈증상을 골라주세요. 약을 추천해드릴게요!",font=("고딕체",15))
label1=Label(window, text="--------------어떤증상을 보이나요?--------------",font=("고딕체",13))
label2=Label(window, text="-----------더 많은 정보를 보고싶다면? ----------",font=("고딕체",13))
btn1=Button(window,image=P2,command= table.headtable)##머리아플때 버튼
btn2=Button(window,image=P3,command= table.mutable)##근육통버튼
btn3=Button(window,image=P4,command= table.smatable)##소화불량 버튼
btn4=Button(window,image=P5,command= table.colictable)##배가 아플때 버튼
btn5=Button(window, text="프로그램 종료", fg="red", command=quit)##종료버튼
btn6=Button(window,text='druginfo 홈페이지 바로가기',command=b6)
btn7=Button(window,text='약학정보원 홈페이지 바로가기',command=b7)




P_label1 = Label(image = P1)
P_label2 = Label(image = P2)
P_label3 = Label(image = P3)
P_label4 = Label(image = P4)
P_label5 = Label(image = P5)



##위젯위치설정

label0.pack()
label1.place(x=0, y=240, relx=0.5, anchor="s")
label2.place(x=0, y=400, relx=0.5, anchor="s")
P_label1.place(x=0, y=200, relx=0.5, anchor="s")##병원마크


btn1.place(x=50 , y=250, width=100 , height=100 )#버튼1
btn2.place(x=150 , y=250, width=100 , height=100 )#버튼2
btn3.place(x=250 , y=250, width=100 , height=100 )#버튼3
btn4.place(x=350 , y=250, width=100 , height=100 )#버튼4
btn5.place(x=0, y=480, relx=0.5, anchor="s")#종료버튼
btn6.place(x=70 , y=410)#druginfo홈페이지버튼
btn7.place(x=250 , y=410)#약학정보원홈페이지버튼



window.mainloop()



