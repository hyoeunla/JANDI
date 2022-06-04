# 첼시를 도와줘!

n = int(input())

for i in range(n):
    p = int(input())
    dic = {}
    for i in range(p):
        cost, Player = input().split()
        Cost = int(cost)
        dic[Cost] = Player

    print(dic.get(max(dic.keys())))
