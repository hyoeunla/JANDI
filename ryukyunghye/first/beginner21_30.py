# 021 문자열 인덱싱
letters = 'python'
print(letters[0],letters[2])

# 022 문자열 슬라이싱
license_plate ="24가 2210"
print(license_plate[4:])

# 023 문자열 인덱싱
string = "홀짝홀짝홀짝"
print(string[::2]) # 시작/끝/오프셋

# 024 문자열 슬라이싱
string ="PYTHON"
print(string[::-1]) 

# 025 문자열 치환
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-"," ")
print(phone_number1)
print(phone_number.replace("-"," "))

# 026 문자열 다루기
phone_number = "010-1111-2222"
phone_number1 = phone_number.replace("-",'')
print(phone_number1)
print(phone_number.replace("-",''))

# 027 문자열 다루기
url = "https://sharebook.kr"
url_split = url.split('.') # .split('') : '' 속을 기준으로 분리함
print(url_split[-1])

# 028 문자열은 immutable
lang ='python'
lang[0] = 'P'
print(lang) 
# 문자열은 수정할 수 없다. 실행 결과를 확인해보면 할당 메서드를 지원하지 않음을 알 수 있다

# 029 replace 메서드
string = 'abcdfe2a354a32a'
string(string.replace('a','A')) # 'a'를 'A'로 변경한다
print(string)                   # Abcdfe2A354A32A

# 030 replace 메서드
string ='abcd'
string.replace('b','B')
print(string)   # abcd
# replace 메서드를 사용하면 원본은 그대로 둔 채로 변경된 새로운 문자열 객체를 리턴해준다
