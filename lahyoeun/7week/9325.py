case = int(input())
for i in range(case):
    s = int(input())
    n = int(input())
    for j in range(n):
        q, p = map(int, input().split())
        s += p*q
    print(s)
