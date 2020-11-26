class TestClass:
    name = "TEST"

    @staticmethod
    def static_method():
        print("STATIC!!")
    
    @property # 함수가 아닌 property이다.
    def full_name(self):
        return self.name + " FFFF"

    def get_name(self):
        print("QQQQQQQQQQQ")
        return self.name

    def area(self, x, y):
        return x * y

class Child(TestClass):
    
    def get_name(self):
        super().get_name()
        return "Child Name: " + self.name

    def area(self, x, y):
        t = super().area(x, y)
        return t / 2


test = TestClass()
child = Child()

# @property
print(test.full_name) # 메소드로 부르는 것이 아닌 변수(property)임.

# @staticmethod
#test.static_method() 
## instance이니까 보이지 않는 self를 넣은 것임.
## @staticmethod를 선언하면 instance인 경우에도 사용할 수 있다.
TestClass.static_method()

# hash, id 
print(hash(test), id(test))

# getattr
a = getattr(test, 'get_name') # self가 붙어 있기 때문에 instance를 줘야 함.
b = getattr(TestClass, 'static_method') # static method는 class 그대로 가져올 수 있음.
a()
b()

print("1111>> ", child.get_name())

# callable
c = callable(test.get_name)
print("cccccccc>> ", c)

# byte, charset, encoding, ascii, latin1, cp949, euc-kr, utf8
s="한글"
s2 = bytes(s, "UTF8")
ord("한")
bytearray(s, 'utf-8')
bytearray(s, 'euc-kr')

