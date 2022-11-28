# 수 정렬하기

n = int(input())
nums = []

for i in range(n):
    num = int(input())
    nums.append(num)

order = sorted(nums)

for j in range(n):
    print(order[j])
