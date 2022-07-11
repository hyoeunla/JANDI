# 1로 만들기
n = int(input())
numbers = [5, 3, 2]
count = 0
while n > 1:
    for i in numbers:
        if n % i == 0:
            n /= i
            break
        elif (n-1) % i == 0:
            n -= 1
            count += 1
            n /= i
            break
    count += 1
print(count)
