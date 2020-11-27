# sort해라 sorted 
numbers = [5, 3, 4, 2, 1]
sort_numbers = sorted(numbers)
print("sort_numbers= ", sort_numbers)
print("numbers=", numbers)

# number 리스트 자체를 sort
numbers.sort()
numbers

# sorting object
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    # 각각의 instance를 str로 변환하라.
    def __str__(self):
        return "{}:{}".format(self.name, self.score)


students = [
    Student("김일수",10),
    Student("김이수",20),
    Student("김삼수",30),
    ]

def print_students():
    print("-----------------------")
    for s in students:
        print(s)


sort_students = sorted(students, key = lambda stu: stu.score)
print_students()

students.sort(key=lambda stu:stu.score)
print_students()

students.sort(key=lambda stu:stu.score, reverse=True)
print_students()

def sort_key(stu):
    return stu.score

students.sort(key = sort_key, reverse=True)
print_students()

# make students.csv
with open("students.csv", "w") as file:
    print("Write mode")
    file.write("이름,성별,나이,성적\n")
    file.write("김일수,남,23,80\n")
    file.write("홍길순,여,25,75\n")
    file.write("박길동,남,45,55\n")
    file.write("최순식,남,34,90\n")
    file.write("강감찬,남,90,100\n")
    file.write("갑돌이,남,38,65\n")
    file.write("박삼순,여,31,70\n")
    file.write("김갑순,여,28,85\n")
    file.write("이갑순,여,28,85\n")
    file.write("이순신,남,88,89\n")
    print("The End!")