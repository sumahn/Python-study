class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Flyable, Unit):
    def __init__(self):
        # super().__init__() # 다중 상속의 경우 첫 번째 나오는 부모 클래스를 상속받는다.
        Unit.__init__(self)
        Flyable.__init__(self) # 다중 상속을 할 때는 부모 class를 직접 적어준다.
# 드랍쉽
dropship = FlyableUnit()