import time
from tkinter import *
import tkinter.ttk as ttk
####### 기본 프레임 #######
root = Tk()
root.title("Suman GUI") # 제목
root.geometry("640x480+500+150") # 가로 x 세로 + X좌표 + Y좌표


####### 프로그레스 바 #######
# 진행 상태 표시
# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(10) # 10 ms 마다 움직임
# progressbar.pack()

# ####### 버튼 활용 #######
# def btncmd():
#     progressbar.stop() # 작동 중지하면서 값이 사라짐
 

# btn = Button(root, text="중지", command=btncmd)
# btn.pack()


p_var2 = DoubleVar() # 진행 상태가 %로 올라가기 때문에 실수도 반영하기 위해 DoubleVar 사용
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)


progressbar2.pack()

def btncmd2():
    for i in range(1, 101): # 1 ~ 100 
        time.sleep(0.01) # 0.01초 대기

        p_var2.set(i) # progress bar의 값 설정
        progressbar2.update() # for 문 돌아갈 때마다 GUI update
        print(p_var2.get())

btn = Button(root, text="시작", command=btncmd2)
btn.pack()

root.mainloop() # 창이 닫히지 않도록