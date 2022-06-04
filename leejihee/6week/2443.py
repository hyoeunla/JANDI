# 2443. 별 찍기 - 6
star = int(input())

for i in range(star, 0, -1):  # 5,4,3,2,1
    print(" "*(star-i), end="")
    print("*" * (i-1), end="")
    print("*" * (i))
