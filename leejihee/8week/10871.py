# 10871. X보다 작은 수
n, m = map(int, input().split())
num = list(map(int, input().split()))

result = []
for i in num:
    if i < m:
        result.append(i)
print(*result)
