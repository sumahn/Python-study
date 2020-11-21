# CLASS
class Dog:
    # constructor ; 생성자 
    # 객체가 생성되었음을 알리며 초기값을 지정해주는 단계
    def __init__(self, name):
        self.name = name
        print(self.name, "was Born")
    
    def speak(self):
        print("YELP!", self.name)

    def wag(self):
        print("Dog's wag tail")
    
    # __ 두 개를 사용하는 것은 서버에 사용하는 파이썬 내장 함수 
    # destructor ; 소멸자
    # 리소스 해제 등의 종료 작업을 하기 위해 사용 
    
    def __del__(self):
         print("destroy!!")





puddle = Dog("Bori")
sheperd = Dog("Ssal")

puddle.speak()
sheperd.speak()

del puddle
del sheperd



# INHERITANCE

class Puppy(Dog):

    def __init__(self, name):
        self.name = name
        self.color = "Red"
        print(self.name + " was born")

    # 앞에 __를 붙이면 class 내에서만 부를 수 있음.
    # 은닉화  
    def __read_diary(self):
        print("Diary content!!")

    def wag(self):
        self.__read_diary()

    def to():
        print("tooooooooooooooo@@@@@@")


d = Dog("puddle")
p = Puppy("sheperd")
d.wag()
p.wag()
d.speak()
p.speak()

p.__read_diary()


# STATIC METHOD ON CLASS

## Non self argument

class Dog:
    def m1(self):
        print("m1")

    # instance화 될 필요가 없음. 
    def m2():
        print("m2")
    
### class는 정적, instance는 동적 

class Calc:
    def plus(a,b):
        return a + b
    
calc1 = Calc()
calc1.plus(1,3) # error 
Calc().plus(1,3) # 성공

class Test:
    def test(self):
        print("Puppy's test")
        self.__q()

    def __q(self):
        print("qqqqqqqqqq")

test = Test()
test.__q()

