# 개미 전사
n = int(input())
foods = list(map(int, input().split()))
result1 = 0
result2 = 0
a = 0


def delmax(x):
    a = x.index(max(x))
    print(x)
    if len(x) > 1:
        if max(x) == x[-1]:
            x.remove(x[-1])
            x.remove(x[a-1])
        elif max(x) == x[0]:
            x.remove(x[a])
            x.remove(x[a])
        else:
            x.remove(x[a])
            x.remove(x[a])
            x.remove(x[a-1])


nn = n / 2
nn = int(nn)
for i in range(nn):
    result1 += max(foods)
    delmax(foods)

if n % 2 != 0:
    n /= 2
    n = int(n)+1
    for i in range(n):
        result2 += max(foods)
        delmax(foods)

print(max(result1, result2))
