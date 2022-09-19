m = int(input())
n = int(input())
s = 0
l = []
for i in range(m, n+1):
    sqrt = i ** (1/2)
    if sqrt % 1 == 0:
        s += i
        l.append(i)
l.sort()
if len(l) == 0:
    print(-1)
else:
    print(s)
    print(l[0])
