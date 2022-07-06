# 떡볶이 떡 만들기

n, m = list(map(int, input().split(' ')))

array = list(map(int, input().split(' ')))   # 각 떡의 개뱔 높이 정보를 입력받기

start = 0       # 이진 탐색을 위한 시작점과 끝점 설정
end = max(array)

result = 0      # 이진 탐색 수행(반복적)
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:       # 절랐을 떄의 떡의 양 계산
            total += x - mid

    if total < m:         # 떡의 양이 부족한 경우 더 많이 자르기(왼쪽 부분 탐색)
        end = mid - 1
    else:                 # 떡의 양이 충분한 경우 덜 자르기(오른쪽 부분 탐색)
        result = mid      # 최대한 덜 잘랐을 때가 정답이므로, 여기에서 result에 기록
        start = mid + 1

print(result)
