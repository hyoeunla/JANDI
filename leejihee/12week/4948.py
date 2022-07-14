# 4948. 베르트랑 공준
# 시간초과가 나므로 소수를 구해 리스트에 넣어놓음

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True


prime_list = []

for i in range(2, 246912):  # 마지막 소수
    if isPrime(i) is True:
        prime_list.append(i)  # 함수를 통해 소수만 리스트에 추가

while True:
    n = int(input())
    count = 0

    if n == 0:
        break

    for i in prime_list:
        if n < i < 2*n+1:
            count += 1

    print(count)

# 시간초과
# while True:
#     n = int(input())
#     count = 0

#     if n == 0:
#         break
#     else:
#         for i in range(n+1, 2*n+1):
#             result = True
#             if (i < 2):
#                 result = False
#             for j in range(2, i):
#                 if i % j == 0:
#                     result = False
#             if result == True:
#                 count += 1
#     print(count)
