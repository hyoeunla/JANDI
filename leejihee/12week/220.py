# 3. 개미 전사
n = int(input())
k = list(map(int, input().split()))

d = [0]*100  # 식량창고 개수

d[0] = k[0]
d[1] = max(k[0], k[1])
# (i-1)번째 창고를 털면 i를 털 수 없음 = d(i-1)
# (i-2)번째 창고를 털면 i를 털 수 있음 = d(i-2)+k[i]
# 둘 중 더 큰 곳을 찾으면 됨
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2]+k[i])
    # print(f'd[{i}] = max({d[i-1]}, {d[i-2]+k[i]})')
print(d[n-1])
