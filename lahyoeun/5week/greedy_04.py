n, k = map(int, input().split())  # n과 k의 값을 나눠 받음
dap = 0  # 횟수를 저장해 줄 변수 0으로 초기화

while n > k:  # k보다 n이 클 때
    while n % k != 0:  # 나머지가 0이 아니라면
        n = n-1  # 하나 뺴주고
        dap = dap + 1  # 회수는 더해줌
    n //= k  # 나머지가 0이면 나눠줌
    dap = dap + 1  # 횟수 더해줌

while n > 1:
    n = n-1
    dap = dap + 1

print(dap)
