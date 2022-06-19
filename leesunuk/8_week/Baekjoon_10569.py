# 다면체
n = int(input())

for _ in range(n):
    V, E = map(int, input().split())
    print(E-V+2)
