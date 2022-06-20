# 상하좌우

n = int(input())
x, y = 1, 1
move = list(input().split())

for i in move:
    if x == 0:
        x += 1
    elif x > n:
        x -= 1
    if y == 0:
        y += 1
    elif y > n:
        y -= 1

    if n >= x >= 1 and n > y >= 1:
        if i == "U":
            x -= 1
        elif i == "D":
            x += 1
        elif i == "R":
            y += 1
        elif i == "A":
            y -= 1
print(x, y)
