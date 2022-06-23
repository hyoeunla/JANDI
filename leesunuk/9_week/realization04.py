# 게임 개발
N, M = map(int, input().split())
x, y, way = map(int, input().split())
field = [[]for _ in range(M)]


for i in range(M):
    field1 = list(map(int, input().split()))
    for j in range(N):
        field[i].append(field1[j])
count = 0
i = 1

while i != 0:
    if y+1 >= N:
        y -= 1
    elif y-1 <= N:
        y += 1
    elif x+1 >= M:
        x -= 1
    elif x-1 <= M:
        x += 1
    if way == 0:
        if field[y+1][x] == 0:
            field[y][x] = 2
            y += 1
            count += 1
        elif field[y-1][x] == 0:
            field[y][x] = 2
            y -= 1
            count += 1
        if field[y][x+1] == 0:
            field[y][x] = 2
            x += 1
            count += 1
        elif field[y][x-1] == 0:
            field[y][x] = 2
            x -= 1
            count += 1
        else:
            i = 0

    elif way == 1:
        if field[y][x+1] == 0:
            field[y][x] = 2
            x += 1
            count += 1
        elif field[y][x-1] == 0:
            field[y][x] = 2
            x -= 1
            count += 1
        if field[y+1][x] == 0:
            field[y][x] = 2
            y += 1
            count += 1
        elif field[y-1][x] == 0:
            field[y][x] = 2
            y -= 1
            count += 1
        else:
            i = 0

    elif way == 2:
        if field[y][x-1] == 0:
            field[y][x] = 2
            x -= 1
            count += 1
        elif field[y][x+1] == 0:
            field[y][x] = 2
            x += 1
            count += 1
        if field[y+1][x] == 0:
            field[y][x] = 2
            y += 1
            count += 1
        elif field[y-1][x] == 0:
            field[y][x] = 2
            y -= 1
            count += 1
        else:
            i = 0

    elif way == 3:
        if field[y-1][x] == 0:
            field[y][x] = 2
            y -= 1
            count += 1
        elif field[y+1][x] == 0:
            field[y][x] = 2
            y += 1
            count += 1
        if field[y][x+1] == 0:
            field[y][x] = 2
            x += 1
            count += 1
        elif field[y][x-1] == 0:
            field[y][x] = 2
            x -= 1
            count += 1
        else:
            i = 0

print(count)
