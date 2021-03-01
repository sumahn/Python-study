from tkinter import *
import tkinter.ttk as ttk

####### 기본 프레임 #######
root = Tk()
root.title("Suman GUI") # 제목
root.geometry("640x480+500+150") # 가로 x 세로 + X좌표 + Y좌표


####### 콤보 박스 #######  
values = [str(i)+ "일" for i in range(1,32)] # 1 ~ 31 까지의 숫자
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set("카드 결제일") # 최초 목록 제목 설정 / 버튼 클릭을 통한 값 설정도 가능

readonly_combobox = ttk.Combobox(root, height=10, values=values, state="readonly") # height는 목록이 몇 개 보여지는가
readonly_combobox.current(0) # 0번째 인덱스 값 선택
readonly_combobox.pack()

####### 버튼 활용 #######
def btncmd():
    print(combobox.get()) # 선택된 값 표시 
    print(readonly_combobox.get())
btn = Button(root, text="선택", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않도록