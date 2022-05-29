# 문제8. 만들 수 없는 금액

# 1부터 target-1까지의 숫자를 만들 수 있다.
# target보다 작은 지 확인하고 크다면 target값을 업데이트 한다.
coin = int(input())
won = sorted(map(int, input().split()))  # 3 2 1 1 9
target = 1  # 처음에 1을 만들 수 있는지 확인하기 위해 1로 설정 (1이 최소이므로)

for i in won:  # 1 1 2 3 9 (5번 돎)
    if target < i:
        break
    target += i
# target(= 1)이 1보다 작은지 확인
# target(= 2)이 1보다 작은지 확인
# target(= 3)이 2보다 작은지 확인
# target(= 5)이 3보다 작은지 확인
# target(= 8)이 9보다 작은지 확인

print(target)
