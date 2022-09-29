# 12943. 콜라츠 추측
def solution(num):
    count = 0
    while num != 1:
        count +=1
        if count == 500:
            return -1
        else:
            num = num//2 if num % 2 == 0 else num * 3 + 1
    return count