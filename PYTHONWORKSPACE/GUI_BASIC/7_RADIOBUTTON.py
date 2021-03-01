from tkinter import *

####### 기본 프레임 #######
root = Tk()
root.title("Suman GUI") # 제목
root.geometry("640x480+500+150") # 가로 x 세로 + X좌표 + Y좌표


####### 라디오 버튼 #######
# 여러 개 버튼 중 택 1 
Label(root, text="메뉴를 선택하세요.").pack()

burger_var = IntVar() # 여기에 int 형으로 값을 저장한다. 
btn_burger1 = Radiobutton(root, text="햄버거", value=1, variable=burger_var)
# btn_burger1.select()
btn_burger2 = Radiobutton(root, text="치즈버거", value=2, variable=burger_var)
btn_burger3 = Radiobutton(root, text="치킨버거", value=3, variable=burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()


Label(root, text="음료를 선택하세요.").pack()

drink_var = StringVar() # 문자로 반환하겠다.
btn_drink1 = Radiobutton(root, text="콜라", value="콜라", variable=drink_var) # burger_var로 쓰면 안된다. 
btn_drink1.select() # 기본값 선택
btn_drink2 = Radiobutton(root, text="사이다", value="사이다", variable=drink_var) # burger_var로 쓰면 안된다. 
btn_drink3 = Radiobutton(root, text="마운틴듀", value="마운틴듀", variable=drink_var) # burger_var로 쓰면 안된다. 

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()


####### 버튼 활용 #######
def btncmd():
    print(burger_var.get()) # 햄버거 중에서 선택된 라디오 항목의 값(value)를 출력 ex) 1, 2, 3
    print(drink_var.get()) # 음료 중에서 선택된 라디오 항목의 값을 출력
btn = Button(root, text="주문", command=btncmd)
btn.pack()

root.mainloop() # 창이 닫히지 않도록