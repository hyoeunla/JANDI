# 10. 기초 - 삼항 연산

# [63] 입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자.
a, b = map(int, input().split())
print(a > b and a or b)
print(max(a, b))
# [64] 입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자. (단, 삼항 연산자 이용)
a, b, c = map(int, input().split())
# 참값 if 조건식 else 거짓값
num = a if a < b else b
print(num)
print(num if num < c else c)
# [우리밋이 알려주는 Bonus 문제 (3)] 1개의 정수형 입력이 들어오면 삼항 연산을 이용하여 '홀수'와 '짝수'를 판별하여라
num = int(input())
print('짝수' if num % 2 else "홀수")
