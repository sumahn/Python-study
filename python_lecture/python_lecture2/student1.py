g_grades = ["A","B","C","D","F"]
g_grades.reverse()
class Student:

    # 초기화
    grade = ''
    def __init__(self, line):
        name, gender, age, score = line.strip().split(',')
        self.name = name
        self.gender = gender
        self.age = int(age)
        self.score = int(score)
    
    def __str__(self):
        return "{}**\t{}\t{}\t{}\t{}".format(self.name[0], self.gender, self.age, self.score, self.grade)

    def make_grade(self):
        if self.score == 100:
            self.grade = "A+"
        elif self.score < 50:
            self.grade = "F"
        else:
            self.grade = g_grades[(self.score // 10) - 5]
    


students = []
with open("students.csv", "r", encoding='cp949') as file:
    for i, line in enumerate(file):
        if i == 0: continue
        students.append( Student(line) )

students.sort(key=lambda stu:stu.score, reverse=True)
m = map(lambda stu: stu.make_grade(), students)
list(m) # 이걸 해줘야 students에 적용됨

print("이름\t""성별\t""나이\t""성적")
print("----\t""----\t""----\t""----")    
for s in students:
    print(s)
