# 2522. 별 찍기 - 12
n = int(input())
for i in range(n):  # 0 1 2
    print(" "*(n-i-1), end="")
    print("*"*(i+1))
for i in range(1, n):
    print(" "*(i), end="")
    print("*"*(n-i))
