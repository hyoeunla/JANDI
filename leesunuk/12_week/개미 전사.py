# 개미 전사
n = int(input())
foods = map(int, input().split())

if n % 2 == 0:
    n /= 2
else:
    n /= 2


print(int(n))
