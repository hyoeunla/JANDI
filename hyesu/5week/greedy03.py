# 문제3. 숫자 카드 게임

n, m = map(int, input.split())  # n, m을 공백으로 구분하여 입력받기

result = 0

for i in range(n):
    data = list(map(int, input.split()))  # 현재 줄에서 '가장 작은 수' 찾기
    min_value = min(data)  # '가장 작은 수' 중애서 가장 큰 수 찾기
    result = max(result, min_value)

print(result)
