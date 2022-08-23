c = int(input())
s = 0
m = 1000001
num = map(int, input().split())
for i in num:
    if s <= i:
        s = i
    else:
        s = s
    if m >= i:
        m = i
    else:
        m = m
print(m, s)
