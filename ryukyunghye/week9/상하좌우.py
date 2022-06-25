# 상하좌우
n = int(input())
start = list(map(str, input().split()))
now = [1, 1]
for i in start:
    if i == 'L':
        if now[1] > 1:
            now[1] -= 1
    elif i == 'R':
        if now[1] < n:
            now[1] += 1
    elif i == 'U':
        if now[0] > 1:
            now[0] -= 1
    elif i == 'D':
        if now[1] < n:
            now[0] += 1
print(now[0], now[1])
