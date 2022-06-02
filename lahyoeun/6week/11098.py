n = int(input())
player = []
for i in range(n):
    a = 0
    b = ""
    p = int(input())
    for j in range(p):
        cost, name = input().split()
        if int(cost) > a:
            a = int(cost)
            b = name
    player.append(b)

for i in range(0, n):
    print(player[i])
