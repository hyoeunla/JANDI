# 2. 큰 수의 법칙
n, m, k = map(int, input("배열의 크기, 더해지는 횟수, 연속해서 몇번까지 더할 건지 입력해주세요: ").split())
num = list(map(int, input("수들을 입력해주세요: ").split()))

num.sort()
print(num)
big = num[n-1]
big2 = num[n-2]
hap = 0
i = 0
while i < m:
    for _ in range(k):
        if i == m:
            break
        hap += big
        i += 1

    if i == m:
        break
    hap += big2
    i += 1

print(hap)
