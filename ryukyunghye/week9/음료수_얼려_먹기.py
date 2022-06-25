# 음료수 얼려 먹기
n, m = map(int, input().split())
mold = []
for _ in range(n):
    mold.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0


def dfs(start_x, start_y):
    # 현재 노드 방문 후 연결된 모든 노드 방문
    mold[start_x][start_y] = 1  # 현재 노드 방문처리
    for i in range(4):  # 인접 노드
        now_x = start_x + dx[i]
        now_y = start_y + dy[i]
        if 0 <= now_x < n and 0 <= now_y < m:
            # 인접 노드가 얼음틀 내부에 있는 경우
            if mold[now_x][now_y] == 0:
                # 음료수를 채울 수 있으면 채우기
                dfs(now_x, now_y)


for i in range(n):  # 모든 위치에 음료수 채우기
    for j in range(m):
        if mold[i][j] == 0:
            # 해당 노드에 채울 수 있다면 dfs 탐색
            dfs(i, j)
            result += 1
print(result)
