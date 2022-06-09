# 9325. 얼마?
n = int(input("테스트 케이스의 개수: "))

for i in range(n):
    price = 0
    s = int(input("자동차 가격: "))
    price += s
    m = int(input("옵션의 개수: "))
    for i in range(m):
        q, p = map(int, input("옵션 개수, 가격:").split())
        price += q*p
    print(price)
