up, down, branch = map(int, input().split())
# snail = 0
# day = 0

# while snail < branch:
#     snail += up
#     day += 1
#     if snail < branch:
#         snail -= down
# print(day)

day = (branch - down) // (up - down) 
if (branch - down) % (up - down): 
    # up보다 작은 나머지가 있으면...
    # 하루 더 올라가야 한다
    day += 1
print(day)