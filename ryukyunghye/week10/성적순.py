# 성적이 낮은 순서로 학생 출력하기
n = int(input())
student = []
for i in range(n):
    in_ = input().split()
    student.append((in_[0], int(in_[1])))
student = sorted(student, key=lambda student: student[1])
for i in student:
    print(i[0], end=' ')
