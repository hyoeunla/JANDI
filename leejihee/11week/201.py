# 3. 떡볶이 떡 만들기
n, m = map(int, input().split())
length = list(map(int, input().split()))

# 최적의 수(=h)를 찾기 위해 이진탐색을 해야 함
start = 0
end = max(length)  # 떡 중에 가장 긴 떡

h = 0
while start <= end:
    total = 0  # 잘린 떡의 길이
    mid = (start+end)//2
    for i in length:
        if i > mid:  # 떡이 mid보다 길면 자름, 안 길면 못 자름
            total += i - mid  # 잘린 떡 합하기
    if total < m:
        # 반토막내면서 자르다가 떡이 m보다 부족해지면 끝점을 감소시킴 (더 자른다)
        end = mid-1
    else:  # 잘린 떡의 합이 m보다 크거나 같을 때
        # 떡이 아직 m보다 크면 시작점을 늘림 (덜 자른다)
        h = mid  # 최적의 h를 구하므로 기록해두고
        start = mid+1  # 시작점을 늘렸을 때 길이 확인해보기
print(h)
# h를 뺀 것의 합이 m보다 커야함.
# h를 구하는 것...
