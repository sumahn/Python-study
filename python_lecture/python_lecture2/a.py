class TestClass:
    name = "TEST"

    @staticmethod
    def static_method():
        print("STATIC!!")

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

# hash, id 
print(hash(test), id(test))
# getattr
a = getattr(test, 'get_name') # self가 붙어 있기 때문에 instance를 줘야 함.
b = getattr(TestClass, 'static_method') # static method는 class 그대로 가져올 수 있음.
a()
b()

print("1111>> ", child.get_name())

c = callable(test.get_name)
print("cccccccc>> ", c)

