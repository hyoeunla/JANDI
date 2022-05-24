# 01. 거스름돈
coin = int(input())  # 문제에선 1260원이라고 주어짐
money = [500, 100, 50, 10]
count = 0            # 거슬러줄 동전의 수
for c in money:
    count += coin//c
    coin %= c
    print(str(c)+"원", count)
print(count)
