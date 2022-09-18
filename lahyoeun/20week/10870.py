a = 0
b = 1
s = 0
n = int(input())
if n == 0:
    print(a)
elif n == 1:
    print(b)
else:
    for i in range(n-1):
        s = a+b
        a = b
        b = s
    print(s)
