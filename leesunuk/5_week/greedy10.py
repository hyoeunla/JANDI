# 10. 무지의 먹방 라이브
def solution(food_times, k):
    count = 1
    i = 0
    food = 0
    while food < len(food_times):  # 음식을 다 먹지 않았다면

        if k == count:  # 끊기는 시간과 count가 일치해지면
            break  # 멈춤

        if food_times[i] == food_times[-1]:  # i번째 음식이 리스트의 마지막 음식이라면
            i = 0  # 리스트 첫번째로 다시 이동
            count += 1  # 이동 했으니 카운트 +1

        if food_times[i] == 0:  # 여기 있는 음식을 다 먹었다면
            i += 1  # 다음 칸으로 이동

        if food_times != 0:  # 여기 음식이 남았다면
            food_times[i] -= 1  # 한입 먹어줌

        for j in food_times:
            if j == 0:  # j번째 음식이 비었다면
                food += 1  # food+1 추가
            else:  # 아니라면
                food = 0  # 다시 초기화
        i += 1  # 다음 음식을 찾으러 +1
        count += 1  # 한번 먹었으니 +1

    answer = i  # 멈췄을 당시 i값을 가져옴

    if food == len(food_times):  # 방송이 끊기기전 음식을 다 먹었다면
        return -1
    else:
        return answer  # i값 리턴
