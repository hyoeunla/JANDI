# 별찍기-12
n = int(input())
i, h = 0, 0
j = n
while h < (n*2)-1:
    if h < n:
        i += 1
        j -= 1
    else:
        i -= 1
        j += 1
    print((" "*j)+("*"*i))
    h += 1
