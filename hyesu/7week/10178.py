# 할로윈의 사탕

a = int(input())

for _ in range(a):
    n, m = map(int, input().split())
    print(f'You get {n//m} piece(s) and your dad gets {n%m} piece(s).')
