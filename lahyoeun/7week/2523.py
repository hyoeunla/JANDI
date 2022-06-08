'''
N = int(input())
for i in range(N+1):
    print("*"*i)
for j in range(N):
    print("*"*(N-j-1)) 출력형식 오류로 고쳤음
'''
n = int(input())
for i in range(1, n + 1):
    print("*" * i)
for i in range(n - 1, 0, -1):
    print("*" * i)
