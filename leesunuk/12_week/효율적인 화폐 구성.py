# 효율적인 화폐 구성

n, m = map(int, input().split())
won = []
result = 0
count = 0
for i in range(n):
    won.append(int(input()))
won.sort(reverse=True)
while 1:
    if count == len(won):
        result = -1
        break

    if m > 0:
        for i in won:
            if m-i >= 0:
                m -= i
                result += 1
                count = 0
                break
            else:
                count += 1
    else:
        break
print(result)
