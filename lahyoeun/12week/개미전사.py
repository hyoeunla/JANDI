x = int(input())
a = list(map(int, input().split()))
b = list([0]*x)
b[0] = a[0]
b[1] = max(a[0], a[1])
for i in range(2, x):
    b[i] = max(b[i-1], b[i-2]+a[i])

print(b[x-1])
