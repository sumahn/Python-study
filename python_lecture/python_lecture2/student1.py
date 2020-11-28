import Student

students = []
with open("students.csv", "r", encoding='cp949') as file:
    for i, line in enumerate(file):
        if i == 0: continue
        students.append( Student.Student(line) )

students.sort(key=lambda stu:stu.score, reverse=True)
m = map(lambda stu: stu.make_grade(), students)
list(m) # 이걸 해줘야 students에 적용됨

print("이름\t""성별\t""나이\t""성적")
print("----\t""----\t""----\t""----")    
for s in students:
    print(s)
