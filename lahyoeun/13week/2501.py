n, k = map(int, input().split())
array = []
for i in range(1, n+1):
    if n % i == 0:
        array.append(i)
while len(array) < k:
    array.append(0)
print(array[k-1])
