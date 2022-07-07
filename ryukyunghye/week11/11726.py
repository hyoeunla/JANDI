# 2xn 타일링
# 방법1
n = int(input())
arr = [0 for _ in range(n+1)]
if n < 3:
    print(n)
else:
    arr[1] = 1
    arr[2] = 2
    for i in range(3, n+1):
        arr[i] = arr[i-1] + arr[i-2]
    print(arr[i] % 10007)

# 방법2
n = int(input())
arr = [0, 1, 2]
for i in range(3, n+1):
    arr.append(arr[i-1]+arr[i-2])
print(arr[n] % 10007)
