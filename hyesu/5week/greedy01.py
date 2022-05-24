# 문제1. 거스름

money = int(input())
count = 0

coin = [500, 100, 50, 10]

for c in coin:
    count += money // coin # 거슬러 줄 수 있는 동전의 개수 
    money %= coin

print(count)
