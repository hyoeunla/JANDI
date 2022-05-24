# 1.문제 거스름돈

N = int(input("받아야 하는 거스름돈을 입력해주세요: "))

a = N//500
N = N-(a*500)
b = N//100
N = N-(b*100)
c = N//50
N = N-(c*50)
d = N//10

print("500원짜리", a, "개\n", '100원짜리', b, "개\n", '50원짜리', c, "개\n",
      '10원짜리', d, "개\n")

# 2.문제
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
