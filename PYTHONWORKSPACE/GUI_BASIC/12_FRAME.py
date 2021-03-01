from tkinter import *


####### 기본 프레임 #######
root = Tk()
root.title("Suman GUI") # 제목
root.geometry("640x480+500+150") # 가로 x 세로 + X좌표 + Y좌표


####### 프레임 #######
Label(root, text="메뉴를 선택해주세요.").pack(side="top")
Button(root, text="주문하기").pack(side="bottom")

# 버거 프레임
frame_burger = Frame(root, relief="solid", bd=1) # relief : 테두리 모양, bd : 외곽선 표시 
frame_burger.pack(side="left", fill="both", expand=True)

Button(frame_burger, text="햄버거").pack()
Button(frame_burger, text="치즈버거").pack()
Button(frame_burger, text="치킨버거").pack()

# 음료 프레임 
frame_drink = LabelFrame(root, text="음료")
frame_drink.pack(side="right", fill= "both", expand=True) # expand : 펼쳐지도록 
Button(frame_drink, text="콜라").pack()
Button(frame_drink, text="사이다").pack()



root.mainloop() # 창이 닫히지 않도록