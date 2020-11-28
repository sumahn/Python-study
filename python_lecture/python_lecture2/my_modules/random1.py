import random
print(dir(random))
print( random.randrange(6))

lst = [1,2,3,4,5]
random.shuffle(lst)
print(lst)

lst = list(range(1, 14))
print(lst, type(lst))
random.shuffle(lst)
print(lst)

fam_names = list("김이박최강고윤엄한배성백전황서천방지마피")
sung = random.choice(fam_names)
print(sung)
random.random()
random.randrange(1, 10)
random.uniform(1, 10) # a, b 사이의 랜덤 실수
random.sample(lst, k=3)