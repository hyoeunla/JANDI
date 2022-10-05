# 70129. 이진 변환 반복하기
def solution(s):
    repeat, zero = 0, 0
    s = list(map(int, s))
    
    while s != [1]:
        zero += s.count(0)
        s = list(map(int, format(sum(s), 'b')))
        repeat += 1
    return repeat, zero