# 시간 초과
# import math, sys
# n=1
# while n!=0:
#     result=[]
#     count=0
#     n=int(sys.stdin.readline())
#     sosu=[True for _ in range(n+1)]
#     if n > 5:
#         for i in range(2, int(math.sqrt(n)+1)):
#             if sosu[i] == True:
#                 j = 2
#                 while i * j <= n:
#                     sosu[i * j] = False
#                     j+=1
#         for i in range (3, n+1):
#             if sosu[i]:
#                 result.append(i)
#         result_Re=list(reversed(result))
#         go=1
#         for i in result_Re:
#             if go == 0:
#                 break
#             for j in result:
#                 if n == i + j:
#                     print(n,'=',j,'+',i)
#                     go=0
#                     break
#             count+=1
#             if count >=len(result):
#                 print("Goldbach's conjecture is wrong.")
#                 break
#     elif 5 > n >0:
#         print("Goldbach's conjecture is wrong.")
import sys

r= 1000000
check = [True for _ in range(r)]

for i in range(2,int(r**0.6)):
    if check[i]==True:
        for j in range(i*2, r, i) : 
            if check[j] == True :
                check[j] = False            

while(True):
    n = int(sys.stdin.readline())

    if not n : 
        break
    for i in range(3,r):
        if check[i] == True:
            if check[n-i] == True :
                print(n, '=', i, '+', n-i)
                break