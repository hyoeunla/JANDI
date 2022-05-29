# 9.볼링공 고르기
n, m = map(int, input("볼링공의 개수와 최대 무게를 입력해주세요: ").split())
k = list(map(int, input("볼링공 각각의 무게를 입력해주세요: ").split()))
start = 0
count = 0
for i in k:
    if start == n:
        break

    for j in range(start, n):
        if i != k[j]:
            count += 1
    start += 1

print(count)
