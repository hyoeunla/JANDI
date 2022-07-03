# 4. 두 배열의 원소 교체
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a = sorted(a)  # a.sort()
b = sorted(b, reverse=True)  # b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        # a[i] = b[i] A만 바뀜
        a[i], b[i] = b[i], a[i]  # 둘다 바뀜
    else:  # A의 원소가 B원소 보다 크면 바꿀 필요가 없으므로
        break

print(sum(a))
