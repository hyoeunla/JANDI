# 02. 큰 수의 법칙
# 방법1 -> 내생각1 sort() 사용
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()
result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += numbers[n-1]
        m -= 1
    if m == 0:
        break
    result += numbers[n-2]
    m -= 1
print(result)

# 방법2 -> 내생각2 sort(reverse=True) 사용
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort(reverse=True)
result = 0
while True:
    for i in range(k):
        if m == 0:
            break
        result += numbers[0]
        m -= 1
    if m == 0:
        break
    result += numbers[1]
    m -= 1
print(result)

# 방법2 -> 책
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]
count = int(m/(k+1))*k
count += m % (k+1)
result = 0
result += (count) * first
result += (m-count) * second
print(result)
