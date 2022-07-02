# 가운데 글자 가져오기

def solution(s):
    x = len(s)
    y = x
    if (x % 2 == 1):
        answer = s[y]
    else:
        answer = s[y-1: y+1]
    return answer
