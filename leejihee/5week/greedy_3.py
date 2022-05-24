# 문제3. 숫자 카드 게임

# 나의 풀이
n, m = map(int, input().split())
k_min = []
for i in range(n):
    kard = map(int, input().split())
    k_min.append(min(kard))
print(max(k_min))

n, m = map(int, input().split())
k_min = [0 for i in range(n)]
for i in range(n):
    kard = map(int, input().split())
    k_min[i] = min(kard)
print(max(k_min))

# 해설
n, m = map(int, input().split())
result = 0
for i in range(n):
    kard = list(map(int, input().split()))
    k_min = min(kard)
    result = max(result, k_min)
    # 둘 중 누가 더 큰지 비교
    # 반복문이므로 처음에는 0, 최솟값 비교해서 result에 넣고
    # 다음에는 result, 최솟값을 비교해서 넣고 ...
    # 가장 큰 값이 result에 들어갈 것임
print(result)
