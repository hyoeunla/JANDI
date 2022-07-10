# x만큼 간격이 있는 n개의 숫자

def solution(x, n):
    answer = [0 for _ in range(n)]
    subx = 0
    for i in range(n):
        subx += x
        answer[i] = subx
    return answer
