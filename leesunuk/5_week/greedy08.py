# 8.만들 수 없는 금액

n = int(input("동전의 개수를 입력해주세요: "))
money = list(map(int, input("동전 각각의 금액을 입력해주세요: ").split()))

money.sort()
result = 1
for i in money:
    if result < i:
        break
    else:
        result += i

print(result)
