n = int(input())
a = 5
b = 7
s = 12
for i in range(n-2):
    c = b+3
    b = c
    s += c
if n == 1:
    print(a)
elif n == 2:
    print(a+b)
else:
    print(s % 45678)
