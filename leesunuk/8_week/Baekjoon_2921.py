# 도미노

n = int(input())
result, s = 0, 0
for i in range(0, n+1):
    for j in range(s, n+1):
        result += i+j
    s += 1

print(result)
