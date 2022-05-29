# 문제9. 볼링공 고르기

n, m = map(int, input().split())
w = list(map(int, input().split()))
result = 0

array = [0]*11  # 같은 무게의 공을 저장하는 공간
for x in w:
    array[x] += 1

for i in range(m):
    n -= array[i]  # 공의 개수에서 계산한 공 개수 제외
    result += array[i]*n  # 무게별 공 개수 * 남은 공 개수
print(result)
