# 얼마?

run = int(input())
for i in range(run):
    s = int(input())
    n = int(input())
    for j in range(n):
        q, p = map(int, input().split())
        s += q * p
    print(s)
