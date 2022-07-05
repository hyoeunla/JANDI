# 소수
startNum = int(input())
endNum = int(input())
primes = []
for i in range(startNum, endNum+1):
    var = 0
    if i > 1:
        for j in range(2, i):
            if i % j == 0:
                var += 1
                break
        if var == 0:
            primes.append(i)
if len(primes) > 0:
    print(sum(primes))
    print(min(primes))
else:
    print(-1)
