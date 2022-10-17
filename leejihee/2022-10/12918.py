# 12918 문자열 다루기 기본
def solution(s):
    if (len(s) == 4 or len(s) == 6) and s.isdigit() == True:
        answer = True 
    else:
        answer = False
    return answer