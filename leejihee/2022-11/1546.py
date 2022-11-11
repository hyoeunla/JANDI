# 1546 평균
subjectCount = int(input())
scoreArr = list(map(int, input().split()))
changeArr = []

m = sorted(scoreArr, reverse=True)[0]

for i in scoreArr:
    changeArr.append(i/m*100)

print(sum(changeArr)/subjectCount)