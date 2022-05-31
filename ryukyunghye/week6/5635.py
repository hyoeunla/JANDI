# [5635] 생일
student = []
for _ in range(int(input())):
    name, day, month, year = input().split()
    student.append([name, int(day), int(month), int(year)])
student.sort(key=lambda a: (a[3], a[2], a[1]))
print(student[-1][0])
print(student[0][0])
