a = []
for i in range(9):
    a.append(int(input()))

for i in range(len(a)-1):  # 빨
    for j in range(i+1, len(a)):  # 파
        if sum(a)-(a[i]+a[j]) == 100:
            a[i] = 101
            a[j] = 101
a.sort()
for i in range(7):
    print(a[i])
