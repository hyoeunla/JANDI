# X보다 작은 수

N, X = map(int, input().split())
ls = list(map(int, input().split()))
result = []
for i in ls:
    if i < X:
        result.append(i)
print(*result)
