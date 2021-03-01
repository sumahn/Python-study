from tkinter import *

####### 기본 프레임 #######
root = Tk()
root.title("Suman GUI") 


####### 버튼 #######
btn1 = Button(root, text="버튼1")
btn1.pack() # pack() 함수로 호출해야만 버튼이 보인다.

btn2 = Button(root, padx=5, pady=10, text="버튼2") # 글자 수가 많아지거나 적어짐에 따라 크기가 달라진다.
btn2.pack()

btn3 = Button(root, padx=10, pady=5, text="버튼3")
btn3.pack()

btn4 = Button(root, width=10, height=3, text="버튼4") # 크기를 이미 정해줬기 때문에 글자 수에 상관없이 크기가 일정하다.
btn4.pack()

btn5 = Button(root, fg="red", bg="yellow", text="버튼5") # fg는 글자 색, bg는 배경 색
btn5.pack()

# 이미지를 통해 버튼 만들어보기
photo = PhotoImage(file="PYTHONWORKSPACE/GUI_BASIC/img.png")
btn6 = Button(root, image=photo)
btn6.pack()

def btncmd():
    print("버튼이 클릭되었습니다.")

btn7 = Button(root, text="동작하는 버튼", command=btncmd)
btn7.pack()


root.mainloop() # 창이 닫히지 않도록