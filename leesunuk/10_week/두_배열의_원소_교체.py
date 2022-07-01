# 두 배열의 원소 교체

N, K = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(K):
    a[i] = b[i]
print(sum(a))
