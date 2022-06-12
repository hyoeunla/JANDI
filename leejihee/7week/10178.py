# 10178. 할로윈의 사탕
n = int(input())
for i in range(n):
    c, v = map(int, input().split())
    son = c // v
    dad = c % v
    print("You get {} piece(s) and your dad gets {} piece(s).".format(son, dad))
