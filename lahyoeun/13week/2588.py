a = int(input())
b = int(input())
c = b
num = [0]*3
mul = 0
for i in range(3):
    num[i] = c % 10
    c //= 10
for i in num:
    mul = a * i
    print(mul)
    mul = 0
print(a*b)
