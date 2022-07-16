# 일곱 난쟁이

import sys

height = []
selected = [False] * 9
for _ in range(9):
    height.append(int(input()))


def dfs(h):
    if len(h) == 7:
        if sum(h) == 100:
            h.sort()
            for i in h:
                print(i)
            sys.exit(0)
        else:
            return

    for i in range(len(height)):
        if not selected[i]:
            selected[i] = 1
            h.append(height[i])
            dfs(h)
            selected[i] = 0
            h.pop()


dfs([])
