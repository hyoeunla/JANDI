#011 변수 사용하기
#삼성전자라는 변수로 50,000원을 바인딩해보세요. 삼성전자 주식 10주를 보유하고 있을 때 총 평가금액을 출력하세요.
samsung= 50000
총평가금액=samsung*10
print(총평가금액)

#012 변수 사용하기
#다음 표는 삼성전자의 일부 투자정보입니다. 변수를 사용해서 시가총액, 현재가, PER 등을 바인딩해보세요.
#표
#항목	값
#시가총액	298조
#현재가	50,000원
#PER	15.79

시가총액=298000000000000
현재가=50000
PER=15.79

print("시가총액=",시가총액)
print("현재가=",현재가)
print("PER=",PER)

#013 문자열 출력
#변수 s와 t에는 각각 문자열이 바인딩 되어있습니다.
s = "hello"
t = "python"
#두 변수를 이용하여 아래와 같이 출력해보세요.
#실행 예:
#hello! python
print(s+"!",t)


#014 파이썬을 이용한 값 계산
#아래 코드의 실행 결과를 예상해보세요.
#2 + 2 * 3 답=8
print(2+2*3)

#015 type 함수
#type() 함수는 데이터 타입을 판별합니다. 변수 a에는 128 숫자가 바인딩돼 있어 type 함수가 int (정수)형임을 알려줍니다.
#>> a = 128
#>> print (type(a))
#<class 'int'>
#아래 변수에 바인딩된 값의 타입을 판별해보세요.
a = "132"  #srt형
print(type(a))

#016 문자열을 정수로 변환
#문자열 '720'를 정수형으로 변환해보세요.
num_str = "720"
int_num=int(num_str)
print(type(int_num))

#017 정수를 문자열 100으로 변환
#정수 100을 문자열 '100'으로 변환해보세요.
num = 100
str_num=str(num)
print(type(str_num))

num="100"
print(type(num))

#018 문자열을 실수로 변환
#문자열 "15.79"를 실수(float) 타입으로 변환해보세요.
num="15.79"
float_num=float(num)
print(type(float_num))

#019 문자열을 정수로 변환
#year라는 변수가 문자열 타입의 연도를 바인딩하고 있습니다. 이를 정수로 변환한 후 최근 3년의 연도를 화면에 출력해보세요.
year = "2020"
int_year=int(year)
print(int_year-1)
print(int_year-2)
print(int_year-3)

#020 파이썬 계산
#에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매되고 있습니다. 총 금액은 계산한 후 이를 화면에 출력해보세요. (변수사용하기)

month=48584
interest_free=36
total=month*interest_free

print("총 금액=", total)