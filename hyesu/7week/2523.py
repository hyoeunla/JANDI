# 별 찍기 - 13

star = int(input())
for i in range(1, 2*star):
    if i <= star:
        print("*"*(i))
    else:
        print("*"*(2*star-i))
