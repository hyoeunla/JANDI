# 백준 2581번 소수
M = int(input())
N = int(input())
result = []
for i in range(M, N+1):
    no = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                no = 1
                break
        if no == 0:
            result.append(i)
if len(result) > 0:
    print(sum(result))
    print(result[0])
else:
    print(-1)
