# 최대공약수와 최소공배수

a, b = map(int, input().split())
a1, b1 = a, b
n = 0
m = 0


for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        n = i

while 1:
    if a == b:
        m = a
        break

    elif a > b:
        b += b1
    elif b > a:
        a += a1
print(n)
print(m)
