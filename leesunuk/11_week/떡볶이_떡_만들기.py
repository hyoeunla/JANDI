# 떡볶이 떡 만들기
N, M = map(int, input().split())
CM = list(map(int, input().split()))
result = 0
i = 0
while i < N:
    if result == M:
        break
    else:
        if i >= N:
            i = 0
        else:
            CM[-1] -= 1
            result += 1
            CM.sort()
print(CM[-1])
