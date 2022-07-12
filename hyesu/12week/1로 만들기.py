# 1로 만들기

x = int(input())

t = [0] * 30001

for i in range(2, x + 1):
    t[i] = t[i-1] + 1
    if i % 2 == 0:
        t[i] = min(t[i], t[i // 2] + 1)
    if i % 3 == 0:
        t[i] = min(t[i], t[i // 3] + 1)
    if i % 5 == 0:
        t[i] = min(t[i], t[i // 5] + 1)

print(t[x])
