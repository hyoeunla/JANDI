# 별찍기-16
n = int(input())
j = n-1
for i in range(1, n+1):
    print((" "*j)+("* "*i))
    j -= 1
