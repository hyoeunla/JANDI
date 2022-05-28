# 09. 볼링공 고르기
# 내 방법
N, M = map(int, input().split())
k = list(map(int, input().split()))
count = 0
for n in range(1, N):
    for m in range(1, N):
        if k[n] != k[m]:
            count += 1
print(count)


# 답안
n, m = map(int, input().split())
data = list(map(int, input().split()))
array = [0] * 11
for x in data:
    array[x] += 1
result = 0
for i in range(1, m+1):
    n -= array[i]
    result += array[i]*n
print(result)
