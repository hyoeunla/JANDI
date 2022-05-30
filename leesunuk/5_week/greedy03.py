# 3. 숫자 카드 게임

n, m = map(int, input("행의 개수와 열의 개수를 입력해주세요: ").split())
num = [[]for _ in range(n)]
for i in range(n):
    card_list = list(map(int, input("%d행에 들어갈 카드들을 입력해주세요: " % (i+1)).split()))
    card = card_list
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
