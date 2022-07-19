# 베르트랑 공준

# while 1:
#     n = int(input())
#     if (n != 0 and n > 1):
#         result_sub = 0
#         result = []
#         for i in range(n+1, n*2+1):
#             for j in range(2, n):
#                 if i % j == 0:
#                     result_sub = 0
#                     break
#                 else:
#                     result_sub = i
#             if result_sub != 0:
#                 result.append(result_sub)
#         print(len(result))
#     elif n == 1:
#         print(n)
#     else:
#         break
# 시간 초과 문제로 다시 고민해보는 중

import sys

while 1:
    n=int(sys.stdin.readline())

    if not n:
        break
    limit = n*2
    alpha=[False, False] + [True] * (limit - 1)
    prime_number=[]

    for i in range(2, limit+1):
        if alpha[i]:
            prime_number.append(i)
            for j in range(2*i, limit+1, i):
                alpha[j]=False

    print(len([x for x in prime_number if n < x <=limit]))
