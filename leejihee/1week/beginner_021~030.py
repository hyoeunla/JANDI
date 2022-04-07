# 021 문자열 인덱싱
# letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters = 'python'
print(letters[0], letters[2])

# 022 문자열 슬라이싱
# 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
print(license_plate[4:])

# 023 문자열 인덱싱
# 아래의 문자열에서 '홀' 만 출력하세요.
string = "홀짝홀짝홀짝"
print(string[0::2])

# 024 문자열 슬라이싱
# 문자열을 거꾸로 뒤집어 출력하세요.
string = "PYTHON"
print(string[::-1])

# 025 문자열 치환
# 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
phone_number = "010-1111-2222"
print(phone_number.replace("-"," "))

# 026 문자열 다루기
# 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
phone_number = "010-1111-2222"
print(phone_number.replace("-",""))

# 027 문자열 다루기
# url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
url = "http://sharebook.kr"
print(url[-2:]) #나의 풀이방법

url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[1]) #의도한 풀이방법

# 028 문자열은 immutable
# 아래 코드의 실행 결과를 예상해보세요.
'''
>> lang = 'python'
>> lang[0] = 'P'
>> print(lang)
문자열은 수정할 수 없다!!
'''

# 029 replace 메서드
# 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = 'abcdfe2a354a32a'
print(string.replace("a","A"))

# 030 replace 메서드
# 아래 코드의 실행 결과를 예상해보세요.
'''
>> string = 'abcd'
>> string.replace('b', 'B')
>> print(string)
두 번째에 변수를 작성하지 않아서 string은 그대로이다. 
'''