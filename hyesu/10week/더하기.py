# 더하기

n = int(input())
for _ in range(n):
    cnt = int(input())
    print(sum(list(map(int, input().strip().split()))))
