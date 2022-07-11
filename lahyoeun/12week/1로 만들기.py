count = 0
x = int(input())
a = list([0]*(x+1))
for i in range(2, x+1):
    a[i] = a[i-1] + 1
    if i % 2 == 0:
        a[i] = min(a[i], a[i//2] + 1)
    if i % 3 == 0:
        a[i] = min(a[i], a[i//3] + 1)
    if i % 5 == 0:
        a[i] = min(a[i], a[i//5] + 1)
print(a[x])
