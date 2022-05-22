'''
[38]
정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
'''
a, b = map(int, input().split)
print(a+b)


'''
[39]
정수 2개를 입력받아 합을 출력하는 프로그램을 작성해보자.
'''
a, b = map(int, input().split)
print(a+b)


'''
[40]
입력된 정수의 부호를 바꿔 출력해보자.
'''
i = -int(input())
print(i)


'''
[41]
영문자 1개를 입력받아 그 다음 문자를 출력해보자.
영문자 'A'의 다음 문자는 'B'이고, 영문자 '0'의 다음 문자는 '1'이다
'''
askii = ord(input())
print(chr(askii+1))  # 헷갈리므로 다시 풀어볼 것


'''
[42]
정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.
'''
a, b = map(int, input().split())
print(a//b)


'''
[43]
정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.
'''
a, b = map(int, input().split())
print(a % b)


'''
[44]
정수를 1개 입력받아 1만큼 더해 출력해보자.
'''
a = int(input())
print(a+1)


'''
[45]
정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
첫 줄에 합
둘째 줄에 차,
셋째 줄에 곱,
넷째 줄에 몫,
다섯째 줄에 나머지,
여섯째 줄에 나눈 값을 순서대로 출력한다.
(실수, 소수점 이하 셋째 자리에서 반올림해 둘째 자리까지 출력)
'''
a, b = map(int, input().split())
print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a % b)
print(round(a/b, 2))


'''
[46]
정수 3개를 입력받아 합과 평균을 출력해보자.
합과 평균을 줄을 바꿔 출력한다.
평균은 소수점 이하 둘째 자리에서 반올림해서 소수점 이하 첫째 자리까지 출력한다.
'''
a, b, c = map(int, input().split())
print(a+b+c)
print(round((a+b+c)/3, 1))
