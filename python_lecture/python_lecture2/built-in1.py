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

# zip - 두 개의 x, y값을 좌표로 표현하는 함수
l1 = [1,2,3]
l2 = [4,5,6]
z = zip(l1, l2)
list(z)

## 갯수가 맞지 않는 zip - 데이터 유실
l3 = [7,8]
z1 = zip(l1, l3)
list(z1)

# filter() function
## filter(filter_fn, iter): filter object
## TRUE인 것만 반환
int_numbers = range(-5,6)
print(list(int_numbers))

negatives = filter(lambda x: x < 0, int_numbers) # object의 주소 제공
print(list(negatives))

# lambda 값을 함수로 쓴다면...
def fn(x): # 뒤에 제공되는 것이 x
    return x < 0 # (condition logic)

n2 = filter(fn, int_numbers)
list(n2)

# map() function
## map(mapped_fn, iter) : map object
def make_double(n):
    return n * 2

numbers = (1, 2, 3, 4)
double_numbers = map(make_double, numbers)
print(list(double_numbers))

triple_numbers = map(lambda x: x * 3, numbers)
print(list(triple_numbers))

# reduce() function
## reduce(reduce_fn, iter) : one_result
from functools import reduce

product = 1
lst = [1, 2, 3, 4]
for num in lst:
    product = product * num
print("product1>>> ", product)

product2 = reduce(lambda x, y: x * y, lst)
print("proudct2>>> ", product2)

# sorted(), reversed()
numbers = [5, 3, 4, 2, 1]
sort_numbers = sorted(numbers)
print("sort_numbers= ", sort_numbers)
print("numbers=", numbers)

numbers.sort()
numbers