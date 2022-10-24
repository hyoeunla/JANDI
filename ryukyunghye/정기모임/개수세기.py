# [10807] 개수 세기
# 방법1
countNumber = int(input())
numberList = list(map(int, input().split()))
findNumber = int(input())
count = 0
for i in range(len(numberList)):
    if numberList[i] == findNumber:
        count += 1 
print(count)

# 방법2
countNumber = int(input())
numberList = list(map(int, input().split()))
findNumber = int(input())
print(numberList.count(findNumber))
