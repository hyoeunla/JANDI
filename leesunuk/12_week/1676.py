# 팩토리얼 0의 개수

n = int(input())
np = 1
count = 0
for i in range(1, n+1):
    np *= i
np = list(str(np))
for i in range(len(np)-1, 0, -1):
    if np[i] == '0':
        count += 1
    else:
        break
print(count)
