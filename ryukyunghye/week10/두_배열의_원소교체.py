# 두 배열의 원소 교체
n, k = map(int, input().split())
aList = list(map(int, input().split()))
bList = list(map(int, input().split()))
aList = sorted(aList)
bList = sorted(bList)[::-1]
# aList.sort()
# bList.sort(reversed = True)
for i in range(k):
    if aList[i] < bList[i]:
        aList[i], bList[i] = bList[i], aList[i]
    else:
        break
print(sum(aList))
