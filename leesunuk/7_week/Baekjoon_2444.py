# 별찍기-7
n = int(input())
a = (n*2)+1
j = n-1

for i in range(1, a-2, 2):
    print((" "*j)+("*"*i))
    j -= 1
for i in range(a-2, 0, -2):
    print((" "*j)+("*"*i))
    j += 1
