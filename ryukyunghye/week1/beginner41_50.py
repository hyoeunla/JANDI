# 041 upper 메서드
ticker = "btc_krw"
print(ticker.upper())
Ticker = ticker.upper()
print(Ticker)
# upper() : 문자열을 대문자로
# + 원본 문자열은 유지, 새로운 문자열 객체가 반환

# 042 lower 메서드
ticker = "BTC_KRW"
print(ticker.lower())
ticker1 = ticker.lower()
print(ticker1)

# 043 capitalize 메서드
a = 'hello'
print(a.capitalize())
b = a.capitalize()
print(b)
# capitalize() : 문자열의 첫 글자는 대문자로, 나머지는 소문자로 변환

# 044 endswith 메서드
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))  # true
# endswith() : 특정 문자로 끝나는지 확인(True/False)

# 045 endswith 메서드
file_name = "보고서.xlsx"
print(file_name.endswith(("xlsx", "xls")))  # true
# 두가지인 경우 ()를 2번 쓰는 이유는 아직 잘 모르겠다

# 046 startswith 메서드
file_name = "2020_보고서.xlsx"
print(file_name.startswith("2020"))  # true
# startswith() : 특정 문자로 시작하는지 확인(True/False)

# 047 split 메서드
a = "hello world"
print(a.split())
# split() : 문자열을 분리할 때 사용, 값o_그 값을 기준으로, 값x_공백을 기준으로 문자열을 분리

# 048 split 메서드
ticker = "btc_krw"
print(ticker.split("_"))

# 049 split 메서드
data = "2020-05-01"
print(data.split("-"))

# 050 rstrip 메서드
data = "039490    "
print(data.rstrip())
data1 = data.rstrip()
print(data1)
# rstrip() : 공백이 제거된 새로운 문자열 객체가 반환됨, 기존의 공백이 포함된 문자열은 메모리에서 자동 삭제
