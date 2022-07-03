# 3.성적이 낮은 순서로 학생 출력하기
n = int(input())
studentList = []

for i in range(n):
    student = input().split()
    student[1] = int(student[1])
    studentList.append(student)
studentList.sort(key=lambda student: student[1])

for i in studentList:
    print(i[0], end=' ')
