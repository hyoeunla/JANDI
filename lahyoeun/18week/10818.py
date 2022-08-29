c = int(input())
num = list(map(int, input().split()))
m = num[0]
n = num[0]
for i in num[1:]:
    if i > m:
        m = i
    elif i < n:
        n = i
print(n, m)
