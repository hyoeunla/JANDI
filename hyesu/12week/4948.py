# 베르트랑 공준

n = 123456 * 2 + 1

prime = [True] * n

for k in range(2, int(n**0.5)+1):
    if prime[k]:
        for i in range(k*k, n, k):
            prime[i] = False

while True:
    w = int(input())
    if w == 0:
        break
    else:
        count = 0
        for j in range(w+1, w*2+1):
            if prime[j]:
                count += 1
        print(count)
