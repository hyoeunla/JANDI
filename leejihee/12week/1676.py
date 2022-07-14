# 1676. 팩토리얼 0의 개수
n = int(input())
result = 1
count = 0
for i in range(1, n+1):
    result *= i

result = str(result)

for j in reversed(result):
    if j == '0':
        count += 1
    else:
        break
print(count)
