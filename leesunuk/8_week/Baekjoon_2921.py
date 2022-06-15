# 도미노

n = int(input())
result = 0
for i in range(0, n+1):
    for j in range(0, n+1, 2):
        result += i+j

print(result)
