# 82612 부족한 금액 계산하기
def solution(price, money, count):
    total = sum(price * i for i in range(1, count+1))
    return 0 if total < money else total - money