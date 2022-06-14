# 10569. 다면체
t = int(input())
for i in range(t):
    v, e = map(int, input().split())
    area = 2-v+e
    print(area)
