'''
061
price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
price = ['20180728', 100, 130, 140, 150, 160, 170]
출력 예시:
[100, 130, 140, 150, 160, 170]
,,,
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

'''
062
슬라이싱을 사용해서 홀수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

'''
063
슬라이싱을 사용해서 짝수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

064
슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
nums = [1, 2, 3, 4, 5]


nums = [1, 2, 3, 4, 5]
print(nums[::-1])

065
interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver']
interest 리스트를 사용하여 아래와 같이 화면에 출력하라.



interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

066 join 메서드
interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
interest 리스트를 사용하여 아래와 같이 화면에 출력하라.



interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
result = ' '.join(interest)
print(result)

067 join 메서드
interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
interest 리스트를 사용하여 아래와 같이 화면에 출력하라.



interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print('/'.join(interest) 

068 join 메서드
interest 리스트에는 아래의 데이터가 바인딩되어 있다.

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
result = '\n'.join(interest)
print(result)

069 문자열 split 메서드
회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.

string = "삼성전자/LG전자/Naver"
이를 interest 이름의 리스트로 분리 저장하라.

string = "삼성전자/LG전자/Naver"
result = string.split("/")
print(result)

070 리스트 정렬
리스트에 있는 값을 오름차순으로 정렬하세요.

data = [2, 4, 3, 1, 5, 10, 9]

data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)

