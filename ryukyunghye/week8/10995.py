# [10995] 별 찍기 - 20
N = int(input())
for i in range(N):
    if i % 2 == 0:
        print("* "*N)
    else:
        print(" *"*N)
