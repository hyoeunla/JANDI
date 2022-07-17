n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

a = [10001] * (m+1)
a[0] = 0
for i in range(n):
    for j in range(array[i], m+1):
        if a[j - array[i]] != 10001:
            a[j] = min(a[j], a[j-array[i]]+1)

if a[m] == 10001:
    print(-1)
else:
    print(a[m])
