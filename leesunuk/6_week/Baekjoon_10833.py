# 사과

n = int(input())
c = 0
for i in range(n):
    a, b = map(int, input().split())
    c += (b % a)
print(c)
