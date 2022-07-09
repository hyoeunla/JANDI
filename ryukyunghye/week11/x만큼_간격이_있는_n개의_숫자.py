# [12954] x만큼 간격이 있는 n개의 숫자
# 방법1
def solution(x, n):
    arr = []
    for i in range(1, n+1):
        arr.append(x*i)
    return arr


# 방법2
def solution(x, n):
    return [x*i for i in range(1, n+1)]


# 테스트8 - 런타임 에러 발생
def solution(x, n):
    arr = []
    if x < 0:
        for i in range(x, x*n-1, x):
            arr.append(i)
    else:
        for i in range(x, x*n+1, x):
            arr.append(i)
    return arr
