# [이코테] 효율적인 화폐 구성
n, m = map(int, input().split())
unitMoney = []
for i in range(n):
    unitMoney.append(int(input()))
array = [10001] * (m + 1)
array[0] = 0
for i in range(n):
    for j in range(unitMoney[i], m + 1):
        if array[j - unitMoney[i]] != 10001:
            array[j] = min(array[j], array[j - unitMoney[i]] + 1)
if array[m] == 10001:
    print(-1)
else:
    print(array[m])
