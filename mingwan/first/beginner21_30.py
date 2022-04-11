#021 문자열 인덱싱
#letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
letters='pyhton'
#파이썬 문자열에서 한 글자를 가져오는 것을 인덱싱이라고 부릅니다. 파이썬 인덱싱은 0부터 시작합니다.
lang = 'phyton'
print(lang[0],lang[2])

#022 문자열 슬라이싱
#자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
license_plate = "24가 2210"
#문자열에서 여러 글자를 가져오는 것을 슬라이싱이라고 부릅니다. 음수 값은 문자열의 뒤에서부터 인덱싱 또는 슬라이싱함을 의미합니다. 슬라이싱에서 시작 인덱스를 생락혀면 0으로 간주하고 끝 인덱스를 생략하면 문자열의 끝을 의미합니다.
license_plate = "24가 2210"
print(license_plate[4:8])
print(license_plate[4:])
print(license_plate[-4:])

#023 문자열 인덱싱
#아래의 문자열에서 '홀'만 출력하세요
#슬라이싱할 때 시작인덱스:끝인덱스:오프셋을 지정할 수 있습니다.
 string = "홀짝홀짝홀짝"
 print(string[0], string[2],string[4],sep="")
 print(string[::2])

 #024 문자열 슬라이싱
 #문자열을 거꾸로 뒤집어 출력하세요.
 string = "PYTHON"
 print(string[::-1])

 #025 문자열 치환
 #아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
 phone_number="010-1111-2222"
 #파이썬 문자열에서 replace 메서드를 사용하면 문자열을 일부를 치환할 수 있습니다. 문자열은 수정할 수 없는 자료형이므로 기존 문자열은 그대로 두고 치환된 새로운 문자열이 리턴됩니다.
 phone_number= "010-1111-2222"
 a= phone_number.replace("-","")
 print(phone_number1)
 print(a)

 #026 문자열 다루기
 #25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
 phone_number = "010-1111-2222"
 a = phone_number.replace('-','')
 print(a)

 #027 문자열 다루기
 #url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
 #문자열로 표현된 url에서 .을 기준으로 분리합니다. 분리된 url 중 마지막을 인덱싱하면 도메인만 출력할 수 있습니다.
 url="http://sharebook.kr"
 url_split=url.split(".")
print(url_split[1])

#028 문자열은 immutable
#문자열은 수정할 수 없습니다. 실행 결과를 확인해보면 문자열이 할당(assignment) 메서드를 지원하지 않음을 알 수 있습니다.
lang="python"
lang[0]='p'
print(lang)

#029 replace 메서드
#아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
string = "abcdef2a354a32a"
string = string.replace('a',"A")
pring(string)

#030 replace 메서드
string = "abcd"
string = string.replace('b',"B")
print(string)

