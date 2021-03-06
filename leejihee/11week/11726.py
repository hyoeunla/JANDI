# 11726. 2×n 타일링
n = int(input())

dp = [0] * 1001  # n은 1~1000까지의 수
dp[1] = 1  # n=1일 때, 1가지
dp[2] = 2  # n=2일 때, 2가지

for i in range(3, 1001):
    dp[i] = dp[i-1] + dp[i-2]
    # n=3부터는 (n-1)+(n-2)로 일반화할 수 있음

print(dp[n] % 10007)
