# 문제10. 무지의 먹방라이브

import heapq

# 나의 풀이
food_times = list(map(int, input().split()))  # 3 1 2이면 다 먹는데 6초가 걸린다는 뜻
k = int(input())  # 5초에 장애발생
time = 0

while time < k:  # 에러나는 시간 전까지 게속 반복하도록
    for i in range(len(food_times)):
        if food_times[i] <= 0:  # 시간이 0이 되었을 때 반복문 나가기
            continue
        else:
            food_times[i] -= 1
            time += 1
        print("{}~{}초 동안에 {}번 음식을 섭취한다. 남은 시간은 {}이다.".format(
            time-1, time, i+1, food_times))

# print("{}초에서 네트워크 장애가 발생. {}번부터 음식 섭취가 중단되었으므로, 장애 복구 후에 {}번부터 다시 먹으면 된다.".format(time, ?, ?))
# 구하지 못함

# 해설


def solution(food_times, k):
    if sum(food_times) <= k:  # 다 먹었으면(합이 먹는 시간보다 적으면) -1 출력
        return -1

    # 시간이 작은 음식부터 빼기 = 우선순위 큐 사용
    q = []
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i]), i+1)

    sum_value = 0
    previous = 0
    lenght = len(food_times)

    # 먹기위해 사용한 시간 + (현재 음식 시간-이전 음식 시간) * 현재 음식 개수와 k비교
    while sum_value + ((q[0][0]-previous)*lenght) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now-previous)*lenght
        lenght -= 1  # 다먹은 음식 제외
        previous = now  # 이전 음식 시간 재설정

    # 남은 음식 중 몇 번쨰 음식인지 확인
    result = sorted(q, key=lambda x: x[1])
    return result[(k-sum_value) % lenght][1]
