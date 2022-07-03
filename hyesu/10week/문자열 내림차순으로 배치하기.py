# 문자열 내림차순으로 배치하기

def solution(s):
    answer = ''
    a = sorted(s, reverse = True)
    answer = ''.join(a)
    return answer
