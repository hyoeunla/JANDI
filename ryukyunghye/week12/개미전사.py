# [이코테] 개미전사
storage = int(input())
foodNumber = list(map(int, input().split()))
table = [0] * 100
table[0] = foodNumber[0]
table[1] = max(foodNumber[0], foodNumber[1])
for i in range(2, storage):
    table[i] = max(table[i-1], table[i-2]+foodNumber[i])
print(table[storage-1])
