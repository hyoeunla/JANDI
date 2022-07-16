# 내 풀이 시간초과
import math
n = int(input())
while n != 0:
    count = 0
    for i in range(n+1, 2*n+1):
        for j in range(2, i):
            if i % j == 0:
                count += 1
                break
    count = n - count
    print(count)
    n = int(input())

# 다시 고안한 풀이


def isPrime(n):
    if n == 1:
        return False
    else:
        for i in range(2, int(math.sqrt(n)) + 1):  # 소수 감별
            if n % i == 0:  # 나누어지면
                return False
        return True  # 아니면 True, 소수임


all_number = list(range(1, 246913))  # 모든 숫자
prime_number = []  # 소수 담아둘 리스트
for i in all_number:
    if isPrime(i):  # i 가 소수면
        prime_number.append(i)  # 넣어줌

n = int(input())
while(n != 0):
    count = 0
    for i in prime_number:
        if n < i and i <= 2*n:
            count += 1
    print(count)
    n = int(input())
