def solution(x):
    a = list(str(x))
    count = 0
    for i in a:
        count += int(i)
    if x % count == 0:
        answer = True
    else:
        answer = False
    return answer
