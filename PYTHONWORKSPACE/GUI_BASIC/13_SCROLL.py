from tkinter import *


####### 기본 프레임 #######
root = Tk()
root.title("Suman GUI") # 제목
root.geometry("640x480+500+150") # 가로 x 세로 + X좌표 + Y좌표


####### 스크롤 #######
frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side="right", fill="y")

# set이 없으면 스크롤을 내려도 다시 올라옴
listbox = Listbox(frame, selectmode="extended", height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32): # 1 ~ 31
    listbox.insert(END, str(i)+"일")
listbox.pack(side="left")

# 리스트박스와 스크롤 매핑
scrollbar.config(command=listbox.yview)

root.mainloop() # 창이 닫히지 않도록