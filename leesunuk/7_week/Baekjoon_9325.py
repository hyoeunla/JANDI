# 얼마?
n = int(input())
for i in range(n):
    car = int(input())
    opt = int(input())
    c = 0
    for j in range(opt):
        a, b = map(int, input().split())
        c += a*b
    print(car+c)
