# [12903] 가운데 글자 가져오기
# 방법1
def solution(s):
    if len(s) % 2 == 0:
        return s[(len(s)//2-1): (len(s)//2+1)]
    else:
        return s[len(s)//2]


# 방법2
def solution(s):
    if len(s) % 2 == 1:
        return s[len(s)//2]
    else:
        return s[(len(s)//2-1): (len(s)//2+1)]
