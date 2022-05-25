# 문제2. 큰 수의 법칙

n, m, k = map(int, input().split())  # n개의 수를 공백으로 구분하여 입력
num = list(map(int, input().split()))
num.sort()  # 입력받은 수 정렬

first = num[n - 1]  # 가장 큰 수
second = num[n - 2]  # 두 번째로 큰 수

result = 0

while True:
    for i in range(k):  # 가장 큰 수를 k번 더하기
        if m == 0:  # m이 0이면 반복문 탈출
            break
        result += first
        m -= 1  # 더할 때마다 1씩 빼기
    if m == 0:  # m이 0이라면 반복문 탈출
        break
    result += second  # 두 번째로 큰 수를 한 번 더하기
    m -= 1  # 더할 때마다 1씩 빼기
print(result)
