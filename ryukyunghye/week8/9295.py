# [9295] 주사위
T = int(input())
for i in range(1, T+1):
    one, two = map(int, input().split())
    print("Case {}: {}".format(i, one+two))
