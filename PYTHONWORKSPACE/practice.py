# from random import *
# # import pickle

# # # profile_file = open("profile.pickle", "wb")
# # # profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]
# # # }
# # # print(profile)
# # # pickle.dump(profile, profile_file) # profile에 있는 정보를 file에 저장
# # # profile_file.close()

# # # profile_file = open("profile.pickle", "rb")
# # # profile = pickle.load(profile_file)
# # # print(profile)
# # # profile_file.close()

# # # with open("profile.pickle", "rb") as profile_file:
# # #     print(pickle.load(profile_file))


# # # for i in range(1, 51):
# # #     with open(str(i)+"주차.txt", "w", encoding="utf8") as report_files:
# # #         report_files.write("- {0} 주차 주간보고 -".format(i))
# # #         report_files.write("\n부서: ")
# # #         report_files.write("\n이름: ")
# # #         report_files.write("\n업무 요약: ")
        




# # # # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# # # name = "마린" # 유닛의 이름
# # # hp = 40 # 유닛의 체력
# # # damage = 5 # 유닛의 공격력

# # # print(f"{name} 유닛이 생성되었습니다.")
# # # print(f"체력{hp}, 공격력{damage}\n")


# # # # 탱크: 공격 유닛, 탱크, 포를 쏠 수 있는데, 일반 모드/시즈 모드
# # # tank_name = "탱크"
# # # tank_hp = 150
# # # tank_damage = 35

# # # print(f"{tank_name} 유닛이 생성되었습니다.")
# # # print(f"체력{tank_hp}, 공격력{tank_damage}\n")

# # # tank2_name = "탱크"
# # # tank2_hp = 150
# # # tank2_damage = 35

# # # print(f"{tank2_name} 유닛이 생성되었습니다.")
# # # print(f"체력{tank2_hp}, 공격력{tank2_damage}\n")


# # # def attack(name, location, damage):
# # #     print(f"{name} : {location} 방향으로 적군을 공격합니다. [공격력 {damage}]")

# # # attack(name, "1시", damage)
# # # attack(tank2_name, "1시", tank_damage)



# # # 클래스

# # # 일반 유닛
# class Unit:
#     def __init__(self, name, hp, speed):
#         # 파이썬 생성자
#         self.name = name
#         self.hp = hp
#         self.speed = speed
#         print("{0} 유닛이 생성되었습니다.".format(name))
        
#     def move(self, location):
#         # print("[지상 유닛 이동]")
#         print("{} : {} 방향으로 이동합니다. [속도 {}]"\
#             .format(self.name, location, self.speed))
    
#     def damaged(self, damage):
#         print(f"{self.name} : {damage} 데미지를 입었습니다.")
#         self.hp -= damage
#         print(f"{self.name} : 현재 체력은 {self.hp} 입니다.")

#         if self.hp <=0:
#             print(f"{self.name} : 파괴되었습니다.")

# # 공격 유닛
# class AttackUnit(Unit):
#     def __init__(self, name, hp, speed, damage):
#         Unit.__init__(self, name, hp, speed)
#         self.damage = damage
    
#     def attack(self, location):
#         print(f"{self.name} : {location} 방향으로 적군을 공격합니다. [공격력 {self.damage}]")

# # 날 수 있는 기능을 가진 클래스
# class Flyable():
#     def __init__(self, flying_speed):
#         self.flying_speed = flying_speed

#     def fly(self, name, location):
#         print(f"{name} : {location} 방향으로 날아갑니다. [속도 {self.flying_speed}]")

# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable):
#     def __init__(self, name, hp, damage, flying_speed):
#         AttackUnit.__init__(self, name, hp, 0, damage) # 지상 스피드 0
#         Flyable.__init__(self, flying_speed)

#     def move(self, location):
#         # print("[공중 유닛 이동]")
#         self.fly(self.name, location)


# # # 객체(instance)
# # # marine1 = Unit("마린", 40, 5)
# # # marine2 = Unit("마린", 40, 5)
# # # tank = Unit("탱크", 150, 35)

# # # 레이스: 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# # # wraith1 = Unit("레이스", 80, 5)
# # # print(f"유닛 이름: {wraith1.name}, 공격력 : {wraith1.damage}")

# # # # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것 (빼앗음)
# # # wraith2 = Unit("빼앗은 레이스", 80, 5)
# # # wraith2.clocking = True

# # # if wraith2.clocking == True:
# # #     print(f"{wraith2.name} 는 현재 클로킹 상태입니다.")

# # # 파이어뱃: 공격 유닛, 화염방사기
# # # firebat1 = AttackUnit("파이어뱃", 50, 16)
# # # firebat1.attack("5시")

# # # # 공격을 2번 받는다고 가정
# # # firebat1.damaged(25)
# # # firebat1.damaged(25)

# # # 메딕: 의무병

# # # 드랍쉽: 공중 유닛, 수송기, 마린 / 파이어뱃 / 탱크 등을 수송, 공격 불가

# # # 발키리: 공중 공격 유닛, 한번에 14발 미사일 발사
# # # valkyrie = FlyableAttackUnit("발키리", 200, 6, 5)
# # # valkyrie.fly(valkyrie.name, "3시")

