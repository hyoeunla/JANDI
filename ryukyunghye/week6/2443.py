# [2443] 별 찍기 - 6
N = int(input())
for i in range(N, 0, -1):
    print(' '*(N-1)+"*"*(2*i-1))
