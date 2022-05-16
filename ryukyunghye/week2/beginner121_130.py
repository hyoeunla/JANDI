# 121. 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자일 경우 소문자로 변경해서 출력하라.
char = input("문자 하나를 입력하시오 : ")
if char.islower():
    print(char.upper())
else:
    print(char.lower())
# islower() : 문자의 소문자 여부를 판별

# 122. 정수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
score = int(input("점수를 입력하시오 : "))
if ((score >= 81) and (score <= 100)):
    print("grade is A")
elif ((score >= 61) and (score <= 80)):
    print("grade is B")
elif ((score >= 41) and (score <= 60)):
    print("grade is C")
elif ((score >= 21) and (score <= 40)):
    print("grade is B")
else:
    print("grade is E")

# 123. 사용자로부터 달러, 엔, 유로 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 각 통화별 환율은 다음과 같다. 상요자는 100달러, 1000엔, 13유로, 100위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
currency_name = {"달러": 1167, "엔": 1.096, "유로": 1268, "위안": 171}
money = input("금액을 입력하시오 : ")
num, currency = money.split()
print(float(num)*currency_name[currency], "원")

# 124. 사용자로부터 세 개의 숫자를 입력받은 후 가장 큰 숫자를 출력하라.
num1 = int(input("숫자1을 입력하시오 : "))
num2 = int(input("숫자2를 입력하시오 : "))
num3 = int(input("숫자3을 입력하시오 : "))
if ((num1 > num2) and (num1 > num3)):
    print(num1)
elif ((num2 > num1) and (num2 > num3)):
    print(num2)
else:
    print(num3)

# 125. 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력받고 통신사를 출력하는 프로그램을 작성하라.
number = input("휴대전화 번호 입력 : ").split("-")[0]
if number == "011":
    company = "SKT"
elif number == "016":
    company = "KT"
elif number == "019":
    company = "LGU"
else:
    company = "알 수 없음"
print("당신은 "+company+"사용자입니다.")
# print(f"당신은 {company} 사용자입니다.")

# 126. 우편번호는 5자리로 구성되는데, 앞의 세 자리는 구를 나타낸다. 예를 들어, 강북의 경우 010, 011, 012 세 자리로 시작한다.
number = input("우편번호 : ")[:3]
if number in ["010", "011", "012"]:
    print("강북구")
elif number in ["013", "014", "015"]:
    print("도봉구")
else:
    print("노원구")
# [:3] : 3번지 전까지 값을 받겠다 -> 0~2번지까지 받음

# 127. 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데 1,3은 남자 2,4는 여자를 의미한다. 사용자로부터 13자리의 주민등록 번호를 입력받은 후 성별(남자, 여자)를 출력하는 프로그램을 작성하라.
number = input("주민등록 번호 : ")[7]
if number == "1" or number == "3":
    print("남자")
else:
    print("여자")

'''
number = input("주민등록 번호 : ")
number = number.split("-")[1]
if number[0] == "1" or number[0]=="3":
    print("남자")
else:
    print("여자")
'''

# 128. 주민등록번호의 뒷 자리 7자리 중 두 번째와 세 번째는 지역코드를 의미한다. 주민등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라.
number = input("주민등록 번호 : ")
back = number.split("-")[1]
if (int((back[1:3])) >= 0 and int(back[1:3]) <= 8):
    print("서울입니다.")
else:
    print("서울이 아닙니다.")

''' 129. 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다. 먼저 앞에서부터 12자리의 숫자에 2,3,4,5,6,7,8,9,2,3,4,5를 차례로 곱한 뒤 그 값을 전부 더한다. 연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.
  8 2 1 0 1 0 - 1 6 3 5 2 1 0
x 2 3 4 5 6 7   8 9 2 3 4 5 
--------------------------------
1차 계산: (8*2 + 2*3 + 1*4 + 0*5 + 1*6 + 0*7 + 1*8 + 6*9 + 3*2 + 5*3 + 2*4 + 1*5) = (128 % 11) = 7
2차 계산: 11 -7 = 4
위와 같이 821010-1635210에 대해서 계산을 해보면 마지막 자리는 4가 되어야 함을 알 수 있다. 즉, 821010-1635210은 유효하지 않은 주민등록번호임을 알 수 있다.
다음과 같이 사용자로부터 주민등록번호를 입력받은 후 주민등록번호가 유효한지를 추렭하는 프로그램을 작성하라.'''
num = input("주민등록 번호 : ")
cal1 = int(num[0]) * 2 + int(num[1]) * 3 + int(num[2]) * 4 + int(num[3]) * 5 + int(num[4]) * 6 + int(num[5]) * \
    7 + int(num[7]) * 8 + int(num[8]) * 9 + int(num[9]) * 2 + \
    int(num[10]) * 3 + int(num[11]) * 4 + int(num[12]) * 5
cal2 = str(11 - (cal1 % 11))
if((num[-1]) == (cal2[-1])):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않은 주민등록번호입니다.")

'''130.  아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다. 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가+변동폭)이 최고가보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.'''
# import requests 저장할 때마다 계속 지워져서 주석처리 했습니다.
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
width = float(btc['max_price']) - float(btc['min_price'])
price = float(btc['opening_price'])
high_price = float(btc['max_price'])
if ((price+width) > high_price):
    print("상승장")
else:
    print("하락장")
