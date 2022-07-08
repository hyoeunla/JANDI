# 2×n 타일링 2

n = int(input())
dp = [0 for i in range(n+2)]
dp[1] = 1
dp[2] = 3
k = 1

for i in range(3, n+2):
    k *= -1
    dp[i] = (dp[i-1]*2+k) % 10007

print(dp[n] % 10007)
