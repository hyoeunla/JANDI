# 별 찍기-6
N = int(input())
N = (2*(N-1))+1
j = 0
for i in range(N, 0, -2):
    print((" "*j)+("*"*i))
    j += 1
