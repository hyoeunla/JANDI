# 10872. 팩토리얼
n = int(input())
result = 1
for i in range(1, n+1):
    result *= i
    # 0을 입력했다면 범위가 (1,1)이라 반복문을 실행하지않음
    # result만 출력되어 1이 출력됨
print(result)
