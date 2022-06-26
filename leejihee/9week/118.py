# 3. 게임 개발
n, m = map(int, input().split())

visit = [[0] * m for _ in range(n)]  # 방문 위치를 저장하기 위한 맵
x, y, d = map(int, input().split())
visit[x][y] = 1

gameMap = []
for i in range(n):
    gameMap.append(list(map(int, input().split())))

# 북 동 남 서 = 상 우 하 좌
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3


count = 1  # 현재 위치 포함
turn_time = 0
while True:
    turn_left()
    nx = x+dx[d]
    ny = y+dy[d]

    if visit[nx][ny] == 0 and gameMap[nx][ny] == 0:
        visit[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else:  # 막혔을 때 1씩 더함
        turn_time += 1

    if turn_time == 4:  # 사방이 막혔을 때
        nx = x-dx[d]
        ny = y-dy[d]
        if gameMap[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break
        turn_time = 0
print(count)
