# 문제9. 볼링공 고르기

n, m = map(int, input().split())
data = list(map(int, input().split()))

array = [0] * 10  # 1부터 10까지 무게를 담을 수 있는 리스트
for i in data:
    array[i] += 1  # 각 무게 해당하는 볼링공의 개수

result = 0
for i in range(1, m + 1):  # 1부터 m까지의 각 무게에 대하여 처리
    n -= array[i]  # 무게 i인 볼링공의 개수 제외
    result += array[i] * n  # B가 선택하는 경우의 수와 곱하기

print(result)
