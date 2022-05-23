# 문제2. 큰 수의 법칙

# 나의 풀이
n, m, k = map(int, input().split())
num = sorted(map(int, input().split()))
total, count = 0, 0

for i in range(m):  # 더할 횟수(m)만큼 반복함
    if count < k:  # 연속으로 더할 수 있는 횟수(k)보다 작을 때만 더하는 조건식
        total += num[-1]  # 정렬했으므로 뒤에 있는 수가 가장 큼
        count += 1
    else:  # count가 k를 넘겼을 때
        total += num[-2]  # 뒤에서 두 번째 수를 더하고
        count = 0  # count는 0으로 초기화
print(total)

# 해설
n, m, k = map(int, input().split())
data = sorted(map(int, input().split()))

first = data[n-1]
second = data[n-2]
result = 0

while True:
    for i in range(k):  # 연속으로 더할 수 있는 횟수(k)보다 작을 때만 더하는 조건식
        if m == 0:  # 더할 횟수(m)이 0이면 멈추는 조건식
            break
        result += first
        m -= 1
    if m == 0:
        break
    result += second  # m==0이 안돼도 k만큼 더해지면 이쪽으로 빠짐
    m -= 1
print(result)
