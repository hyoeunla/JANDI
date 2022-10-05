# 12941. 최솟값 만들기
def solution(A,B):
    sum = 0
    A.sort()
    B.sort(reverse=True) 
    for i,j in zip(A, B):
        sum += i*j
    return sum