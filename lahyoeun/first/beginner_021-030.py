'''
021
letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
>> letters = 'python'
'''
letters = 'python'
print(letters[0], letters[2])

'''
022
자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
>> license_plate = "24가 2210"
'''
num = '24가 2210'
print(num[4:8])  # 내가 쓴 답
print(num[-4:])  # 정답

'''
023
아래의 문자열에서 '홀' 만 출력하세요.
>> string = "홀짝홀짝홀짝"
'''
string = "홀짝홀짝홀짝"
print(string[0], string[2], string[4])  # 내가 쓴 답
print(string[::2])  # 정답

'''
024
문자열을 거꾸로 뒤집어 출력하세요.
>> string = "PYTHON"
'''
string = "PYTHON"
print(string[:: -1])

'''
025
아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
>> phone_number = "010-1111-2222"
실행 예
010 1111 2222
'''
num = "010-1111-2222"
print(num[0:3], num[4:8], num[9:13])  # 내 풀이

num1 = num.replace("-", " ")
print(num1)  # 정답

'''
026
25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
실행 예
01011112222
'''
phone = "010-1111-2222"
phone1 = phone.replace("-", "")
print(phone1)

'''
url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
>> url = "http://sharebook.kr"
실행 예:
kr
'''
url = "http://sharebook.kr"
print(url[-2:])  # 내가 푼 풀이(잘못된 것)

url = "http://sharebook.kr"
url_split = url.split('.')
print(url_split[-1])  # 정답

'''
028
아래 코드의 실행 결과를 예상해보세요.
>> lang = 'python'
>> lang[0] = 'P'
>> print(lang)
'''
# 오류가 남 문자열은 수정이 불가능

'''
029
아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
>> string = 'abcdfe2a354a32a'
실행 예:
Abcdfe2A354A32A
'''
string = 'abcdfe2a354a32a'
string_a = string.replace('a', "A")
print(string_a)  # 내가 푼 풀이

string = 'abcdfe2a354a32a'
string = string.replace('a', "A")
print(string)  # 정답

'''
030
아래 코드의 실행 결과를 예상해보세요.
>> string = 'abcd'
>> string.replace('b', 'B')
>> print(string)
'''
# abcd가 출력됨
