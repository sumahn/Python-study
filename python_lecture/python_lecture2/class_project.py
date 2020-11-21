# 사각형 클래스(1) - 내가 한 것  

## 사각형 클래스 자식 > 직사각형(가로, 세로), 평행사변형(밑변, 높이)

class quadrangle:

    # 사각형 클래스 초기화
    def __init__(self):
        self.area = 0
        self.bottom = 0
        self.height = 0
    
    # 넓이 구하는 공식
    def get_area(self, bottom, height):
        self.area = bottom * height
        
        return self.area

class rectangle(quadrangle):
    def __init__(self):
        self.area = 0
        self.bottom = 0
        self.height = 0

class parallelogram(quadrangle):
    def __init__(self):
        self.area=0
        self.bottom=0
        self.height=0 



# 사각형 클래스(2)

class Casting:
    def to_int(s):
        if type(s) == str:
            return int(s)
        else:
            return s


class quadrangle:

    def __init__(self):
        self.name = "quadrangle"
        print("quadrangle is created\n")

    def input_data(self):
        datum = input(self.msg) # 5,3
        data = datum.split(',')
        x, y = Casting.to_int(data[0]), Casting.to_int(data[1]) #['5','3']
        return self.__get_area(x,y)

    def __get_area(self, x, y):
        result = x * y
        print("{0}의 넓이는 {1}입니다.\n".format(self.name, result))

class rectangle(quadrangle):
    
    def __init__(self):

        self.name = "직사각형"
        self.msg = "가로와 세로는 (usage: 가로, 세로)  \n"
        print("rectangle is created")

class parallelogram(quadrangle):

    def __init__(self):
        self.name = "평행사변형"
        self.msg = "밑변과 높이는? (usage: 밑변, 높이)  \n"
        print("parallelogram is created")



while True:
    rect_type = input("사각형의 종류는 무엇입니까?\n(usage: 직사각형 >> 1  평행사변형 >> 2)\t (quit:q) \n>> ")
    if rect_type == 'q':
        break

    all_rects = [rectangle(), parallelogram()]
    rect_idx = Casting.to_int(rect_type) - 1
    rect = all_rects[rect_idx] 

    rect.input_data()
    