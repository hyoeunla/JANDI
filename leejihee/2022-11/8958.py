# 8958 OX퀴즈
n = int(input())
list = [input() for i in range(n)]

for i in list:
    score = 0
    i = i.split('X')
    for j in i:
        for k in range(1,len(j)+1):
            score += k
    print(score)
