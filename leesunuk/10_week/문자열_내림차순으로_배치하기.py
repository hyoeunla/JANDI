# 문자열 내림차순으로 배치하기

def solution(s):
    a = list(s)
    a.sort(reverse=True)
    s = "".join(a)
    return s
