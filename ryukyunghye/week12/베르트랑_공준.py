# [4948] 베르트랑 공준
primeNumber = []
for i in range(2, 123456*2+1):
    count = 0
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            count += 1
            break
    if count == 0:
        primeNumber.append(i)
while True:
    n = int(input())
    result = 0
    if n == 0:
        break
    for i in primeNumber:
        if n < i <= 2*n:
            result += 1
    print(result)
