# [2750] 수 정렬하기
countNumber = int(input())
numberList = []
for i in range(countNumber):
    temp = int(input())
    numberList.append(temp)
numberList.sort()
for i in range(countNumber):
    print(numberList[i])
