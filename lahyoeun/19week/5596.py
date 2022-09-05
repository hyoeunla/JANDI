a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = sum(a)
t = sum(b)
if s >= t:
    print(s)
else:
    print(t)
