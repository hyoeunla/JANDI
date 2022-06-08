# 별찍기-13
n = int(input())
j = 0
for i in range((n*2)-1):
    if i < n:
        j += 1
    else:
        j -= 1
    print("*"*j)
