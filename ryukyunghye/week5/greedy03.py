# 03. 숫자 카드 게임

# 방법1 -> 나의 풀이
n, m = map(int, input().split())
result = 0
for i in range(n):
    nlist = list(map(int, input().split()))  # nXm 입력받기
    num_m = min(nlist)                       # 가장 작은 수 뽑기
    result = max(result, num_m)              # 각 줄에서 가장 큰 수를 뽑음
print(result)

# 방법2 -> 책의 풀이, 2중 반복문
n, m = map(int, input().split())
result = 0
for i in range(n):
    data = list(map(int, input().split()))
    min_value = 10001
    for a in data:
        min_value = min(min_value, a)
    result = max(result, min_value)
print(result)
