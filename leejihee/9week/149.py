# 3. 음료수 얼려먹기
n, m = map(int, input().split())
iceBox = []
for i in range(n):
    iceBox.append(list(map(int, input())))


def dfs(x, y):  # 깊이 우선 탐색
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    if iceBox[x][y] == 0:
        iceBox[x][y] = 1
        # 상하좌우 위치 재귀호출로 확인하기
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


result = 0
for i in range(n):  # 행
    for j in range(m):  # 열
        if dfs(i, j) == True:
            result += 1
print(result)
