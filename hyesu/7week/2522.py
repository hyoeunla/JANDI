# 별 찍기 - 12

star = int(input())
for i in range(1, 2*star):
    if i <= star:
        print(" "*(star - i)+"*"*(i))
    else:
        print(" "*(i-star)+"*"*(2*star-i))
