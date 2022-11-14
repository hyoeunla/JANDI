# 2775번: 부녀회장이 될테야

s = int(input())
result = 0

for i in range(s):
    k = int(input())
    k += 1
    n = int(input())
    apa = [0 for _ in range(k)]
    for j in range(k):
        apa[j] = [0 for _ in range(n)]
    for j in range(0, n):
        apa[0][j] = j+1

    if k == 0:
        print(n)

    else:
        for i in range(1, k):
            for j in range(n+1):
                for l in range(j):
                    result += apa[i-1][l]
                apa[i][j-1] = result
                result = 0
        print(apa[k-1][n-1])
