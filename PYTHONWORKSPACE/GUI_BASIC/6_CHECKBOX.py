from tkinter import *

####### 기본 프레임 #######
root = Tk()
root.title("Suman GUI") # 제목
root.geometry("640x480+500+150") # 가로 x 세로 + X좌표 + Y좌표


####### 체크박스 #######
chkvar = IntVar() # chkvar에 int 형으로 값을 저장한다. 
chkbox = Checkbutton(root, text="오늘 하루 보지 않기", variable= chkvar) # 체크 해제 했을 때의 값, 체크했을 때의 값
chkbox.select() # 자동 선택 처리
chkbox.deselect() # 선택 해제 처리
chkbox.pack()

chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text="일주일동안 보지 않기", variable= chkvar2) # variable에 chkvar를 똑같이 넣어주면 안 됨.
chkbox2.pack()

####### 버튼 활용 #######
def btncmd():
    print(chkvar.get()) # 0: 체크 해제, 1: 체크
    print(chkvar2.get())

btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않도록