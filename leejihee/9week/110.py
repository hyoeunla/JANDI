# 4-1. 상하좌우
# 나의 풀이
n = int(input())
mv = input().split()
x, y = 1, 1

for i in mv:
    if i == 'R':
        if x < n:
            y += 1
    elif i == 'L':
        if x < 1:
            y -= 1
    elif i == 'U':
        if x > 1:
            x -= 1
    elif i == 'D':
        if y < n:
            x += 1
print(x, y)

# 해설
n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]  # 왼 오 위 아래
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):  # 4번 반복
        if plan == move_types[i]:  # [0]~[3]까지 입력한만큼 반복
            nx = x+dx[i]  # 'D'면 1+1
            ny = y+dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:  # 범위 체크
        continue
    x, y = nx, ny
print(x, y)
