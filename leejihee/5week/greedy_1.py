# 문제1. 거스름돈

# 나의 풀이
money = int(input())  # 거스름돈 1260
count = 0
if money//500 > 0:
    count += (money//500)
    money -= 500*(money//500)
    # money를 나누고, 남은 나머지를 money에 다시 넣어준다.
    # money %= 500를 하면 260이 남음
if money//100 > 0:
    count += (money//100)
    money -= 100*(money//100)
if money//50 > 0:
    count += (money//50)
    money -= 50*(money//50)
if money//10 > 0:
    count += (money//10)
    money -= 10*(money//10)
print(count)

# 해설
money = 1260
coin = [500, 100, 50, 10]
count = 0
for i in coin:
    count += money//i
    money %= i
print(count)
