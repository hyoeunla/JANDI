# 게임 개발
n, m = map(int, input().split())
a, b, direction = map(int, input().split())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))  # 육지(0), 바다(1) 받기
dx = [0, 1, 0, -1]  # 북동남서 x축
dy = [1, 0, -1, 0]  # 북동남서 y축
board[a][b] = 1     # 시작위치 등록
count = 1           # 등록 수 세기
d = 0               # 방향
while True:
    direction -= 1            # 바라보는 방향
    if direction < 0:         # 0~3까지 순환
        direction = 3
    nowX = a + dx[direction]    # 옮긴 위치 : a + 바라보는 방향
    nowY = b + dy[direction]    # 옮긴 위치 : b + 바라보는 방향
    if board[nowX][nowY] == 0:  # 옮긴 위치가 육지(0)라면
        board[nowX][nowY] = 1   # 옮긴 위치 등록
        a, b = nowX, nowY
        count += 1              # 등록 수 세기
        d = 0
    else:                    # 옮긴 위치가 바다(1)면
        d += 1               # 제자리에서 돌아보기
    if d == 4:               # 북동남서 4번 돌았을 때
        nowX = a - dx[direction]  # 이전 위치로 이동
        nowY = b - dy[direction]
        if board[nowX][nowY] == 0:
            a, b = nowX, nowY
        else:
            break
print(count)
