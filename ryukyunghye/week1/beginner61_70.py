# 061 price 변수에는 날짜와 종가 정보가 저장돼 있다. 날짜 정보를 제외하고 가격 정보만 출력하라.(힌트: 슬라이싱)
price = ['20180728', 100, 130, 140, 150, 160, 170]
print(price[1:])

# 062 슬라이싱을 사용해서 홀수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[::2])  # 처음부터 끝까지 두 칸 간격으로

# 063 슬라이싱을 사용해서 짝수만 출력하라.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[1::2])  # 1번지부터 두 칸 간격으로

# 064 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
nums = [1, 2, 3, 4, 5]
print(nums[::-1])  # 처음부터 끝까지 역순으로

# 065  interest 리스트에는 아래의 데이터가 바인디오디어 있다. interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
interest = ['삼성전자', 'LG전자', 'Naver']
print(interest[0], interest[2])

# 066 interest 리스트에는 아래의 데이터가 바인딩되어 있다. interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("".join(interest))
# '구분자'.join(리스트) : 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐준다

# 067 interest 리스트에는 아래의 데이터가 바인딩되어 있다. interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

# 068  interest 리스트에는 아래의 데이터가 바인딩되어 있다.
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

# 069 회사 이름이 슬래시('/')로 구분되어 하나의 문자열로 저장되어 있다. 이를 interest 이름의 리스트로 분리 저장하라.
string = "삼성전자/LG전자/Naver"
interest = string.split('/')
print(interest)

# 070 리스트에 있는 값을 오름차순으로 정렬하세요.
data = [2, 4, 3, 1, 5, 10, 9]
data1 = data.sort()
print(data1)
data1 = sorted(data)
print(data1)
# sort() : 리스트 원본값을 직접 수정
# sorted() : 원본 값은 그대로 두고 정렬 값을 반환
