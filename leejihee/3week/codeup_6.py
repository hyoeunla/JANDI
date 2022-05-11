'''
[47]
정수 1개를 입력받아 2배 곱해 출력해보자.
'''
a = int(input())
print(a << 1)

'''
[48]
정수 2개(a, b)를 입력받아 a를 2^b배 곱한 값으로 출력해보자. ( a * 2(b 제곱) )
'''
a, b = map(int, input().split())
print(a << b)
