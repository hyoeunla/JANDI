# 생일

n = int(input())
student = []
for _ in range(n):
    student.append(input().strip().split())
student.sort(key=lambda x: (-int(x[3]), -int(x[2]), -int(x[1])))
print(student[0][0])
print(student[len(student)-1][0])
