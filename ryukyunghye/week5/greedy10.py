# 10. 무지의 먹방 라이브
# 다시 풀어야 함
def solution(food_times, k):
    low, high = 0, 100000000
    n, cutting, idx = len(food_times), 0, 0
    while low <= high:
        mid = (low+high) // 2
        v = n * mid
        for f in food_times:
            tmp = f-mid
            if tmp < 0:
                v += tmp
        if v <= k:
            cutting, idx = mid, v
            low = mid + 1
        else:
            high = mid - 1
    food_times = [f-cutting for f in food_times]
    for i in range(n):
        if food_times[i] > 0 and idx == k:
            return i+1
        else:
            if food_times[i] > 0:
                idx += 1
    return -1
