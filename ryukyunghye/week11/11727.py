# 2xn 타일링2
# 방법1
n = int(input())
dp = [0, 1, 3]
for i in range(3, n+1):
    dp.append((dp[i-1])+((dp[i-2]*2)))
print(dp[n] % 10007)

# 방법2
n = int(input())
arr = [0 for _ in range(n+1)]
if n == 1:
    print(n)
else:
    arr[1] = 1
    arr[2] = 3
    for i in range(3, n+1):
        arr[i] = arr[i-1]+arr[i-2]*2
    print(arr[n] % 10007)
