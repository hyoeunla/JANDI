'''61번: price 변수에는 ['20180728', 100, 130, 140, 150, 160, 170] 가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱) '''
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

'''62번: 슬라이싱을 사용해서 홀수만 출력하라. (nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) '''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])

'''63번: 슬라이싱을 사용해서 짝수만 출력하라. (nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) '''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])

'''64번: 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라. (nums = [1, 2, 3, 4, 5])'''
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

'''65번: interest 리스트에는 interest = ['삼성전자', 'LG전자', 'Naver']가 바인딩되어 있다. 삼성전자 Naver 두개만 화면에 출력하라.'''
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

'''66번: interest 리스트에는 interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']가 바인딩되어 있다.
삼성전자 LG전자 Naver SK하이닉스 미래에셋대우 를 출력하라 '''
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

'''67번: 위 interest 리스트를 사용하여 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우 를 출력하라'''
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

'''68번: 위 interest 리스트를 사용하여
삼성전자
LG전자
Naver
SK하이닉스
미래에셋대우
와 같이 출력하라 '''

interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

'''69번: 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열(string = "삼성전자/LG전자/Naver") 로 저장되어 있다. 이를 interest 이름의 리스트로 분리 저장하라.'''

string = "삼성전자/LG전자/Naver"
interest=string.split("/")
print (interest[0:3])

'''70번: 리스트에 있는 값을 오름차순으로 정렬하세요. (data = [2, 4, 3, 1, 5, 10, 9]) '''
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print (data)
