# 떡볶이 떡 만들기
n, m = map(int, input().split())
height = list(map(int, input().split()))
startPoint = 0
endPoint = max(height)
result = 0
while startPoint <= endPoint:
    total = 0
    middle = (startPoint+endPoint)//2
    for h in height:
        if h > middle:
            total += h - middle
    if total < m:
        endPoint = middle-1
    else:
        result = middle
        startPoint = middle+1
print(result)
