n, x = map(int, input().split())
num = list(map(int, input().split()))

smallnum = []
for i in num:
    if i < x:
        smallnum.append(i)
print(*smallnum)
