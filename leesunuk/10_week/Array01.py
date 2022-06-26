# 위에서 아래로
n = int(input())
result = []
for i in range(n):
    result.append(int(input()))

result.sort(reverse=True)
print(result)
