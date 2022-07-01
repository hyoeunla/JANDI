# [12917] 문자열 내림차순으로 배치하기
# 방법1
def solution(s):
    return (''.join(sorted(s)[::-1]))


# 방법2
def solution(s):
    return ''.join(sorted(s, reverse=True))


# 방법3
def solution(s):
    return (''.join(reversed(sorted(s))))
