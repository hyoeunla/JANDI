# [10984] 내 학점을 구해줘
T = int(input())
for i in range(T):
    N = int(input())
    c = 0
    g = 0
    for i in range(N):
        C, G = map(str, input().split())
        c += int(C)
        g += float(C)*float(G)
    g = round(g/c, 1)
    print(c, g)
