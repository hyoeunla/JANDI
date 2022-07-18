# 백준 소수 구하기
# 내 1풀이 시간초과
m, n = map(int, input().split())  # m과 n을 입력받음
prime_number = list(range(m, n+1))  # 범위의 모든 값을 넣어줌
for i in range(m, n+1):  # 범위만큼 반복
    for j in range(2, int(i**0.5)+1):  # 나누어줄 값 범위
        if i % j == 0:  # 나머지가 없으면
            prime_number.remove(i)  # 소수가 아니므로 지워줌
            break
for i in prime_number:  # 소수만 남은 리스트 출력
    print(i)

# 내 풀이 2


def isPrime(n):  # isPrime이라는 함수를 정의
    if n == 1:  # 1 일 경우 false 반환
        return False
    else:
        for i in range(2, int(n**0.5)+1):  # 아니라면 이 범위에서 나눠주기
            if n % i == 0:  # 나누어 떨어지면
                return False  # false 반환
        return True


m, n = map(int, input().split())
for i in range(m, n+1):  # 입력받은 범위에서 반복
    if isPrime(i):  # isPrime 함수가 참인 i(소수) 라면
        print(i)  # print 해줌
