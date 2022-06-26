# 게임 개발

n, m = map(int, input().split())

d = [[0] * m for _ in range(n)]  # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
x, y, direction = map(int, input().split())  # 현재 캐릭터의 X좌표, Y좌표, 방향을 입력받기
d[x][y] = 1  # 현재 좌표 방문 처리

array = []  # 전체 맵 정보를 입력받기
for i in range(n):
    array.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]   # 북, 동, 남 , 서 방향 정의
dy = [0, 1, 0, -1]


def turn_left():  # 왼쪽으로 회전
    global direction
    direction -= 1
    if direction == -1:
        direction = 3


count = 1  # 시뮬레이션 시작
turn_time = 0
while True:

    turn_left()  # 왼쪽으로 회전
    nx = x + dx[direction]
    ny = y + dy[direction]

    if d[nx][ny] == 0 and array[nx][ny] == 0:  # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue

    else:     # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
        turn_time += 1

    if turn_time == 4:  # 네 방향 모두 갈 수 없는 경우
        nx = x - dx[direction]
        ny = y - dy[direction]

        if array[nx][ny] == 0:  # 뒤로 갈 수 있다면 이동하기
            x = nx
            y = ny

        else:   # 뒤가 바다로 막혀있는 경우
            break
        turn_time = 0

print(count)
