from tkinter import *

####### 기본 프레임 #######
root = Tk()
root.title("Suman GUI") 
root.geometry("640x480+500+150") # 가로 x 세로 + X좌표 + Y좌표


####### 레이블 #######
label1 = Label(root, text="안녕하세요.")
label1.pack()

# 이미지 넣어보기
photo = PhotoImage(file="PYTHONWORKSPACE/GUI_BASIC/img.png")
label2 = Label(root, image=photo)
label2.pack()

def change():
    label1.config(text="또 만나요.")

    global photo2 # Garbage Collection이 전역 변수로 만들지 않으면 메모리 공간에서 제거시켜서 global로 전역변수화 시켜야 한다. 
    photo2 = PhotoImage(file="PYTHONWORKSPACE/GUI_BASIC/img2.png")
    label2.config(image=photo2)

btn = Button(root, text="클릭", command=change)
btn.pack()



root.mainloop() # 창이 닫히지 않도록