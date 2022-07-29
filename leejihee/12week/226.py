# 5. 효율적인 화폐 구성
n, m = map(int, input().split())
k = list([int(input()) for _ in range(n)])

d = [10001]*(m+1)

d[0] = 0
for i in k:  # 화폐 종류마다 반복
    for j in range(i, m+1):  # 화폐가 3이면 3부터 셀 수 있도록
        if d[j-i] != 10001:  # d[j-i]값이 바뀌었다면
            d[j] = min(d[j], d[j-i]+1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
