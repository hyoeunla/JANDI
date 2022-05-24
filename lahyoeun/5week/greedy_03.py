n, m = map(int, input().split())
a = 0

for i in range(n):
    j = list(map(int, input().split()))
    min_v = min(j)
    a = max(a, min_v)
print(a)
