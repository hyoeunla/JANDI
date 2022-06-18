# 다면체

n = int(input())
for i in range(n):
    v, e = map(int, input().split())
    print(e - v + 2)
