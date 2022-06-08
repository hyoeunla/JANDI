# [9325] 얼마?
T = int(input())
for i in range(T):
    s = int(input())
    n = int(input())
    for _ in range(n):
        q, p = map(int, input().split())
        s += q*p
    print(s)
