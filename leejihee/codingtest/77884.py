# 77884 약수의 개수와 덧셈
def solution(left, right):
    total = 0
    arr = list(range(left, right+1))

    for i in arr:
        count=0
        for j in range(1,i+1):
            if i%j==0:
                count+=1
        total += i if count%2==0 else -i
    return total