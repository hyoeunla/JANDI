charge = 1260
n = 0
n = charge // 500
s = ((charge)-500*n) // 100
k = (((charge)-500*n) - 100*s) // 50
l = ((((charge)-500*n) - 100*s) - 50*k) // 10
print(n+s+k+l)  # 나의 풀이

n = 1260
count = 0

coin_types = [500, 100, 50, 10]  # 큰 단위의 화폐부터

for coin in coin_types:
    count += n // coin  # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 새기
    n %= coin

print(count)


charge = 1260
n = 0
n = charge // 500
s = ((charge)-500*n) // 100
charge = ((charge)-500*n)
k = (charge - 100*s) // 50
charge = (charge - 100*s)
l = (charge - 50*k) // 10
print(n+s+k+l)
# 수정한 답
