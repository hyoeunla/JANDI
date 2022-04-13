'''
021 문자열 인덱싱
letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
>> letters = 'python'
실행 예
p t
'''
letters = 'python'
print(letters[0], letters[2])  # 파이썬 인덱싱은 0부터 시작

'''
022 문자열 슬라이싱
자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
>> license_plate="24가 2210"
실행 예: 2210
'''
license_plate = "24가 2210"
print(license_plate[4:8])

'''
023 문자열 인덱싱
아래의 문자열에서 '홀'만 출력하세요.
>> string="홀짝홀짝홀짝"
실행 예:
홀홀홀
'''
string = "홀짝홀짝홀짝"
print(string[0:6:2])  # 슬라이싱할 때 시작인덱스:끝인덱스:오프셋 지정할 수있고 시작,끝 생략 가능

'''
024 문자열 슬라이싱
문자열을 거꾸로 뒤집어 출력하세요.
>> string="PYTHON"
실헹 예:
NOHTYP
'''
string = "PYTHON"
print(string[::-1])  # 뒤집는 건 시작과 끝에서 -1

'''
025 문자열 치환
아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
>> phone_number="010-1111-2222"
실행 예
010 1111 2222
'''
phone_number = "010-1111-2222"
a = phone_number.replace("-", " ")
print(a)

'''
026 문자열 다루기
25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
실행 예
01011112222
'''
phone_number = "010-1111-2222"
a = phone_number.replace("-", "")
print(a)

'''
027 문자열 다루기
url에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
>> url="http://sharebook.kr"
실행 예
kr
'''
url = "http://sharebook.kr"
a = url.split(".")
print(a[1])

'''
028 문자열은 immutable
아래 코드의 실행 결과를 예상해보세요.
>> lang='python'
>> lang[0]='p'
>> print(lang)
'''
lang = 'python'
lang[0] = 'p'
print(lang)
# 문자열은 수정할 수 없다.

'''
029 relplace 메서드
아래 문자열에서 소문자 'a'응 대문자 'A'로 변경하세요.
>> string='abcdfe2a354a32a'
실행 예:
Abcdfe2A354A32A
'''
string = 'abcdfea354a32a'
a = string.replace('a', "A")
print(a)

'''
030 replace 메서드
아래 코드의 실행 결과를 예상해보세요.
>> string='abcd'
>> string.replace('b', 'B')
>> print(string)
'''
string = 'abcd'
string.replace('b', 'B')
print(string)
# 문자형은 변경할 수 없는 자료형이기 때문에 abcd가 그대로 출력된다.
# replace 메서드를 사용하면 원본은 그대로 둔채로 변경된 새로운 문자열 객체를 리턴해준다.
