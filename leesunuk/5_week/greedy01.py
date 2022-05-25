# 1. 거스름돈

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

# 다른 방법
money = [500, 100, 50, 10]
N = int(input("받아야 하는 거스름돈을 입력해주세요: "))

for i in range(4):
    a = N//money[i]
    N = N-(a*money[i])
    print(money[i], "원", a, "개")

# 차이점
'''
list와 반복문을 사용했냐 안 했냐의 차이다. 더 간략해지는 아래 방법이 더 효율적이다.
'''

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

# 3. 숫자 카드 게임

n, m = map(int, input("행의 개수와 열의 개수를 입력해주세요: ").split())
num = [[]for _ in range(n)]
for i in range(n):
    x, y, z = map(int, input("%d행에 들어갈 카드들을 입력해주세요: " % (i+1)).split())
    card = [x, y, z]
    for _ in range(3):
        num[i] = card
        num[i].sort()

for j in range(n):
    if j+1 == n:
        break

    if num[j][0] >= num[j+1][0]:
        win = num[j][0]
    else:
        win = num[j+1][0]

print(win)

# 다른 방법

n, m = map(int, input("행의 개수와 열의 개수를 입력해주세요: ").split())

result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)
print(result)


# 차이점
'''
일단 내 코드는 너~~~~~무 복잡하고, 길다. 그게 가장 큰 차이점이다. 다른 방법을 보고 많이 나의 방식에 대한 회의감이 몰려왔다.
굳이 문제에서 원하는 대로 풀이를 쓸 필요가 없다는 걸 깨달았다. 어차피 내가 문제 순서대로 해도 방식만 같아 값이 출력 된다면, 굳이 말로
풀어져있는 설명들 대로 코드를 안 짜도 되는 것이다. 나는 한 행씩 받아 값들을 저장하고, 그 행들을 하나씩 비교해 닶을 추출해낸 반면,
다른 방법에선 한 행을 받을때마다 작은 값을 저장하여 다른 행이 들어오면 그 행의 작은 값과 계산하여 큰 값을 넣어 출력하는 간단한 프로그램이었다.
'''
