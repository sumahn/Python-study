from tkinter import *

####### 기본 프레임 #######
root = Tk()
root.title("Suman GUI") # 제목
root.geometry("640x480+500+150") # 가로 x 세로 + X좌표 + Y좌표
root.resizable(False, False) # X(너비), Y(높이) 값 변경 불가 (창 크기 변경 불가)


root.mainloop() # 창이 닫히지 않도록