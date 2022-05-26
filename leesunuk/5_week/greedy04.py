# 4. 1이 될 때까지
n, k = map(int, input("숫자, 나눠줄 숫자를 입력해주세요: ").split())
bun = 0


while 1:
    if n == 1:
        break
    bun += 1
    if n % k != 0:
        n -= 1
    else:
        n = n/k
print(bun)
