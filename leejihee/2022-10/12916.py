# 나의 풀이
def solution(s):    
    pWord, yWord = 0, 0
    for i in s:
        if i=='P' or i=='p':
            pWord+=1
        elif i=='Y' or i=='y':
            yWord+=1
    return True if pWord == yWord else False

# 다른 사람의 풀이
def solution(s):    
    return s.lower().count('p') == s.lower().count('y')