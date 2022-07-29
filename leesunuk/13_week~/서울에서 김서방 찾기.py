def solution(seoul):
    count=0
    for i in seoul:
        if i == 'Kim':
            break
        else:
            count+=1
    answer = '김서방은 '+str(count)+"에 있다"
    return answer