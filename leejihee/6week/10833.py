# 10833. 사과
school = int(input())
sum = 0

for i in range(school):
    student, apple = map(int, input().split())
    a = apple % student  # 학생에게 나눠주고 남은 사과
    sum += a  # 시과의 합을 구함
print(sum)