# # # 벌쳐 : 지상 유닛, 기동성이 빠름
# # vulture = AttackUnit("벌쳐", 80, 10, 20)

# # # 배틀크루져 : 공중 유닛, 체력도 굉장히 좋음 ,공격력도 강함
# # battlecruiser = FlyableAttackUnit("배틀크루져", 500, 25, 3)

# # vulture.move("11시")
# # battlecruiser.move("9시")





# # 건물
# # class BuildingUnit(Unit):
# #     def __init__(self, name, hp, location):
# #         pass

# # # 서플라이 디폿 : 건물, 1개 건물 = 8 유닛. 
# # supply_depot = BuildingUnit("서플라이 디폿", 500, "7시")

# # def game_start():
# #     print("[알림] 새로운 게임을 시작합니다.")

# # def game_over():
# #     pass

# # game_start()
# # game_over()


# # super
# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         # Unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) # super를 할 때는 self를 쓰지 않고, ()를 붙여준다. 
#         self.location = location


# # 마린
# class Marine(AttackUnit):
#     def __init__(self):
#         AttackUnit.__init__(self, "마린", 40, 1, 5)

#     # 스팀팩 : 일정 시간 동안 이동 및 공격 속도를 증가, 체력 10 감소  
#     def stimpack(self):
#         if self.hp > 10:
#             self.hp -= 10
#             print("{} : 스팀팩을 사용합니다.".format(self.name))
#         else:
#             print("{} : 체력이 부족하여 스팀팩을 사용하지 않습니다.".format(self.name))

# # 탱크 
# class Tank(AttackUnit):
#     # 시즈모드 : 탱크를 지상에 고정시켜, 더 높은 파워로 공격 가능. 이동 불가
#     seize_developed = False # 시즈모드 개발여부

#     def __init__(self):
#         AttackUnit.__init__(self, "탱크", 150, 1, 35)
#         self.seize_mode = False

#     def set_seize_mode(self):
#         if Tank.seize_developed == False:
#             return 
        
#         # 현재 시즈모드가 아닐 때 -> 시즈모드
#         if self.seize_mode == False:
#             print("{} : 시즈모드로 전환합니다.".format(self.name))
#             self.damage *= 2
#             self.seize_mode = True

#         # 현재 시즈모드일 때 -> 시즈모드 해제 
#         else:
#             print("{} : 시즈모드를 해제합니다.".format(self.name))
#             self.damage /= 2
#             self.seize_mode = False


# # 레이스
# class Wraith(FlyableAttackUnit):
#     def __init__(self):
#         FlyableAttackUnit.__init__(self, "레이스",80, 20, 5)
#         self.clocked = False # 클로킹 모드 (해제 상태)

#     def clocking(self):
#         if self.clocked == True: # 클로킹 모드 -> 모드 해제
#             print("{} : 클로킹 모드 해제합니다.".format(self.name))
#             self.clocked = False
#         else:
#             print("{} : 클로킹 모드 설정합니다.".format(self.name))
#             self.clocked = True

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     print("Player : gg")
#     print("[Player] 님이 게임에서 퇴장하셨습니다.")




# # 실제 게임 진행 
# game_start()

# # 마린 3기 생성
# m1 = Marine()
# m2 = Marine()
# m3 = Marine()

# # 탱크 2기 생성
# t1 = Tank()
# t2 = Tank()

# # 레이스 1기 생성
# w1 = Wraith()

# # 유닛 일괄 관리
# attack_units = []
# attack_units.append(m1)
# attack_units.append(m2)
# attack_units.append(m3)
# attack_units.append(t1)
# attack_units.append(t2)
# attack_units.append(w1)

# # 전군 이동
# for unit in attack_units:
#     unit.move("1시")

# # 탱크 시즈모드 개발 
# Tank.seize_developed = True
# print("[알림] 탱크 시즈 모드 개발이 완료되었습니다.")

# # 공격 모드 준비 (마린 : 스팀팩, 탱크 : 시즈모드, 레이스 : 클로킹 모드)
# for unit in attack_units:
#     if isinstance(unit, Marine):
#         unit.stimpack()
#     elif isinstance(unit, Tank):
#         unit.set_seize_mode()
#     elif isinstance(unit, Wraith):
#         unit.clocking()

# # 전군 공격
# for unit in attack_units:
#     unit.attack("1시")

# # 전군 피해
# for unit in attack_units:
#     unit.damaged(randint(5, 21)) # 공격은 랜덤으로 받음 (5 ~ 20)

# # 게임 종료 
# game_over()









# 예외 처리 

try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append(int(input("첫 번째 숫자를 입력하세요 : ")))
    nums.append(int(input("두 번째 숫자를 입력하세요 : ")))
    # nums.append(int(nums[0]/nums[1]))
    print("{} / {} = {}".format(nums[0], nums[1], nums[2]))
except ValueError:
    print("에러! 잘못된 값을 입력하였습니다.")
except ZeroDivisionError as err:
    print(err)
except Exception as err:
    print("알 수 없는 에러가 발생하였습니다.")  
    print(err)
