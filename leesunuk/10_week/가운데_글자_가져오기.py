# 가운데 글자 가져오기

def solution(s):
    a = list(s)
    if len(s) % 2 == 0:
        return "".join(a[len(s)//2-1:len(s)//2+1])
    elif len(s) % 2 != 0:
        return a[int(len(s)//2)]
