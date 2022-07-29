#소수 구하기

import sys
M,N=map(int, sys.stdin.readline().split())

alpha=[False, False] + [True] *(N-1)
prime_number=[]

for i in range(2, N+1):
    if alpha[i]==True:
        prime_number.append(i)
        for j in range(2*i, N+1, i):
            alpha[j]=False

for i in prime_number:
    if M <= i <= N:
        print(i)
