# 위에서 아래로
N = int(input())
S = []
for i in range(N):
    S.append(int(input()))

S = sorted(S, reverse=True)
for i in S:
    print(i, end=' ')
