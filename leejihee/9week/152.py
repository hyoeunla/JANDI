# 4. 미로 탈출
from collections import deque

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))

dx = [-1, 1, 0, 0]  # 상하
dy = [0, 0, -1, 1]  # 좌우


def bfs(x, y):  # 넓이 우선 탐색
    queue = deque()  # 리스트 생성
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if maze[nx][ny] == 0:
                continue

            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[x][y]+1  # 하나씩 증가하여 마지막 위치의 값이 움직인 값이 됨
                queue.append((nx, ny))  # 좌표 추가 - 삭제 반복

    return maze[n-1][m-1]  # 마지막 위치 반환


print(bfs(0, 0))  # 처음 위치
