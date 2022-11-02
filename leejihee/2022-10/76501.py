# 76501. 음양 더하기
def solution(absolutes, signs):
    arr = []
    for i in range(len(signs)):
        if signs[i] == True:
            arr.append(absolutes[i])
        else:
            arr.append(-absolutes[i])
    return sum(arr)