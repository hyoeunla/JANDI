# [12922] 수박수박수박수박수박수?
# 방법1
def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += '수'
        else:
            answer += '박'
    return answer


# 방법2
def solution(n):
    return ('수박'*n)[:n]
