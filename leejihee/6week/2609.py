# 2609. 최대공약수와 최소공배수
a, b = map(int, input().split())

# 최대공약수
for i in range(min(a, b), 0, -1):  # 최대공약수를 구하기 위해 나눌 수 있는 큰 값부터 대입해봄
    if a % i == 0 and b % i == 0:  # 둘다 나머지가 0일 때 공약수가 구해짐
        print(i)
        break

# 최소공배수
for i in range(max(a, b), (a*b)+1):  # 둘이 최소공배수가 될 경우 중 가장 작은 수는 n*1, 가장 큰 수는 둘을 곱한 수
    if i % a == 0 and i % b == 0:  # i에서 나눌 때 둘 다 0이 되어야 최소공배수가 됨
        print(i)
        break
