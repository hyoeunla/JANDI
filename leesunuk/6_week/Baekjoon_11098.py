n = int(input())
pick = []
for i in range(n):
    p = int(input())
    for j in range(p):
        member = list(input().split())
        member[0] = int(member[0])
        if j == 0:
            a = member
        else:
            if a[0] < member[0]:
                a = member

    pick.append(a)


for i in range(0, n):
    print(pick[i][1])
