'''
121:번: 사용자로부터 문자 한 개를 입력 받고, 소문자일 경우 대문자로, 대문자 일 경우, 소문자로 변경해서 출력하라.
'''
a = input("문자 한개를 입력해주세요: ")
b = a.islower()
if b == True:
    print(a.upper())
else:
    print(a.lower())

'''
또 다른 방법
'''
a = input("")
if a.islower():
    print(a.upper())
else:
    print(a.lower())

'''
122번: 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.
(A(81~100), B(61~80), C(41~60), D(21~40), E(0~20))
'''
score = input("점수를 입력해주세요: ")
iscore = int(score)
if iscore > 80:
    print("grade is A")
elif 81 > iscore > 60:
    print("grad is B")
elif 61 > iscore > 40:
    print("grad is C")
elif 41 > iscore > 20:
    print("grad is D")
else:
    print("grad is E")

'''
123번: 사용자로부터 달러, 엔, 유로, 또는 위안 금액을 입력받은 후 이를 원으로 변환하는 프로그램을 작성하라. 각 통화별 환율은 다음과 같다.
 사용자는 100 달러, 1000 엔, 13 유로, 100 위안과 같이 금액과 통화명 사이에 공백을 넣어 입력한다고 가정한다.
달러    1167
엔     1.096
유로    1268
위안	171
'''
HW = {"달러": 1167, "엔": 1.086, "유로": 1268, "위안": 171}
a = input("입력: ")
b, c = a.split()
print(float(b) * HW[c], "원")

'''
124번: 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자를 출력하라.
'''
a = input("첫번째 숫자를 입력해주세요: ")
b = input("두번째 숫자를 입력해주세요: ")
c = input("세번째 숫자를 입력해주세요: ")

if a > b:
    d = a
else:
    d = b

if d > c:
    print(d)
else:
    print(c)

'''
다른 방법
'''
a = input("첫번째 숫자를 입력해주세요: ")
b = input("두번째 숫자를 입력해주세요: ")
c = input("세번째 숫자를 입력해주세요: ")

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

'''
125번:휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다.
사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.
011	SKT
016	KT
019	LGU
010	알수없음
'''
num = input("휴대전화 번호 입력: ")
if num[0:3] == "011":
    print("당신은 SKT 사용자입니다.")
elif num[0:3] == "016":
    print("당신은 KT 사용자입니다.")
elif num[0:3] == "019":
    print("당신은 LGU 사용자입니다.")
else:
    print("알수 없음")

'''
다른 방법(split()을 이용한 방법)
'''
num = input("휴대전화 번호 입력: ")
nb = num.split("-")[0]
if nb == "011":
    com = "SKT"
elif nb == "016":
    com = "KT"
elif nb == "019":
    com = "LGU"
else:
    com = "알수없음"
print(f"당신은 {com} 사용자입니다.")

'''
126번: 우편번호는 5자리로 구성되는데, 앞의 세자리는 구를 나타낸다.
예를들어, 강북구의 경우 010, 011, 012 세 자리로 시작한다.
010~012	강북구
013~015	도봉구
016~019 노원구
'''
a = input("우편번호를 입력해주세요: ")
b = a[0:3]
if b in ["010", "012", "013"]:
    print("강북구")
elif b in ["014", "015", "016"]:
    print("도봉구")
elif b in ["017", "018", "019"]:
    print("노원구")

'''
127번: 주민등록번호 뒷 자리 7자리 중 첫째 자리는 성별을 나타내는데, 1, 3은 남자 2, 4는 여자를 의미한다.
사용자로부터 13자리의 주민등록번호를 입력 받은 후 성별 (남자, 여자)를 출력하는 프로그램을 작성하라.
'''

a = input("주민등록번호 13자리를 입력해주세요: ")
b = a[7:8]
if b in ["2", "4"]:
    print("여자")
elif b in ["1", "3"]:
    print("남자")

'''
다른방법(split()을 이용한 방법)
'''

주민번호 = input("주민등록번호: ")
주민번호 = 주민번호.split("-")[1]
if 주민번호[0] == "1" or 주민번호[0] == "3":
    print("남자")
else:
    print("여자")

'''
128번: 주민등록번호의 뒷 자리 7자리 중 두번째와 세번째는 지역코드를 의미한다.
 주민 등록 번호를 입력 받은 후 출생지가 서울인지 아닌지 판단하는 코드를 작성하라
 00 ~ 08	서울
 09 ~ 12	부산
'''
a = input("주민등록번호 13자리를 입력해주세요: ")
b = a.split("-")[1]
c = int(b[1:3])
if 0 < c < 9:
    print("서울")
else:
    print("서울이 아닙니다")

'''
129번: 주민등록번호는 13자리로 구성되는데 마지막 자리수는 주민등록번호의 유효성을 체크하는데 사용된다.
 먼저 앞에서부터 12자리의 숫자에 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5를 차례로 곱한 뒤 그 값을 전부 더한다.
  연산 결과 값을 11로 나누면 나머지가 나오는데 11에서 나머지를 뺀 값이 주민등록번호의 마지막 번호가 된다.
'''
a = input("주민등록번호를 입력해주세요")
d = (int(a[0])*2 + int(a[1])*3 + int(a[2])*4 +
     int(a[3])*5 + int(a[4])*6 + int(a[5])*7 +
     int(a[7])*8 + int(a[8])*9 + int(a[9])*2 + int(a[10])*3 + int(a[11])*4 + int(a[12])*5) % 11
e = 11-d
e = str(e)
if(e == a[13]):
    print("유효한 주민등록번호입니다.")
else:
    print("유효하지 않는 주민등록번호입니다.")

'''
130번: 아래 코드는 비트코인의 가격 정보를 딕셔너리로 가져오는 코드이다.
import requests
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']
btc 딕셔너리 안에는 시가, 종가, 최고가, 최저가 등이 저장되어 있다.
 최고가와 최저가의 차이를 변동폭으로 정의할 때 (시가 + 변동폭)이 최고가 보다 높을 경우 "상승장", 그렇지 않은 경우 "하락장" 문자열을 출력하라.

Key Name	Description
opening_price	최근 24시간 내 시작 거래금액
closing_price	최근 24시간 내 마지막 거래금액
min_price	최근 24시간 내 최저 거래금액
max_price	최근 24시간 내 최고 거래금액
'''
btc = requests.get("https://api.bithumb.com/public/ticker/").json()['data']

BD = float(btc['max_price'])-float(btc['min_price'])
SG = float(btc['opening_pirce'])
MX = float(btc['max_price'])

if SG + BD > MX:
    print("상승장")
else:
    print("하락장")
