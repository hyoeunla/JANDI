# 음료수 얼려먹기
N, M = map(int, input().split())
ice = []

for i in range(N):
    ice.append(list(map(int, input())))


def dfs(x, y):
    if x <= -1 or x >= N or y <= -1 or y >= M:
        return False

    if ice[x][y] == 0:
        ice[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False


result = 0
for i in range(N):
    for j in range(M):
        if dfs(i, j) == True:
            result += 1
print(result)
