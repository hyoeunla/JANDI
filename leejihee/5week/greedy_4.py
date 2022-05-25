# 문제4. 1이 될 때까지

# 나의 풀이
n, k = map(int, input().split())
count = 0
while n > 1:
    if n % k != 0:  # 17%4==1
        n -= 1  # 16
        count += 1
    else:
        n = n//k
        count += 1
print(count)

# 해설
n, k = map(int, input().split())
count = 0
while n >= k:  # n을 k로 나눌 수 있을 때까지만 반복
    while n % k != 0:
        n -= 1
        count += 1
    n //= k
    count += 1
while n > 1:  # 다 나눴는데 n이 1보다 크다면 1씩 빼줌
    n -= 1
    count += 1
print(count)
