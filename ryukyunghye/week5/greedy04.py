# 04. 1이 될 때까지

# 방법1 -> 나의 풀이
n, k = map(int, input().split())
count = 0
while n >= k:
    if n % k == 0:
        n = n/k
        count += 1
    else:
        n -= 1
        count += 1
print(count)

# 방법2 -> 책의 풀이1
n, k = map(int, input().split())
result = 0
while n >= k:
    while n % k == 0:
        n -= 1
        result += 1
    n //= k
    result += 1
while n > 1:
    n -= 1
    result += 1
print(result)

# 방법3 -> 책의 풀이2
n, k = map(int, input().split())
result = 0
while True:
    target = (n//k) * k
    result += (n - target)
    if n < k:
        break
    result += 1
    n//k
result += (n-1)
print(result)
