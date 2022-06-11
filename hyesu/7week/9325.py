# 얼마?

n = int(input())
for i in range(n):
    s = int(input())
    c = int(input())
    for j in range(c):
        q, p = map(int, input().split())
        s += q * p
    print(s)
