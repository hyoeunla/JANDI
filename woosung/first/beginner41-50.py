#041 upper 메서드
#다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
from winreg import HKEY_LOCAL_MACHINE


ticker = "btc_krw"
ticker1=ticker.upper()
print(ticker1)

#042 lower 메서드
#다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
ticker = "BTC_KRW"
ticker1=ticker.lower()
print(ticker1)

#043 capitalize 메서드
#문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
a="hello"
a1=a.replace("h","H")
print(a1)

a = "hello"
a = a.capitalize()
print(a)

#044 endswith 메서드
#파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
file_name = "보고서.xlsx"
file_name.endswith("xlsx")
print(file_name)

#045 endswith 메서드
#파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
file_name = "보고서.xlsx"
file_name.endswith(("xlsx","xls"))
print(file_name)

#046 startswith 메서드
#파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요.
file_name = "2020_보고서.xlsx"
file_name.startswith("2020")
print(file_name)

#047 split 메서드
#다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
a = "hello world"
a.split()

#048 split 메서드
#다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
ticker = "btc_krw"
ticker.split("_")

#049 split 메서드
#다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
date = "2020-05-01"
date.split("-")

#050 rstrip 메서드
#문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.

data = "039490     "
data=data.rstrip()
print(data)
