from tkinter import *

####### 기본 프레임 #######
root = Tk()
root.title("Suman GUI") # 제목
root.geometry("640x480+500+150") # 가로 x 세로 + X좌표 + Y좌표


####### 텍스트 #######
txt = Text(root, width=30, height=5)
txt.pack()

txt.insert(END, "글자를 입력하세요.")


####### 엔트리 #######
e = Entry(root, width=30)
e.pack()

e.insert(0, "한 줄만 입력하세요.") # 값이 비어 있으므로 END를 써도 동일하다. 


####### 버튼 활용 #######
def btncmd():
    # 내용 출력
    print(txt.get("1.0", END)) # 라인 1부터(1) , 0번째(.0) 인덱스로부터 끝까지(END) 가져와라        1: 첫번째 라인  0: 0번째 column 위치
    print(e.get())
    
    # 내용 삭제
    txt.delete("1.0", END)
    e.delete(0, END)
btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않도록