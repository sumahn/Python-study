from tkinter import *

####### 기본 프레임 #######
root = Tk()
root.title("Suman GUI") # 제목
root.geometry("640x480+500+150") # 가로 x 세로 + X좌표 + Y좌표


####### 리스트박스 #######
listbox = Listbox(root, selectmode="extended", height=0) # selectmode: single 일 경우 하나만 선택 가능하다. height 숫자만큼 보여줌(0일 경우에는 모두 다 보여줌)
listbox.insert(0, "사과")
listbox.insert(1, "딸기")
listbox.insert(2, "바나나")
listbox.insert(END, "수박")
listbox.insert(END, "포도")
listbox.pack()



####### 버튼 활용 #######
def btncmd():
    # 삭제
    # listbox.delete(0) # 맨 앞 항목 삭제

    # # 갯수 확인 
    # print("리스트에는", listbox.size(), "개가 있어요.")

    # # 항목 확인 (시작 idx, 끝 idx)
    # print("1번째부터 3번째까지의 항목: ", listbox.get(0,2))

    # 선택된 항목 확인 (위치로 반환 (ex) (1, 2, 3)) 
    print("선태된 항목: ", listbox.curselection())



btn = Button(root, text="클릭", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않도록