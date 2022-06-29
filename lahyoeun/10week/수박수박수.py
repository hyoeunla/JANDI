def solution(n):
    answer = ''
    for i in range(n):
        if i % 2 == 0:
            answer += '수'  # 짝수일 경우 수
        else:
            answer += '박'  # 홀수일 경우 박
    return answer
