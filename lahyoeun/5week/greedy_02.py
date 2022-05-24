n, m, k = map(int, input().split())
add = list(map(int, input().split()))

add.sort()  # 정렬
first = add[n-1]  # 배열에서 가장 큰 수
second = add[n-2]   # 배열에서 두번째로 큰 수

a = 0
while True:
    for i in range(k):  # k번 반복
        if m == 0:
            break  # 반복문 탈출
        a = a + first  # a에 first 값 더해주기
        m = m-1  # 횟수인 m번 반복할 때 마다 줄여주기
    if m == 0:  # 만약 이렇게 수행하고 m이 0이면
        break  # 반복문 탈출
    a = a + second  # 아니면 2번째로 큰 수 더해주고
    m = m-1  # 횟수 줄임
print(a)  # 결과값 출력
