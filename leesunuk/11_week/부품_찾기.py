# 부품 찾기
N = int(input())
Nlist = input().split()
M = int(input())
Mlist = input().split()

for i in Mlist:
    on = 0
    for j in Nlist:
        if i == j:
            on = 1
    if on == 1:
        print("yes", end=" ")
    else:
        print("no", end=" ")
