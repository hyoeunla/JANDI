# 08. 만들 수 없는 금액
n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
coin = 1
for i in numbers:
    if coin < i:
        break
    coin += i
print(coin)
