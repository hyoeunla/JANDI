N = int(input())
if N == 0:
    print(1)
else:
    for i in range(1, N):
        N = N*i
    print(N)
