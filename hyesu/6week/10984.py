# 내 학점을 구해줘

t = int(input())
for i in range(t):
    a = int(input())
    h = 0
    p = 0
    for i in range(a):
        c, g = map(str, input().split())
        h += int(c)
        p += float(c) * float(g)
    p = round(p / h, 1)
    print(h, p)
