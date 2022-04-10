'''41번: ticker = "btc_krw"를 대문자 BTC_KRW로 변경하세요.

내답: ticker = "btc_krw";t1=ticker.replace("btc_krw","BTC_KRW");print(t1)

다른 방법: ticker = "btc_krw";ticker1 = ticker.upper();print(ticker1)

차이점: 내 방식은 replace로 기존에 있던걸 삭제하고 치환하는 방법이고, 다른 방법은 upper() 메서드를 호출해서 소문자를 대문자로 치환해주는 것이다.''''

'''42번: ticker = "BTC_KRW"를 소문자 btc_krw로 변경하세요.'''
ticker = "BTC_KRW"; t1=ticker.lower();print(t1)

'''43번: 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요. '''

m="hello"; m1=m.capitalize(); print(m1)

'''44번: 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.

내답: file_name = "보고서.xlsx"; file_name.endswith(); print(file_name)

해답: file_name = "보고서.xlsx"; file_name.endswith("xlsx"); print(file_name)

변수.endswith("확인하고 싶은 문자열")
'''

'''45번: 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요. 

내답: file_name = "보고서.xlsx"; file_name.endswith("xlsx", "xls"); print(file_name)
해답: file_name = "보고서.xlsx"; file_name.endswith(("xlsx", "xls")); print(file_name)

한번더 ()로 감싸줘야 된다. '''

'''46번: 파일 이름이 문자열로 저장되어 있을 때 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인해보세요. '''
file_name = "2020_보고서.xlsx"; file_name.startswith("2020")

'''47번: a = "hello world" 공백을 기준으로 문자열을 나눠보세요.'''
a = "hello world";b=a.split(" ");print(b)

'''48번: ticker = "btc_krw" btc와 krw로 나눠보세요. '''
ticker = "btc_krw"; t1=ticker.split("_");print(t1)

'''49번: date = "2020-05-01" 연도, 월, 일로 나눠보세요.'''

date = "2020-05-01"; d1=date.split("-");print(d1)

'''50번: data = "039490     " 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.'''
data = "039490     "; data.rstrip();print(data)

