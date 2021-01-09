import pickle

# profile_file = open("profile.pickle", "wb")
# profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]
# }
# print(profile)
# pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file = open("profile.pickle", "rb")
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

# with open("profile.pickle", "rb") as profile_file:
#     print(pickle.load(profile_file))


# for i in range(1, 51):
#     with open(str(i)+"주차.txt", "w", encoding="utf8") as report_files:
#         report_files.write("- {0} 주차 주간보고 -".format(i))
#         report_files.write("\n부서: ")
#         report_files.write("\n이름: ")
#         report_files.write("\n업무 요약: ")
        




# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린" # 유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print(f"{name} 유닛이 생성되었습니다.")
# print(f"체력{hp}, 공격력{damage}\n")


# # 탱크: 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반 모드/시즈 모드
# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print(f"{tank_name} 유닛이 생성되었습니다.")
# print(f"체력{tank_hp}, 공격력{tank_damage}\n")

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print(f"{tank2_name} 유닛이 생성되었습니다.")
# print(f"체력{tank2_hp}, 공격력{tank2_damage}\n")


# def attack(name, location, damage):
#     print(f"{name} : {location} 방향으로 적군을 공격합니다. [공격력 {damage}]")

# attack(name, "1시", damage)
# attack(tank2_name, "1시", tank_damage)



# 클래스

# 일반 유닛
class Unit:
    def __init__(self, name, hp, speed):
        # 파이썬 생성자
        self.name = name
        self.hp = hp
        self.speed = speed
        
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{} : {} 방향으로 이동합니다. [속도 {}]"\
            .format(self.name, location, self.speed))

# 공격 유닛
class AttackUnit(Unit):
    def __init__(self, name, hp, speed, damage):
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]\n")

    def damaged(self, damage):
        print(f"{self.name} : {damage} 데미지를 입었습니다.\n")
        self.hp -= damage
        print(f"{self.name} : 현재 체력은 {self.hp} 입니다.\n")

        if self.hp <=0:
            print(f"{self.name} : 파괴되었습니다.")

# 날 수 있는 기능을 가진 클래스
class Flyable():
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")

# 공중 공격 유닛 클래스
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0
        Flyable.__init__(self, flying_speed)

    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 객체(instance)
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank = Unit("탱크", 150, 35)

# 레이스: 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print(f"유닛 이름: {wraith1.name}, 공격력 : {wraith1.damage}")

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print(f"{wraith2.name} 는 현재 클로킹 상태입니다.")

# 파이어뱃: 공격 유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# # 공격을 2번 받는다고 가정
# firebat1.damaged(25)
# firebat1.damaged(25)

# 메딕: 의무병

# 드랍쉽: 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송, 공격 불가

# 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# valkyrie.fly(valkyrie.name, "3시")

# 벌쳐 : 지상 유닛, 기동성이 빠름
vulture = AttackUnit("벌쳐", 80, 10, 20)

# 배틀크루져 : 공중 유닛, 체력도 굉장히 좋음 ,공격력도 강함
battlecruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)

vulture.move("11시")
battlecruiser.move("9시")